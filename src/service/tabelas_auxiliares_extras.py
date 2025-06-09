import os

from service.categoria_documento_service import process_csv_files as process_categoria_documento
from repository.categoria_documento_repository import ConexaoBanco as BancoCategoria_documento

from service.tipo_parecer_service import process_tipo_parecer
from repository.tipo_parecer_repository import ConexaoBanco as BancoTipo_parecer

from service.escala_monetaria_service import process_csv_files as process_escala_monetaria
from repository.escala_monetaria_repository import ConexaoBanco as BancoEscala_monetaria

from service.ordem_exercicio_service import process_csv_files as process_ordem_exercicio
from repository.ordem_exercicio_repository import ConexaoBanco as BancoOrdem_exercicio

from service.moeda_service import process_csv_files as process_moeda
from repository.moeda_repository import ConexaoBanco as BancoMoeda

from service.tipo_relatorio_auditor_service import process_csv_files as process_tipo_relatorio_auditor
from repository.tipo_relatorio_auditor_repository import ConexaoBanco as BancoTipo_relatorio_auditor

from service.tipo_relatorio_especial_service import process_csv_files as process_tipo_relatorio_especial
from repository.tipo_relatorio_especial_repository import ConexaoBanco as BancoTipo_relatorio_especial

from service.assunto_prensa_service import process_csv_files as process_assunto_prensa
from repository.assunto_prensa_repository import ConexaoBanco as BancoAssunto_prensa

from service.especie_documento_eventual_service import process_csv_files as process_especie_documento_eventual
from repository.especie_documento_eventual_repository import ConexaoBanco as BancoEspecie_documento_eventual

from service.tipo_evento_service import process_csv_files as process_tipo_evento
from repository.tipo_evento_repository import ConexaoBanco as BancoTipo_evento

from service.tipo_apresentacao_evento_service import process_csv_files as process_tipo_apresentacao_evento
from repository.tipo_apresentacao_evento_repository import ConexaoBanco as BancoTipo_apresentacao_evento

CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")


def _template_execucao_simples(etiqueta, base_path, process_func, banco_cls, insert_func, passar_conexao=False):
    repo = banco_cls(db_path=CAMINHO_BANCO)
    repo.conectar()
    conn = repo.connection
    try:
        conn.execute("BEGIN")
        sucesso = falha = 0
        erros = []

        # Chama o process_func com ou sem o argumento 'conexao'
        if passar_conexao:
            dados = process_func(base_path, conexao=repo)
        else:
            dados = process_func(base_path)

        for d in dados:
            try:
                getattr(repo, insert_func)(d)
                sucesso += 1
            except Exception as e:
                falha += 1
                erros.append(str(e))

        conn.commit()

        if erros:
            with open(f"logs/erros_{etiqueta}.log", "w", encoding="utf-8") as f:
                f.write("\n".join(erros))

        return f"{etiqueta}: {sucesso} inseridos, {falha} com erro."

    except Exception as e:
        conn.rollback()
        return f"Erro fatal ao processar {etiqueta}: {e}"
    finally:
        repo.desconectar()



# FUNÇÕES EXISTENTES
def executar_categoria_documento():
    entradas = [
        {"base_path": "data_extraido/FCA/sucesso", "regex_arquivo": r"^fca_cia_aberta_geral.*\.csv$", "campo": "Categoria_Registro_CVM"},
        {"base_path": "data_extraido/FRE/sucesso", "regex_arquivo": r"^fre_cia_aberta_\d{4}\.csv$", "campo": "CATEG_DOC"},
        {"base_path": "data_extraido/IPE/sucesso", "regex_arquivo": r"^ipe_cia_aberta.*\.csv$", "campo": "Categoria"},
    ]
    repo = BancoCategoria_documento(db_path=CAMINHO_BANCO)
    repo.conectar()
    conn = repo.connection
    try:
        conn.execute("BEGIN")
        sucesso = falha = 0
        erros = []
        for entrada in entradas:
            dados = process_categoria_documento(entrada["base_path"], entrada["regex_arquivo"], entrada["campo"])
            for dado in dados:
                try:
                    repo.inserir_ou_ignorar_categoria_documento(dado)
                    sucesso += 1
                except Exception as e:
                    falha += 1
                    erros.append(str(e))
        conn.commit()
        if erros:
            with open("logs/erros_categoria_documento.log", "w", encoding="utf-8") as f:
                f.write("\n".join(erros))
        return f"Categoria Documento: {sucesso} inseridos, {falha} com erro."
    except Exception as e:
        conn.rollback()
        return f"Erro fatal ao processar Categoria Documento: {e}"
    finally:
        repo.desconectar()


