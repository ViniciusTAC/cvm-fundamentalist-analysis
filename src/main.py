# # Imports e configuração
# import os
# import sys
# import subprocess
# import threading
# import argparse
# import logging

# from utils.logger import configurar_logger
# from collectors.coletor import Coletor

# # Services e Repositories
# from service.empresas_service import process_csv_files as process_empresas
# from repository.empresas_repository import ConexaoBanco as BancoEmpresas

# from service.periodicos_eventuais_service import process_csv_files as process_ipe
# from repository.periodicos_eventuais_repository import ConexaoBanco as BancoIPE

# from service.formulario_referencia_service import process_csv_files as process_fre
# from repository.formulario_referencia_repository import ConexaoBanco as BancoFRE

# from service.parecer_demonstrativo_service import (
#     process_csv_files as process_parecer_demo,
# )
# from repository.parecer_demonstrativo_repository import ConexaoBanco as BancoParecerDemo

# from service.parecer_trimestral_service import process_csv_files as process_parecer_trim
# from repository.parecer_trimestral_repository import ConexaoBanco as BancoParecerTrim

# from service.numeros_acoes_service import process_csv_files as process_num_acoes
# from repository.numeros_acoes_repository import ConexaoBanco as BancoNumAcoes

# from service.demostrativo_financeiro_service import process_dfp_files as process_dfp
# from repository.demostrativo_financeiro_repository import (
#     ConexaoBanco as BancoDemostrativo,
# )

# from service.informacao_trimestral_service import process_dfp_files as process_itr
# from repository.informacao_trimestral_repository import (
#     ConexaoBanco as BancoInformacaoTri,
# )

# from service.tabelas_auxiliares_extras import (
#     executar_categoria_documento,
#     executar_tipo_parecer,
#     executar_escala_monetaria,
#     executar_ordem_exercicio,
#     executar_moeda,
# )

# from service.especie_controle_service import (
#     process_csv_files as process_especie_controle,
# )
# from repository.especie_controle_repository import ConexaoBanco as BancoEspecie_controle

# from service.situacao_emissor_service import (
#     process_csv_files as process_situacao_emissor,
# )
# from repository.situacao_emissor_repository import ConexaoBanco as BancoSituacao_emissor

# from service.setor_atividade_service import process_csv_files as process_setor_atividade
# from repository.setor_atividade_repository import ConexaoBanco as BancoSetor_atividade


# def configurar_argumentos():
#     parser = argparse.ArgumentParser(description="Processador CVM")
#     parser.add_argument("-d", "--debug", action="store_true", help="Ativa modo debug")
#     parser.add_argument(
#         "-v", "--verbose", action="store_true", help="Ativa modo verbose"
#     )
#     return parser.parse_args()


# CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")
# cancelar_evento = threading.Event()

# ETIQUETAS = {
#     "coletar": "Coletar e Extrair Dados",
#     "especies_controle": "Espécies de Controle",
#     "situacao_emissor": "Situação do Emissor",
#     "setor_atividade": "Setor de Atividade",
#     "categoria_documento": "Categoria de Documento",
#     "tipo_parecer": "Tipo de Parecer",
#     "escala_monetaria": "Escala Monetária",
#     "ordem_exercicio": "Ordem de Exercício",
#     "moeda": "Moeda",
#     "empresas": "Empresas",
#     "ipe": "Periódicos Eventuais",
#     "fre": "Formulários de Referência",
#     "parecer_demo": "Parecer - Demonst. Financeiros",
#     "parecer_trim": "Parecer - Inf. Trimestrais",
#     "num_acoes": "Número de Ações",
#     "dfp": "Demonstrativos Financeiros",
#     "itr": "Informações Trimestrais",
# }


# def executar_script_inicial():
#     if os.path.exists(CAMINHO_BANCO):
#         print("⚠️ Banco de dados já existe. Pulando execução do script.")
#         return
#     try:
#         subprocess.run(
#             [sys.executable, "sqlite-projeto/script-automatizar-sqlite.py"], check=True
#         )
#         print("✅ Script de automação executado com sucesso.")
#     except subprocess.CalledProcessError as e:
#         print(f"❌ Erro ao executar o script:\n{str(e)}")
#         sys.exit(1)


# def run_processos_selecionados(vars):
#     print("🔄 Executando...\n")
#     mensagens = []
#     executar_script_inicial()

#     # if vars["coletar"].get():
#     #     coletor = Coletor(nivel=nivel_log)
#     #     coletor.collect_data()
#     #     mensagens.append("Coleta e extração concluídas.")

