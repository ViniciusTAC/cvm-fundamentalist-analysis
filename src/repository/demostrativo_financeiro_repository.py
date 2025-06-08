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

    def inserir_ou_atualizar_demonstrativo(self, demonstrativo):
        try:

            def debug_sql(query, values):
                print("\n--- SQL GERADO ---")
                parts = query.split("?")
                sql_with_values = ""

                for i in range(len(parts) - 1):
                    val = values[i]
                    if isinstance(val, str):
                        val_str = f"'{val}'"
                    elif val is None:
                        val_str = "NULL"
                    else:
                        val_str = str(val)
                    sql_with_values += parts[i] + val_str

                sql_with_values += parts[-1]
                print(sql_with_values)
                print("--- FIM SQL ---\n")

            cursor = self.connection.cursor()
            # agora_local = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime('%Y-%m-%d %H:%M:%S')

            query = """
                INSERT INTO demonstrativo_financeiro (
                    codigo_cvm,
                    id_plano_conta,
                    id_escala,
                    codigo_grupo_dfp,
                    id_moeda,
                    id_ordem,
                    conta_fixa,
                    versao,
                    data_inicio_exercicio,
                    data_fim_exercicio,
                    data_referencia_doc,
                    valor_conta,
                    data_doc,
                    mes_doc,
                    ano_doc
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(codigo_cvm, id_plano_conta, codigo_grupo_dfp, conta_fixa, mes_doc, ano_doc) DO UPDATE SET
                    id_escala = excluded.id_escala,
                    id_moeda = excluded.id_moeda,
                    id_ordem = excluded.id_ordem,
                    versao = excluded.versao,
                    data_inicio_exercicio = excluded.data_inicio_exercicio,
                    data_fim_exercicio = excluded.data_fim_exercicio,
                    data_referencia_doc = excluded.data_referencia_doc,
                    valor_conta = excluded.valor_conta,
                    data_doc = excluded.data_doc
            """

            values = (
                tratar_valor(demonstrativo.codigo_cvm),
                tratar_valor(demonstrativo.id_plano_conta),
                tratar_valor(demonstrativo.id_escala),
                tratar_valor(demonstrativo.codigo_grupo_dfp),
                tratar_valor(demonstrativo.id_moeda, tipo="int"),
                tratar_valor(demonstrativo.id_ordem, tipo="int"),
                tratar_valor(demonstrativo.conta_fixa),
                tratar_valor(demonstrativo.versao, tipo="int"),
                tratar_valor(demonstrativo.data_inicio_exercicio, tipo="date"),
                tratar_valor(demonstrativo.data_fim_exercicio, tipo="date"),
                tratar_valor(demonstrativo.data_referencia_doc, tipo="date"),
                tratar_valor(demonstrativo.valor_conta, tipo="float"),
                tratar_valor(demonstrativo.data_doc, tipo="date"),
                tratar_valor(demonstrativo.mes, tipo="int"),
                tratar_valor(demonstrativo.ano, tipo="int"),
            )
            # debug_sql(query, values)
            cursor.execute(query, values)

            # self.connection.commit()
            self.log_sucesso.info(
                f"Demonstrativo inserido para CNPJ {demonstrativo._cnpj_companhia}, conta {demonstrativo._codigo_conta}, mês {demonstrativo._mes_doc}, ano {demonstrativo._ano_doc}."
            )
            print(
                f"✔ Demonstrativo inserido para CNPJ {demonstrativo._cnpj_companhia}, conta {demonstrativo._codigo_conta}."
            )
        except sqlite3.Error as e:
            escrever_linha_em_branco(self.log_erro)
            escrever_linha_separador(self.log_erro)
            self.log_erro.error(
                f"Erro ao inserir demonstrativo para CNPJ {demonstrativo._cnpj_companhia}, conta {demonstrativo._codigo_conta}, erro: {e}."
            )
            print(
                f"❌ Erro ao inserir demonstrativo para CNPJ {demonstrativo._cnpj_companhia}, erro: {e}"
            )


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
