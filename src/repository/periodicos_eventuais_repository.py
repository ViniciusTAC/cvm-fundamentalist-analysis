# import mysql.connector
# from mysql.connector import Error
# from sqlalchemy import null
# import os
# from datetime import datetime
# import logging
# from utils.logger import escrever_linha_em_branco, escrever_linha_separador


# class ConexaoBanco:
#     """Classe para gerenciar a conexão com o banco de dados MySQL."""

#     def __init__(self, host, database, user, password):
#         self.host = host
#         self.database = database
#         self.user = user
#         self.password = password
#         self.connection = None
#         self.log_sucesso, self.log_erro = self._setup_logger()


#     def _setup_logger(self, log_dir="logs/logs_insercao"):
#         # Diretórios para logs de sucesso e erro
#         hoje = datetime.now().strftime("%Y-%m-%d")
#         log_sucesso_dir = os.path.join(log_dir, hoje)
#         log_erro_dir = os.path.join(log_dir, hoje)

#         os.makedirs(log_sucesso_dir, exist_ok=True)
#         os.makedirs(log_erro_dir, exist_ok=True)

#         # Configuração do logger de sucesso
#         sucesso_logger = logging.getLogger("sucesso")
#         sucesso_logger.setLevel(logging.INFO)
#         sucesso_handler = logging.FileHandler(
#             os.path.join(log_sucesso_dir, "sucesso.log"), encoding="utf-8"
#         )
#         sucesso_handler.setFormatter(
#             logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#         )
#         if not sucesso_logger.handlers:
#             sucesso_logger.addHandler(sucesso_handler)

#         # Configuração do logger de erro
#         erro_logger = logging.getLogger("erro")
#         erro_logger.setLevel(logging.WARNING)
#         erro_handler = logging.FileHandler(
#             os.path.join(log_erro_dir, "erro.log"), encoding="utf-8"
#         )
#         erro_handler.setFormatter(
#             logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#         )
#         if not erro_logger.handlers:
#             erro_logger.addHandler(erro_handler)

#         return sucesso_logger, erro_logger

#     def conectar(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host=self.host,
#                 database=self.database,
#                 user=self.user,
#                 password=self.password,
#             )
#             if self.connection.is_connected():
#                 print("Conexão com o banco de dados estabelecida com sucesso.")
#         except Error as e:
#             print(f"Erro ao conectar ao banco de dados: {e}")

#     def desconectar(self):
#         if self.connection and self.connection.is_connected():
#             self.connection.close()
#             print("Conexão com o banco de dados encerrada.")

#     def inserir_periodicos_eventuais(self, periodicos_eventuais):
#         try:
#             cursor = self.connection.cursor()
#             query = """
#                             INSERT INTO periodicos_eventuais (
#                                 cnpj_companhia,
#                                 codigo_cvm,
#                                 assunto,
#                                 categoria_doc,
#                                 especie,
#                                 link_doc,
#                                 nome_companhia,
#                                 protocolo_entrega,
#                                 tipo,
#                                 tipo_apresentacao,
#                                 versao,
#                                 data_entrega_doc,
#                                 data_referencia_doc,
#                                 data_doc,
#                                 mes_doc,
#                                 ano_doc
#                             ) VALUES (
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s,
#                                 %s
#                             )
#                     """
#             # Construir valores garantindo que não haja extras e substituindo 'nan' por None
#             # Construir valores garantindo validação dos campos
#             values = (
#                 tratar_valor(periodicos_eventuais._cnpj_companhia),
#                 tratar_valor(periodicos_eventuais._codigo_cvm),
#                 tratar_valor(periodicos_eventuais._assunto),
#                 tratar_valor(periodicos_eventuais._categoria_doc),
#                 tratar_valor(periodicos_eventuais._especie),
#                 tratar_valor(periodicos_eventuais._link_doc),
#                 tratar_valor(periodicos_eventuais._nome_companhia),
#                 tratar_valor(periodicos_eventuais._protocolo_entrega),
#                 tratar_valor(periodicos_eventuais._tipo),
#                 tratar_valor(periodicos_eventuais._tipo_apresentacao),
#                 tratar_valor(periodicos_eventuais._versao, tipo="int"),
#                 tratar_valor(periodicos_eventuais._data_entrega_doc, tipo="date"),
#                 tratar_valor(periodicos_eventuais._data_referencia_doc, tipo="date"),
#                 tratar_valor(periodicos_eventuais._data_doc, tipo="date"),
#                 tratar_valor(periodicos_eventuais._mes_doc, tipo="int"),
#                 tratar_valor(periodicos_eventuais._ano_doc, tipo="int"),
#             )
#             print("\n\n")
#             # Gerar query SQL formatada para depuração
#             formatted_query = query.replace("%s", "{}").format(
#                 *[f"'{v}'" if v is not None else "NULL" for v in values]
#             )
#             print("SQL gerado para execução:\n", formatted_query)