def executar_tipo_parecer():
    entradas = [
        {"base_path": "data_extraido/DFP/sucesso", "regex_arquivo": r"^dfp_cia_aberta_parecer.*\.csv$", "campo": "TP_PARECER_DECL"},
        {"base_path": "data_extraido/ITR/sucesso", "regex_arquivo": r"^itr_cia_aberta_parecer.*\.csv$", "campo": "TP_PARECER_DECL"},
    ]
    repo = BancoTipo_parecer(db_path=CAMINHO_BANCO)
    repo.conectar()
    conn = repo.connection
    try:
        conn.execute("BEGIN")
        sucesso = falha = 0
        erros = []
        for entrada in entradas:
            dados = process_tipo_parecer(entrada["base_path"], entrada["regex_arquivo"], entrada["campo"])
            for dado in dados:
                try:
                    repo.inserir_ou_ignorar_tipo_parecer(dado)
                    sucesso += 1
                except Exception as e:
                    falha += 1
                    erros.append(str(e))
        conn.commit()
        if erros:
            with open("logs/erros_tipo_parecer.log", "w", encoding="utf-8") as f:
                f.write("\n".join(erros))
        return f"Tipo Parecer: {sucesso} inseridos, {falha} com erro."
    except Exception as e:
        conn.rollback()
        return f"Erro fatal ao processar Tipo Parecer: {e}"
    finally:
        repo.desconectar()


def executar_escala_monetaria():
    return _template_execucao_simples(
        "escala_monetaria",
        "data_extraido/DFP/sucesso",
        process_escala_monetaria,
        BancoEscala_monetaria,
        "inserir_ou_ignorar_escala_monetaria",
        passar_conexao=True
    )


def executar_ordem_exercicio():
    return _template_execucao_simples(
        "ordem_exercicio",
        "data_extraido/DFP/sucesso",
        process_ordem_exercicio,
        BancoOrdem_exercicio,
        "inserir_ou_ignorar_ordem_exercicio",
        passar_conexao=True
    )


def executar_moeda():
    return _template_execucao_simples(
        "moeda",
        "data_extraido/DFP/sucesso",
        process_moeda,
        BancoMoeda,
        "inserir_ou_ignorar_moeda",
        passar_conexao=True
    )


def executar_tipo_relatorio_auditor():
    return _template_execucao_simples("tipo_relatorio_auditor", "data_extraido/DFP/sucesso", process_tipo_relatorio_auditor, BancoTipo_relatorio_auditor, "inserir_ou_ignorar_tipo_relatorio_auditor")


def executar_tipo_relatorio_especial():
    return _template_execucao_simples("tipo_relatorio_especial", "data_extraido/ITR/sucesso", process_tipo_relatorio_especial, BancoTipo_relatorio_especial, "inserir_ou_ignorar_tipo_relatorio_especial")


def executar_assunto_prensa():
    return _template_execucao_simples("assunto_prensa", "data_extraido/IPE/sucesso", process_assunto_prensa, BancoAssunto_prensa, "inserir_ou_ignorar_assunto_prensa")


def executar_especie_documento_eventual():
    return _template_execucao_simples("especie_documento_eventual", "data_extraido/IPE/sucesso", process_especie_documento_eventual, BancoEspecie_documento_eventual, "inserir_ou_ignorar_especie_documento_eventual")


def executar_tipo_evento():
    return _template_execucao_simples("tipo_evento", "data_extraido/IPE/sucesso", process_tipo_evento, BancoTipo_evento, "inserir_ou_ignorar_tipo_evento")


def executar_tipo_apresentacao_evento():
    return _template_execucao_simples("tipo_apresentacao_evento", "data_extraido/IPE/sucesso", process_tipo_apresentacao_evento, BancoTipo_apresentacao_evento, "inserir_ou_ignorar_tipo_apresentacao_evento")