#     def executar_etapa(
#         etiqueta, caminho, banco_cls, process_func, insert_func, *args_extra
#     ):
#         try:
#             banco = banco_cls(db_path=CAMINHO_BANCO)
#             banco.conectar()
#             conn = banco.connection
#             conn.execute("BEGIN")
#             dados = (
#                 process_func(caminho, *args_extra)
#                 if args_extra
#                 else process_func(caminho)
#             )
#             sucesso = falha = 0
#             for dado in dados:
#                 if cancelar_evento.is_set():
#                     conn.rollback()
#                     banco.desconectar()
#                     mensagens.append(f"{etiqueta} abortado.")
#                     return
#                 try:
#                     getattr(banco, insert_func)(dado)
#                     sucesso += 1
#                 except Exception as e:
#                     falha += 1
#             conn.commit()
#             banco.desconectar()
#             mensagens.append(f"{etiqueta}: {sucesso} inseridos, {falha} com erro.")
#         except Exception as e:
#             mensagens.append(f"Erro fatal em {etiqueta}: {str(e)}")

#     # Auxiliares
#     if vars["especies_controle"].get():
#         executar_etapa(
#             "Espécies de Controle",
#             "data_extraido/FCA/sucesso",
#             BancoEspecie_controle,
#             process_especie_controle,
#             "inserir_ou_ignorar_especie_controle",
#         )

#     if vars["situacao_emissor"].get():
#         executar_etapa(
#             "Situação do Emissor",
#             "data_extraido/FCA/sucesso",
#             BancoSituacao_emissor,
#             process_situacao_emissor,
#             "inserir_ou_ignorar_situacao_emissor",
#         )

#     if vars["setor_atividade"].get():
#         executar_etapa(
#             "Setor de Atividade",
#             "data_extraido/FCA/sucesso",
#             BancoSetor_atividade,
#             process_setor_atividade,
#             "inserir_ou_ignorar_setor_atividade",
#         )

#     # Extras (sem necessidade de transação)
#     if vars["categoria_documento"].get():
#         executar_categoria_documento()
#         mensagens.append("Categoria de Documento processada.")
#     if vars["tipo_parecer"].get():
#         executar_tipo_parecer()
#         mensagens.append("Tipo de Parecer processado.")
#     if vars["escala_monetaria"].get():
#         executar_escala_monetaria()
#         mensagens.append("Escala Monetária processada.")
#     if vars["ordem_exercicio"].get():
#         executar_ordem_exercicio()
#         mensagens.append("Ordem de Exercício processada.")
#     if vars["moeda"].get():
#         executar_moeda()
#         mensagens.append("Moeda processada.")

#     # Principais
#     if vars["empresas"].get():
#         executar_etapa(
#             "Empresas",
#             "data_extraido/FCA/sucesso",
#             BancoEmpresas,
#             process_empresas,
#             "inserir_ou_atualizar_empresa",
#             CAMINHO_BANCO,
#         )

#     if vars["ipe"].get():
#         executar_etapa(
#             "Periódicos Eventuais",
#             "data_extraido/IPE/sucesso",
#             BancoIPE,
#             process_ipe,
#             "inserir_periodicos_eventuais",
#             CAMINHO_BANCO,
#         )

#     if vars["fre"].get():
#         executar_etapa(
#             "Formulários de Referência",
#             "data_extraido/FRE/sucesso",
#             BancoFRE,
#             process_fre,
#             "inserir_formulario_referencia",
#             CAMINHO_BANCO,
#         )

#     if vars["parecer_demo"].get():
#         executar_etapa(
#             "Parecer - Demonstrativos",
#             "data_extraido/DFP/sucesso",
#             BancoParecerDemo,
#             process_parecer_demo,
#             "inserir_parecer_demonstrativo",
#             CAMINHO_BANCO,
#         )

#     if vars["parecer_trim"].get():
#         executar_etapa(
#             "Parecer - Trimestral",
#             "data_extraido/ITR/sucesso",
#             BancoParecerTrim,
#             process_parecer_trim,
#             "inserir_parecer_trimestral",
#             CAMINHO_BANCO,
#         )

#     if vars["num_acoes"].get():
#         try:
#             banco = BancoNumAcoes(db_path=CAMINHO_BANCO)
#             banco.conectar()
#             conn = banco.connection
#             conn.execute("BEGIN")
#             dados = process_num_acoes(
#                 "data_extraido/DFP/sucesso", "DFP"
#             ) + process_num_acoes("data_extraido/ITR/sucesso", "ITR")
#             sucesso = falha = 0
#             for d in dados:
#                 if cancelar_evento.is_set():
#                     conn.rollback()
#                     banco.desconectar()
#                     mensagens.append("Número de Ações abortado.")
#                     return
#                 try:
#                     banco.inserir_numeros_acoes(d)
#                     sucesso += 1
#                 except:
#                     falha += 1
#             conn.commit()
#             banco.desconectar()
#             mensagens.append(f"Número de Ações: {sucesso} inseridos, {falha} com erro.")
#         except Exception as e:
#             mensagens.append(f"Erro fatal em Número de Ações: {str(e)}")

