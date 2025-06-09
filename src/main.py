
import os
import sys
import subprocess
import threading
import argparse
import logging
import time

from utils.logger import configurar_logger
from collectors.coletor import Coletor

# Tabelas principais
from service.empresas_service import process_csv_files as process_empresas
from repository.empresas_repository import ConexaoBanco as BancoEmpresas

from service.periodicos_eventuais_service import process_csv_files as process_ipe
from repository.periodicos_eventuais_repository import ConexaoBanco as BancoIPE

from service.formulario_referencia_service import process_csv_files as process_fre
from repository.formulario_referencia_repository import ConexaoBanco as BancoFRE

from service.parecer_demonstrativo_service import (
    process_csv_files as process_parecer_demo,
)
from repository.parecer_demonstrativo_repository import ConexaoBanco as BancoParecerDemo

from service.parecer_trimestral_service import process_csv_files as process_parecer_trim
from repository.parecer_trimestral_repository import ConexaoBanco as BancoParecerTrim

from service.numeros_acoes_service import process_csv_files as process_num_acoes
from repository.numeros_acoes_repository import ConexaoBanco as BancoNumAcoes

from service.demostrativo_financeiro_service import process_dfp_files as process_dfp
from repository.demostrativo_financeiro_repository import (
    ConexaoBanco as BancoDemostrativo,
)

from service.informacao_trimestral_service import process_itr_files as process_itr
from repository.informacao_trimestral_repository import (
    ConexaoBanco as BancoInformacaoTri,
)

# Auxiliares extras
from service.tabelas_auxiliares_extras import (
    executar_categoria_documento,
    executar_tipo_parecer,
    executar_escala_monetaria,
    executar_ordem_exercicio,
    executar_moeda,
    executar_tipo_relatorio_auditor,
    executar_tipo_relatorio_especial,
    executar_assunto_prensa,
    executar_especie_documento_eventual,
    executar_tipo_evento,
    executar_tipo_apresentacao_evento,
)

# Auxiliares simples
from service.especie_controle_service import (
    process_csv_files as process_especie_controle,
)
from repository.especie_controle_repository import ConexaoBanco as BancoEspecie_controle

from service.situacao_emissor_service import (
    process_csv_files as process_situacao_emissor,
)
from repository.situacao_emissor_repository import ConexaoBanco as BancoSituacao_emissor

from service.setor_atividade_service import process_csv_files as process_setor_atividade
from repository.setor_atividade_repository import ConexaoBanco as BancoSetor_atividade


def configurar_argumentos():
    parser = argparse.ArgumentParser(description="Processador CVM")
    parser.add_argument("-d", "--debug", action="store_true", help="Ativa modo debug")
    parser.add_argument("-v", "--verbose", action="store_true", help="Ativa modo verbose")
    return parser.parse_args()


CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")
cancelar_evento = threading.Event()

ETIQUETAS = {
    "coletar": "Coletar e Extrair Dados",
    "especies_controle": "Espécies de Controle",
    "situacao_emissor": "Situação do Emissor",
    "setor_atividade": "Setor de Atividade",
    "categoria_documento": "Categoria de Documento",
    "tipo_parecer": "Tipo de Parecer",
    "escala_monetaria": "Escala Monetária",
    "ordem_exercicio": "Ordem de Exercício",
    "moeda": "Moeda",
    "tipo_relatorio_auditor": "Tipo Relatório Auditor",
    "tipo_relatorio_especial": "Tipo Relatório Especial",
    "assunto_prensa": "Assunto Prensa",
    "especie_documento_eventual": "Espécie Documento Eventual",
    "tipo_evento": "Tipo Evento",
    "tipo_apresentacao_evento": "Tipo Apresentação Evento",
    "empresas": "Empresas",
    "ipe": "Periódicos Eventuais",
    "fre": "Formulários de Referência",
    "parecer_demo": "Parecer - Demonst. Financeiros",
    "parecer_trim": "Parecer - Inf. Trimestrais",
    "num_acoes": "Número de Ações",
    "dfp": "Demonstrativos Financeiros",
    "itr": "Informações Trimestrais",
}


def executar_script_inicial():
    if os.path.exists(CAMINHO_BANCO):
        print("\u26a0\ufe0f Banco de dados já existe. Pulando execução do script.")
        return
    try:
        subprocess.run(
            [sys.executable, "sqlite-projeto/script-automatizar-sqlite.py"], check=True
        )
        print("\u2705 Script de automação executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar o script:\n{str(e)}")
        sys.exit(1)


