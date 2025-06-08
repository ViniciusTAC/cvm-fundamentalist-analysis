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

    def inserir_periodicos_eventuais(self, periodicos_eventuais):
        try:
            cursor = self.connection.cursor()
            query = """
                            INSERT INTO periodicos_eventuais (
                                cnpj_companhia,
                                id_assunto,
                                id_categoria_doc,
                                id_especie_eventual,
                                link_doc,
                                protocolo_entrega,
                                id_tipo_evento,
                                id_tipo_apres,
                                versao,
                                data_entrega,
                                data_referencia,
                                data_doc,
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
                tratar_valor(periodicos_eventuais.cnpj_companhia),
                tratar_valor(periodicos_eventuais.id_assunto, tipo="int"),
                tratar_valor(periodicos_eventuais.id_categoria_doc, tipo="int"),
                tratar_valor(periodicos_eventuais.id_especie_eventual, tipo="int"),
                tratar_valor(periodicos_eventuais.link_doc),
                tratar_valor(periodicos_eventuais.protocolo_entrega),
                tratar_valor(periodicos_eventuais.id_tipo_evento, tipo="int"),
                tratar_valor(periodicos_eventuais.id_tipo_apres, tipo="int"),
                tratar_valor(periodicos_eventuais.versao, tipo="int"),
                tratar_valor(periodicos_eventuais.data_entrega, tipo="date"),
                tratar_valor(periodicos_eventuais.data_referencia, tipo="date"),
                tratar_valor(periodicos_eventuais.data_doc, tipo="date"),
                tratar_valor(periodicos_eventuais.mes, tipo="int"),
                tratar_valor(periodicos_eventuais.ano, tipo="int"),
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
                f"Periodicos e Eventuais do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano} inserida com sucesso."
            )
            print(
                f"Periodicos e Eventuais {periodicos_eventuais._cnpj_companhia} inserida com sucesso."
            )
            escrever_linha_em_branco(self.log_sucesso)
        except sqlite3.Error as e:
            escrever_linha_em_branco(self.log_erro)
            escrever_linha_separador(self.log_erro)
            escrever_linha_em_branco(self.log_erro)

            self.log_erro.error(
                f"Erro ao inserir Periodicos e Eventuais do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano}, erro: {e}."
            )
            escrever_linha_em_branco(self.log_erro)
            print(
                f"Erro ao inserir Periodicos e Eventuais do CNPJ: {periodicos_eventuais._cnpj_companhia} e do ano {periodicos_eventuais._ano}, erro: {e}."
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