#     if vars["dfp"].get():
#         try:
#             banco = BancoDemostrativo(db_path=CAMINHO_BANCO)
#             banco.conectar()
#             conn = banco.connection
#             conn.execute("BEGIN")
#             dados = process_dfp(
#                 "data_extraido/DFP/sucesso", banco, db_path=CAMINHO_BANCO
#             )
#             sucesso = falha = 0
#             for d in dados:
#                 if cancelar_evento.is_set():
#                     conn.rollback()
#                     banco.desconectar()
#                     mensagens.append("Demonstrativos Financeiros abortado.")
#                     return
#                 try:
#                     banco.inserir_ou_atualizar_demonstrativo(d)
#                     sucesso += 1
#                 except Exception as e:
#                     falha += 1
#             conn.commit()
#             banco.desconectar()
#             mensagens.append(
#                 f"Demonstrativos Financeiros: {sucesso} inseridos, {falha} com erro."
#             )
#         except Exception as e:
#             mensagens.append(f"Erro fatal em Demonstrativos Financeiros: {str(e)}")

#     if vars["itr"].get():
#         try:
#             banco = BancoInformacaoTri(db_path=CAMINHO_BANCO)
#             banco.conectar()
#             conn = banco.connection
#             conn.execute("BEGIN")
#             dados = process_itr(
#                 "data_extraido/ITR/sucesso", banco, db_path=CAMINHO_BANCO
#             )
#             sucesso = falha = 0
#             for d in dados:
#                 if cancelar_evento.is_set():
#                     conn.rollback()
#                     banco.desconectar()
#                     mensagens.append("Informações Trimestrais abortado.")
#                     return
#                 try:
#                     banco.inserir_ou_atualizar_informacao_tri(d)
#                     sucesso += 1
#                 except Exception as e:
#                     falha += 1
#             conn.commit()
#             banco.desconectar()
#             mensagens.append(
#                 f"Informações Trimestrais: {sucesso} inseridos, {falha} com erro."
#             )
#         except Exception as e:
#             mensagens.append(f"Erro fatal em Informações Trimestrais: {str(e)}")

#     # Fim
#     print("\n✅ Execução finalizada.\n")
#     resumo_texto = "\n\n".join(mensagens)
#     print("===== RESUMO DA EXECUÇÃO =====")
#     print(resumo_texto)
#     with open("resumo_execucao.log", "w", encoding="utf-8") as f:
#         f.write(resumo_texto)


# if __name__ == "__main__":
#     args = configurar_argumentos()
#     nivel_log = (
#         logging.DEBUG
#         if args.debug
#         else logging.INFO if args.verbose else logging.WARNING
#     )
#     logger = configurar_logger(nivel=nivel_log)

#     try:
#         vars = {
#             chave: type("BoolVar", (), {"get": lambda self=True: True})()
#             for chave in ETIQUETAS.keys()
#         }
#         cancelar_evento.clear()
#         run_processos_selecionados(vars)
#     except KeyboardInterrupt:
#         cancelar_evento.set()
#         print("⏹ Execução cancelada pelo usuário.")
import os
import sys
import subprocess
import threading
import argparse
import logging

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

from service.informacao_trimestral_service import process_dfp_files as process_itr
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
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Ativa modo verbose"
    )
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
        print("⚠️ Banco de dados já existe. Pulando execução do script.")
        return
    try:
        subprocess.run(
            [sys.executable, "sqlite-projeto/script-automatizar-sqlite.py"], check=True
        )
        print("✅ Script de automação executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar o script:\n{str(e)}")
        sys.exit(1)


