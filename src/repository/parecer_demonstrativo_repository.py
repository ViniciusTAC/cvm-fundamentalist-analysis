import sqlite3
import os
from datetime import datetime
# from zoneinfo import ZoneInfo
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
        sucesso_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        sucesso_logger.addHandler(sucesso_handler)

        erro_logger = logging.getLogger(f"erro_{id(self)}")
        erro_logger.setLevel(nivel)
        erro_handler = logging.FileHandler(
            os.path.join(log_erro_dir, "erro.log"), encoding="utf-8"
        )
        erro_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        erro_logger.addHandler(erro_handler)

        # return sucesso_logger, erro_logger


        # os.makedirs(log_sucesso_dir, exist_ok=True)
        # os.makedirs(log_erro_dir, exist_ok=True)

        # sucesso_logger = logging.getLogger("sucesso")
        # sucesso_logger.setLevel(logging.INFO)
        # sucesso_handler = logging.FileHandler(
        #     os.path.join(log_sucesso_dir, "sucesso.log"), encoding="utf-8"
        # )
        # sucesso_handler.setFormatter(
        #     logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        # )
        # if not sucesso_logger.handlers:
        #     sucesso_logger.addHandler(sucesso_handler)

        # erro_logger = logging.getLogger("erro")
        # erro_logger.setLevel(logging.WARNING)
        # erro_handler = logging.FileHandler(
        #     os.path.join(log_erro_dir, "erro.log"), encoding="utf-8"
        # )
        # erro_handler.setFormatter(
        #     logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        # )
        # if not erro_logger.handlers:
        #     erro_logger.addHandler(erro_handler)


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

    def inserir_parecer_demonstrativo(self, parecer_demonstrativo):
        try:
            cursor = self.connection.cursor()
            query = """
                            INSERT INTO parecer_demonstrativo (
                                cnpj_companhia,
                                num_linha_parecer_declaracao,
                                id_tipo_parecer,
                                id_tipo_rel_auditor,
                                texto_parecer_declaracao,
                                versao,
                                data_referencia_doc,
                                mes,
                                ano
                            ) VALUES (
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
                tratar_valor(parecer_demonstrativo.cnpj_companhia),
                tratar_valor(parecer_demonstrativo.num_linha_parecer_declaracao, tipo="int"),
                tratar_valor(parecer_demonstrativo.id_tipo_rel_auditor, tipo="int"),
                tratar_valor(parecer_demonstrativo.id_tipo_rel_auditor, tipo="int"),
                tratar_valor(parecer_demonstrativo.texto_parecer_declaracao),
                tratar_valor(parecer_demonstrativo.versao, tipo="int"),
                tratar_valor(parecer_demonstrativo.data_referencia_doc, tipo="date"),
                tratar_valor(parecer_demonstrativo.mes, tipo="int"),
                tratar_valor(parecer_demonstrativo.ano, tipo="int"),
            )
            # print("\n\n")
            # # Gerar query SQL formatada para depuração
            # formatted_query = query.replace("%s", "{}").format(
            #     *[f"'{v}'" if v is not None else "NULL" for v in values]
            # )
            # print("SQL gerado para execução:\n", formatted_query)

            cursor.execute(query, values)
            # self.connection.commit()
            # escrever_linha_em_branco()
            # escrever_linha_separador()
            # escrever_linha_em_branco()
            # self.logger.info(f"Empresa {empresa._nome_empresa} do ano {empresa.ano} inserida com sucesso.")
            # escrever_linha_em_branco()
            self.log_sucesso.info(f"Parecer Demonstrativo do CNPJ: {parecer_demonstrativo._cnpj_companhia} e do ano {parecer_demonstrativo.ano} inserida com sucesso.")
            print(
                f"Parecer Demonstrativo  do CNPJ: {parecer_demonstrativo._cnpj_companhia} e do ano {parecer_demonstrativo.ano} inserida com sucesso."
            )
            escrever_linha_em_branco(self.log_sucesso)
        except sqlite3.Error as e:
            escrever_linha_em_branco(self.log_erro)
            escrever_linha_separador(self.log_erro)
            escrever_linha_em_branco(self.log_erro)

            self.log_erro.error(
                f"Erro ao inserir Parecer Demonstrativo do CNPJ: {parecer_demonstrativo._cnpj_companhia} e do ano {parecer_demonstrativo.ano}, erro: {e}."
            )
            escrever_linha_em_branco(self.log_erro)
            print(
                f"Erro ao inserir Parecer Demonstrativo  do CNPJ: {parecer_demonstrativo._cnpj_companhia} e do ano {parecer_demonstrativo.ano}, erro: {e}."
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