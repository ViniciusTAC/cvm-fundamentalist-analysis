import sqlite3
import os
from datetime import datetime
from zoneinfo import ZoneInfo
import logging
from utils.logger import escrever_linha_em_branco, escrever_linha_separador


class ConexaoBanco:
    """Classe para gerenciar a conexão com o banco de dados SQLite."""

    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.log_sucesso, self.log_erro = self._setup_logger()

    def _setup_logger(self, log_dir="logs/logs_insercao"):
        hoje = datetime.now().strftime("%Y-%m-%d")
        log_sucesso_dir = os.path.join(log_dir, hoje)
        log_erro_dir = os.path.join(log_dir, hoje)

        os.makedirs(log_sucesso_dir, exist_ok=True)
        os.makedirs(log_erro_dir, exist_ok=True)

        sucesso_logger = logging.getLogger("sucesso")
        sucesso_logger.setLevel(logging.INFO)
        sucesso_handler = logging.FileHandler(
            os.path.join(log_sucesso_dir, "sucesso.log"), encoding="utf-8"
        )
        sucesso_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        if not sucesso_logger.handlers:
            sucesso_logger.addHandler(sucesso_handler)

        erro_logger = logging.getLogger("erro")
        erro_logger.setLevel(logging.WARNING)
        erro_handler = logging.FileHandler(
            os.path.join(log_erro_dir, "erro.log"), encoding="utf-8"
        )
        erro_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        if not erro_logger.handlers:
            erro_logger.addHandler(erro_handler)

        return sucesso_logger, erro_logger

    def conectar(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("Conexão com o banco de dados SQLite estabelecida com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")

    def inserir_formulario_referencia(self, formulario_referencia):
        try:
            cursor = self.connection.cursor()
            query = """
                            INSERT INTO formulario_referencia (
                                cnpj_companhia,
                                categoria_doc,
                                denominacao_companhia,
                                id_doc,
                                link_doc,
                                versao,
                                data_recebimento_doc,
                                data_referencia_doc,
                                data_doc,
                                mes_doc,
                                ano_doc
                            ) VALUES (
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?
                            )
                    """
            # Construir valores garantindo que não haja extras e substituindo 'nan' por None
            # Construir valores garantindo validação dos campos
            values = (
                tratar_valor(formulario_referencia._cnpj_companhia),
                tratar_valor(formulario_referencia._categoria_doc),
                tratar_valor(formulario_referencia._denominacao_companhia),
                tratar_valor(formulario_referencia._id_doc, tipo="int"),
                tratar_valor(formulario_referencia._link_doc),
                tratar_valor(formulario_referencia._versao, tipo="int"),
                tratar_valor(formulario_referencia.data_recebimento_doc, tipo="date"),
                tratar_valor(formulario_referencia.data_referencia_doc, tipo="date"),
                tratar_valor(formulario_referencia._data_doc, tipo="date"),
                tratar_valor(formulario_referencia._mes_doc, tipo="int"),
                tratar_valor(formulario_referencia._ano_doc, tipo="int"),
            )
            # print("\n\n")
            # Gerar query SQL formatada para depuração
            # formatted_query = query.replace("%s", "{}").format(
            #     *[f"'{v}'" if v is not None else "NULL" for v in values]
            # )
            # print("SQL gerado para execução:\n", formatted_query)

            cursor.execute(query, values)
            # self.connection.commit()
            # escrever_linha_em_branco()
            # escrever_linha_separador()
            # escrever_linha_em_branco()
            # self.logger.info(f"Empresa {empresa._nome_empresa} do ano {empresa._ano_doc} inserida com sucesso.")
            # escrever_linha_em_branco()
            self.log_sucesso.info(
                f"Formulário de Referência {formulario_referencia._denominacao_companhia}, do CNPJ: {formulario_referencia._cnpj_companhia} e do ano {formulario_referencia._ano_doc} inserida com sucesso."
            )
            print(
                f"Formulário de Referência {formulario_referencia._denominacao_companhia} inserida com sucesso."
            )
            escrever_linha_em_branco(self.log_sucesso)
        except sqlite3.Error as e:
            escrever_linha_em_branco(self.log_erro)
            escrever_linha_separador(self.log_erro)
            escrever_linha_em_branco(self.log_erro)

            self.log_erro.error(
                f"Erro ao inserir Formulário de Referência {formulario_referencia._denominacao_companhia}, do CNPJ: {formulario_referencia._cnpj_companhia} e do ano {formulario_referencia._ano_doc}, erro: {e}."
            )
            escrever_linha_em_branco(self.log_erro)
            print(
                f"Erro ao inserir Formulário de Referência {formulario_referencia._denominacao_companhia}, do CNPJ: {formulario_referencia._cnpj_companhia} e do ano {formulario_referencia._ano_doc}, erro: {e}."
            )


def tratar_valor(valor, tipo=None):
    if str(valor).lower() == "nan" or valor is None:
        return None
    if tipo == "int":
        try:
            return int(valor)
        except (ValueError, TypeError):
            return None
    elif tipo == "date":
        try:
            return str(valor) if str(valor) != "" else None
        except (ValueError, TypeError):
            return None
    else:
        return valor