#             cursor.execute(query, values)
#             self.connection.commit()
#             self.log_sucesso.info(f"Periodicos e Eventuais {periodicos_eventuais._nome_companhia}, do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano_doc} inserida com sucesso.")
#             print(
#                 f"Periodicos e Eventuais {periodicos_eventuais._nome_companhia} inserida com sucesso."
#             )
#             escrever_linha_em_branco(self.log_sucesso)
#         except Error as e:
#             escrever_linha_em_branco(self.log_erro)
#             escrever_linha_separador(self.log_erro)
#             escrever_linha_em_branco(self.log_erro)

#             self.log_erro.error(
#                 f"Erro ao inserir Periodicos e Eventuais {periodicos_eventuais._nome_companhia}, do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano_doc}, erro: {e}."
#             )
#             escrever_linha_em_branco(self.log_erro)
#             print(
#                 f"Erro ao inserir Periodicos e Eventuais {periodicos_eventuais._nome_companhia}, do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano_doc}, erro: {e}."
#             )


# def tratar_valor(valor, tipo=None):
#     """
#     Trata um valor, convertendo 'nan' ou valores inválidos em None.
#     Opcionalmente, converte o valor para o tipo especificado.

#     :param valor: O valor a ser tratado.
#     :param tipo: O tipo esperado (str, int, float, etc.) ou 'date' para datas.
#     :return: O valor tratado ou None.
#     """
#     if str(valor).lower() == "nan" or valor is None:
#         return None

#     if tipo == "int":
#         try:
#             return int(valor)
#         except (ValueError, TypeError):
#             return None
#     elif tipo == "date":
#         try:
#             # Garantir que o valor seja uma string válida para data
#             return str(valor) if str(valor) != "" else None
#         except (ValueError, TypeError):
#             return None
#     else:
#         return valor  # Retorna o valor original se não precisa de conversão


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

    def inserir_periodicos_eventuais(self, periodicos_eventuais):
        try:
            cursor = self.connection.cursor()
            query = """
                            INSERT INTO periodicos_eventuais (
                                cnpj_companhia,
                                codigo_cvm,
                                assunto,
                                categoria_doc,
                                especie,
                                link_doc,
                                nome_companhia,
                                protocolo_entrega,
                                tipo,
                                tipo_apresentacao,
                                versao,
                                data_entrega_doc,
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
                tratar_valor(periodicos_eventuais._cnpj_companhia),
                tratar_valor(periodicos_eventuais._codigo_cvm),
                tratar_valor(periodicos_eventuais._assunto),
                tratar_valor(periodicos_eventuais._categoria_doc),
                tratar_valor(periodicos_eventuais._especie),
                tratar_valor(periodicos_eventuais._link_doc),
                tratar_valor(periodicos_eventuais._nome_companhia),
                tratar_valor(periodicos_eventuais._protocolo_entrega),
                tratar_valor(periodicos_eventuais._tipo),
                tratar_valor(periodicos_eventuais._tipo_apresentacao),
                tratar_valor(periodicos_eventuais._versao, tipo="int"),
                tratar_valor(periodicos_eventuais._data_entrega_doc, tipo="date"),
                tratar_valor(periodicos_eventuais._data_referencia_doc, tipo="date"),
                tratar_valor(periodicos_eventuais._data_doc, tipo="date"),
                tratar_valor(periodicos_eventuais._mes_doc, tipo="int"),
                tratar_valor(periodicos_eventuais._ano_doc, tipo="int"),
            )
            # print("\n\n")
            # # Gerar query SQL formatada para depuração
            # formatted_query = query.replace("%s", "{}").format(
            #     *[f"'{v}'" if v is not None else "NULL" for v in values]
            # )
            # print("SQL gerado para execução:\n", formatted_query)

            cursor.execute(query, values)
            # self.connection.commit()
            self.log_sucesso.info(
                f"Periodicos e Eventuais {periodicos_eventuais._nome_companhia}, do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano_doc} inserida com sucesso."
            )
            print(
                f"Periodicos e Eventuais {periodicos_eventuais._nome_companhia} inserida com sucesso."
            )
            escrever_linha_em_branco(self.log_sucesso)
        except sqlite3.Error as e:
            escrever_linha_em_branco(self.log_erro)
            escrever_linha_separador(self.log_erro)
            escrever_linha_em_branco(self.log_erro)

            self.log_erro.error(
                f"Erro ao inserir Periodicos e Eventuais {periodicos_eventuais._nome_companhia}, do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano_doc}, erro: {e}."
            )
            escrever_linha_em_branco(self.log_erro)
            print(
                f"Erro ao inserir Periodicos e Eventuais {periodicos_eventuais._nome_companhia}, do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano_doc}, erro: {e}."
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
