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

CAMINHO_BANCO = "sqlite-projeto/cvm-dados.db"

def executar_categoria_documento():
    entradas = [
        {"base_path": "data_extraido/FCA/sucesso", "regex_arquivo": r"^fca_cia_aberta_geral.*\.csv$", "campo": "Categoria_Registro_CVM"},
        {"base_path": "data_extraido/FRE/sucesso", "regex_arquivo": r"^fre_cia_aberta_\d{4}\.csv$", "campo": "CATEG_DOC"},
        {"base_path": "data_extraido/IPE/sucesso", "regex_arquivo": r"^ipe_cia_aberta.*\.csv$", "campo": "Categoria"},
    ]
    repo = BancoCategoria_documento(db_path=CAMINHO_BANCO)
    repo.conectar()
    for entrada in entradas:
        dados = process_categoria_documento(entrada["base_path"], entrada["regex_arquivo"], entrada["campo"])
        for dado in dados:
            repo.inserir_ou_ignorar_categoria_documento(dado)
    repo.desconectar()


def executar_tipo_parecer():
    entradas = [
        {"base_path": "data_extraido/DFP/sucesso", "regex_arquivo": r"^dfp_cia_aberta_parecer.*\.csv$", "campo": "TP_PARECER_DECL"},
        {"base_path": "data_extraido/ITR/sucesso", "regex_arquivo": r"^itr_cia_aberta_parecer.*\.csv$", "campo": "TP_PARECER_DECL"},
    ]
    repo = BancoTipo_parecer(db_path=CAMINHO_BANCO)
    repo.conectar()
    for entrada in entradas:
        dados = process_tipo_parecer(entrada["base_path"], entrada["regex_arquivo"], entrada["campo"])
        for dado in dados:
            repo.inserir_ou_ignorar_tipo_parecer(dado)
    repo.desconectar()


def executar_escala_monetaria():
    entradas = [{"base_path": "data_extraido/DFP/sucesso"}, {"base_path": "data_extraido/ITR/sucesso"}]
    repo = BancoEscala_monetaria(db_path=CAMINHO_BANCO)
    repo.conectar()
    for entrada in entradas:
        valores = process_escala_monetaria(entrada["base_path"], conexao=repo)
        for valor in valores:
            repo.inserir_ou_ignorar_escala_monetaria(valor)
    repo.desconectar()


def executar_ordem_exercicio():
    entradas = [{"base_path": "data_extraido/DFP/sucesso"}, {"base_path": "data_extraido/ITR/sucesso"}]
    repo = BancoOrdem_exercicio(db_path=CAMINHO_BANCO)
    repo.conectar()
    for entrada in entradas:
        valores = process_ordem_exercicio(entrada["base_path"], conexao=repo)
        for valor in valores:
            repo.inserir_ou_ignorar_ordem_exercicio(valor)
    repo.desconectar()


def executar_moeda():
    entradas = [{"base_path": "data_extraido/DFP/sucesso"}, {"base_path": "data_extraido/ITR/sucesso"}]
    repo = BancoMoeda(db_path=CAMINHO_BANCO)
    repo.conectar()
    for entrada in entradas:
        valores = process_moeda(entrada["base_path"], conexao=repo)
        for valor in valores:
            repo.inserir_ou_ignorar_moeda(valor)
    repo.desconectar()