def run_processos_selecionados(vars):
    print("🔄 Executando...\n")
    mensagens = []
    executar_script_inicial()

    tempo_inicio = time.time()

    if vars["coletar"].get():
        coletor = Coletor(nivel=nivel_log)
        coletor.collect_data()
        mensagens.append("Coleta e extração concluídas.")

    def executar_etapa(etiqueta, caminho, banco_cls, process_func, insert_func, usa_banco=False, *args_extra):
        try:
            banco = banco_cls(db_path=CAMINHO_BANCO)
            banco.conectar()
            conn = banco.connection
            conn.execute("BEGIN")

            if usa_banco:
                dados = process_func(caminho, banco, *args_extra)
            else:
                dados = process_func(caminho, *args_extra) if args_extra else process_func(caminho)

            sucesso = falha = 0
            for dado in dados:
                if cancelar_evento.is_set():
                    conn.rollback()
                    banco.desconectar()
                    mensagens.append(f"{etiqueta} abortado.")
                    return
                try:
                    getattr(banco, insert_func)(dado)
                    sucesso += 1
                except Exception:
                    falha += 1
            conn.commit()
            banco.desconectar()
            mensagens.append(f"{etiqueta}: {sucesso} inseridos, {falha} com erro.")
        except Exception as e:
            mensagens.append(f"Erro fatal em {etiqueta}: {str(e)}")

    # Auxiliares simples
    if vars["especies_controle"].get():
        executar_etapa("Espécies de Controle", "data_extraido/FCA/sucesso", BancoEspecie_controle, process_especie_controle, "inserir_ou_ignorar_especie_controle")

    if vars["situacao_emissor"].get():
        executar_etapa("Situação do Emissor", "data_extraido/FCA/sucesso", BancoSituacao_emissor, process_situacao_emissor, "inserir_ou_ignorar_situacao_emissor")

    if vars["setor_atividade"].get():
        executar_etapa("Setor de Atividade", "data_extraido/FCA/sucesso", BancoSetor_atividade, process_setor_atividade, "inserir_ou_ignorar_setor_atividade")

    # Auxiliares extras
    if vars["categoria_documento"].get(): mensagens.append(executar_categoria_documento())# noqa: E701
    if vars["tipo_parecer"].get(): mensagens.append(executar_tipo_parecer())# noqa: E701
    if vars["escala_monetaria"].get(): mensagens.append(executar_escala_monetaria())# noqa: E701
    if vars["ordem_exercicio"].get(): mensagens.append(executar_ordem_exercicio())# noqa: E701
    if vars["moeda"].get(): mensagens.append(executar_moeda())# noqa: E701
    if vars["tipo_relatorio_auditor"].get(): mensagens.append(executar_tipo_relatorio_auditor())# noqa: E701
    if vars["tipo_relatorio_especial"].get(): mensagens.append(executar_tipo_relatorio_especial())# noqa: E701
    if vars["assunto_prensa"].get(): mensagens.append(executar_assunto_prensa())# noqa: E701
    if vars["especie_documento_eventual"].get(): mensagens.append(executar_especie_documento_eventual())# noqa: E701
    if vars["tipo_evento"].get(): mensagens.append(executar_tipo_evento())# noqa: E701
    if vars["tipo_apresentacao_evento"].get(): mensagens.append(executar_tipo_apresentacao_evento())  # noqa: E701

    # Tabelas principais
    if vars["empresas"].get():
        executar_etapa("Empresas", "data_extraido/FCA/sucesso", BancoEmpresas, process_empresas, "inserir_ou_atualizar_empresa", True)

    if vars["ipe"].get():
        executar_etapa("Periódicos Eventuais", "data_extraido/IPE/sucesso", BancoIPE, process_ipe, "inserir_periodicos_eventuais", True)

    if vars["fre"].get():
        executar_etapa("Formulários de Referência", "data_extraido/FRE/sucesso", BancoFRE, process_fre, "inserir_formulario_referencia", True)

    if vars["parecer_demo"].get():
        executar_etapa("Parecer - Demonstrativos", "data_extraido/DFP/sucesso", BancoParecerDemo, process_parecer_demo, "inserir_parecer_demonstrativo", True)

    if vars["parecer_trim"].get():
        executar_etapa("Parecer - Trimestral", "data_extraido/ITR/sucesso", BancoParecerTrim, process_parecer_trim, "inserir_parecer_trimestral", True)

    if vars["num_acoes"].get():
        try:
            banco = BancoNumAcoes(db_path=CAMINHO_BANCO)
            banco.conectar()
            conn = banco.connection
            conn.execute("BEGIN")
            dados = process_num_acoes("data_extraido/DFP/sucesso", "DFP") + process_num_acoes("data_extraido/ITR/sucesso", "ITR")
            sucesso = falha = 0
            for d in dados:
                if cancelar_evento.is_set():
                    conn.rollback()
                    banco.desconectar()
                    mensagens.append("Número de Ações abortado.")
                    return
                try:
                    banco.inserir_numeros_acoes(d)
                    sucesso += 1
                except:  # noqa: E722
                    falha += 1
            conn.commit()
            banco.desconectar()
            mensagens.append(f"Número de Ações: {sucesso} inseridos, {falha} com erro.")
        except Exception as e:
            mensagens.append(f"Erro fatal em Número de Ações: {str(e)}")

    if vars["dfp"].get():
        executar_etapa("Demonstrativos Financeiros", "data_extraido/DFP/sucesso", BancoDemostrativo, process_dfp, "inserir_ou_atualizar_demonstrativo", True)

    if vars["itr"].get():
        executar_etapa("Informações Trimestrais", "data_extraido/ITR/sucesso", BancoInformacaoTri, process_itr, "inserir_ou_atualizar_informacao_tri", True)

    print("\n✅ Execução finalizada.\n")
    tempo_fim = time.time()
    duracao = tempo_fim - tempo_inicio
    duracao_formatada = time.strftime("%H:%M:%S", time.gmtime(duracao))

    resumo_texto = "\n\n".join(mensagens)
    print("===== RESUMO DA EXECUÇÃO =====")
    print(resumo_texto)
    print(f"\n🕒 Tempo total de execução: {duracao_formatada}")

    with open("resumo_execucao.log", "w", encoding="utf-8") as f:
        f.write(resumo_texto)
        f.write(f"\n\n🕒 Tempo total de execução: {duracao_formatada}")


if __name__ == "__main__":
    args = configurar_argumentos()
    nivel_log = logging.DEBUG if args.debug else logging.INFO if args.verbose else logging.WARNING
    logger = configurar_logger(nivel=nivel_log)

    try:
        vars = {
            chave: type("BoolVar", (), {"get": lambda self=True: True})()
            for chave in ETIQUETAS.keys()
        }
        cancelar_evento.clear()
        run_processos_selecionados(vars)
    except KeyboardInterrupt:
        cancelar_evento.set()
        print("⏹ Execução cancelada pelo usuário.")