def run_processos_selecionados(vars):
    print("🔄 Executando...\n")
    mensagens = []
    executar_script_inicial()

    # if vars["coletar"].get():
    #     coletor = Coletor(nivel=nivel_log)
    #     coletor.collect_data()
    #     mensagens.append("Coleta e extração concluídas.")

    def executar_etapa(
        etiqueta,
        caminho,
        banco_cls,
        process_func,
        insert_func,
        usa_banco=False,
        *args_extra,
    ):
        try:
            banco = banco_cls(db_path=CAMINHO_BANCO)
            banco.conectar()
            conn = banco.connection
            conn.execute("BEGIN")

            if usa_banco:
                dados = process_func(caminho, banco, *args_extra)
            else:
                dados = (
                    process_func(caminho, *args_extra)
                    if args_extra
                    else process_func(caminho)
                )

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

    # Auxiliares simples com transação
    if vars["especies_controle"].get():
        executar_etapa(
            "Espécies de Controle",
            "data_extraido/FCA/sucesso",
            BancoEspecie_controle,
            process_especie_controle,
            "inserir_ou_ignorar_especie_controle",
        )

    if vars["situacao_emissor"].get():
        executar_etapa(
            "Situação do Emissor",
            "data_extraido/FCA/sucesso",
            BancoSituacao_emissor,
            process_situacao_emissor,
            "inserir_ou_ignorar_situacao_emissor",
        )

    if vars["setor_atividade"].get():
        executar_etapa(
            "Setor de Atividade",
            "data_extraido/FCA/sucesso",
            BancoSetor_atividade,
            process_setor_atividade,
            "inserir_ou_ignorar_setor_atividade",
        )

    # Auxiliares extras com retorno
    if vars["categoria_documento"].get():
        mensagens.append(executar_categoria_documento())

    if vars["tipo_parecer"].get():
        mensagens.append(executar_tipo_parecer())

    if vars["escala_monetaria"].get():
        mensagens.append(executar_escala_monetaria())

    if vars["ordem_exercicio"].get():
        mensagens.append(executar_ordem_exercicio())

    if vars["moeda"].get():
        mensagens.append(executar_moeda())

        # Tabelas principais
    if vars["empresas"].get():
        executar_etapa(
            "Empresas",
            "data_extraido/FCA/sucesso",
            BancoEmpresas,
            process_empresas,
            "inserir_ou_atualizar_empresa",
            True,  # <- usa somente a conexão
        )

    if vars["ipe"].get():
        executar_etapa(
            "Periódicos Eventuais",
            "data_extraido/IPE/sucesso",
            BancoIPE,
            process_ipe,
            "inserir_periodicos_eventuais",
            True,
        )

    if vars["fre"].get():
        executar_etapa(
            "Formulários de Referência",
            "data_extraido/FRE/sucesso",
            BancoFRE,
            process_fre,
            "inserir_formulario_referencia",
            True,
        )

    if vars["parecer_demo"].get():
        executar_etapa(
            "Parecer - Demonstrativos",
            "data_extraido/DFP/sucesso",
            BancoParecerDemo,
            process_parecer_demo,
            "inserir_parecer_demonstrativo",
            True,
        )

    if vars["parecer_trim"].get():
        executar_etapa(
            "Parecer - Trimestral",
            "data_extraido/ITR/sucesso",
            BancoParecerTrim,
            process_parecer_trim,
            "inserir_parecer_trimestral",
            True,
        )

    if vars["num_acoes"].get():
        try:
            banco = BancoNumAcoes(db_path=CAMINHO_BANCO)
            banco.conectar()
            conn = banco.connection
            conn.execute("BEGIN")
            dados = process_num_acoes(
                "data_extraido/DFP/sucesso", "DFP"
            ) + process_num_acoes("data_extraido/ITR/sucesso", "ITR")
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
                except:
                    falha += 1
            conn.commit()
            banco.desconectar()
            mensagens.append(f"Número de Ações: {sucesso} inseridos, {falha} com erro.")
        except Exception as e:
            mensagens.append(f"Erro fatal em Número de Ações: {str(e)}")

    if vars["dfp"].get():
        executar_etapa(
            "Demonstrativos Financeiros",
            "data_extraido/DFP/sucesso",
            BancoDemostrativo,
            process_dfp,
            "inserir_ou_atualizar_demonstrativo",
            True,
            CAMINHO_BANCO,
        )

    if vars["itr"].get():
        executar_etapa(
            "Informações Trimestrais",
            "data_extraido/ITR/sucesso",
            BancoInformacaoTri,
            process_itr,
            "inserir_ou_atualizar_informacao_tri",
            True,
            CAMINHO_BANCO,
        )
    print("\n✅ Execução finalizada.\n")
    resumo_texto = "\n\n".join(mensagens)
    print("===== RESUMO DA EXECUÇÃO =====")
    print(resumo_texto)
    with open("resumo_execucao.log", "w", encoding="utf-8") as f:
        f.write(resumo_texto)


if __name__ == "__main__":
    args = configurar_argumentos()
    nivel_log = (
        logging.DEBUG
        if args.debug
        else logging.INFO if args.verbose else logging.WARNING
    )
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
