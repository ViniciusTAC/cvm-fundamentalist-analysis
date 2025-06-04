import sqlite3
import os
from datetime import datetime
import logging
from utils.logger import escrever_linha_em_branco, escrever_linha_separador


class ConexaoBanco:
    """Classe para gerenciar a conexão com o banco de dados SQLite."""

    def __init__(self, db_path, nivel=logging.WARNING):
        self.db_path = db_path
        self.connection = None
        self.log_sucesso, self.log_erro = self._setup_logger(nivel=nivel)

    def _setup_logger(self, log_dir="logs/logs_insercao", nivel=logging.WARNING):
        hoje = datetime.now().strftime("%Y-%m-%d")
        log_sucesso_dir = os.path.join(log_dir, hoje)
        log_erro_dir = os.path.join(log_dir, hoje)

        os.makedirs(log_sucesso_dir, exist_ok=True)
        os.makedirs(log_erro_dir, exist_ok=True)

        sucesso_logger = logging.getLogger(f"sucesso_{id(self)}")
        sucesso_logger.setLevel(nivel)
        sucesso_handler = logging.FileHandler(
            os.path.join(log_sucesso_dir, "sucesso.log"), encoding="utf-8"
        )
        sucesso_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        sucesso_logger.addHandler(sucesso_handler)

        erro_logger = logging.getLogger(f"erro_{id(self)}")
        erro_logger.setLevel(nivel)
        erro_handler = logging.FileHandler(
            os.path.join(log_erro_dir, "erro.log"), encoding="utf-8"
        )
        erro_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        erro_logger.addHandler(erro_handler)

        # return sucesso_logger, erro_logger

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

    def inserir_ou_ignorar_tipo_relatorio_especial(self, tipo_relatorio_especial):
        try:
            cursor = self.connection.cursor()

            query = """
                INSERT INTO tipo_relatorio_especial (
                    descricao
                )
                VALUES (
                    ?
                )
            """

            values = (tratar_valor(tipo_relatorio_especial._descricao),)

            cursor.execute(query, values)
            # self.connection.commit()
            self.log_sucesso.info(
                f"Tipo relatorio especial: {tipo_relatorio_especial._descricao} inserida/atualizada com sucesso."
            )
            print(
                f"Tipo relatorio especial: {tipo_relatorio_especial._descricao} inserida com sucesso."
            )
        except sqlite3.Error as e:
            escrever_linha_em_branco(self.log_erro)
            escrever_linha_separador(self.log_erro)
            escrever_linha_em_branco(self.log_erro)
            self.log_erro.error(
                f"Erro ao inserir Tipo relatorio especial: {tipo_relatorio_especial._descricao}, erro: {e}."
            )
            escrever_linha_em_branco(self.log_erro)
            print(
                f"Erro ao inserir Tipo relatorio especial: {tipo_relatorio_especial._descricao}, erro: {e}."
            )
            # if commit:
            #     self.connection.rollback()
            # raise


def tratar_valor(valor, tipo=None):
    """
    Trata um valor, convertendo 'nan' ou valores inválidos em None.
    Opcionalmente, converte o valor para o tipo especificado.

    :param valor: O valor a ser tratado.
    :param tipo: O tipo esperado (str, int, float, etc.) ou 'date' para datas.
    :return: O valor tratado ou None.
    """
    if str(valor).lower() == "nan" or valor is None:
        return None

    if tipo == "int":
        try:
            return int(valor)
        except (ValueError, TypeError):
            return None
    elif tipo == "date":
        try:
            # Garantir que o valor seja uma string válida para data
            return str(valor) if str(valor) != "" else None
        except (ValueError, TypeError):
            return None
    else:
        return valor  # Retorna o valor original se não precisa de conversão
