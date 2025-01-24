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
#         self.logger = self._setup_logger()
        

#     def _setup_logger(self):
#         os.makedirs("logs", exist_ok=True)
#         log_filename = f"logs/logs_inserção_banco/{datetime.now().strftime('%Y-%m-%d')}.log"
#         logging.basicConfig(
#             level=logging.INFO,
#             format="%(asctime)s - %(levelname)s - %(message)s",
#             handlers=[
#                 logging.FileHandler(log_filename, encoding="utf-8"),
#                 logging.StreamHandler()
#             ]
#         )
#         return logging.getLogger(__name__)

#     def conectar(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host=self.host,
#                 database=self.database,
#                 user=self.user,
#                 password=self.password
#             )
#             if self.connection.is_connected():
#                 print("Conexão com o banco de dados estabelecida com sucesso.")
#         except Error as e:
#             print(f"Erro ao conectar ao banco de dados: {e}")

#     def desconectar(self):
#         if self.connection and self.connection.is_connected():
#             self.connection.close()
#             print("Conexão com o banco de dados encerrada.")



#     def inserir_empresa(self, empresa):
#         try:
#             cursor = self.connection.cursor()
#             query = """
#                 INSERT INTO empresas (
#                     categoria_doc, codigo_cvm, cnpj_companhia, descricao_atividade, especie_controle_acionario,
#                     identificador_documento, mes_encerramento_exercicio_social, nome_empresa, nome_anterior_empresa,
#                     pagina_web, pais_custodia_valores_mobiliarios, pais_origem, setor_atividade, situacao_emissor,
#                     situacao_registro_cvm, versao, data_registro_cvm, data_nome_empresarial, data_categoria_registro_cvm,
#                     data_situacao_registro_cvm, data_constituicao, data_especie_controle_acionario,
#                     data_referencia_documento, data_situacao_emissor, data_alteracao_exercicio_social,
#                     dia_encerramento_exercicio_social, data_doc, mes_doc, ano_doc
#                 ) VALUES (
#                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
#                 )
#             """
#             # Construir valores garantindo que não haja extras e substituindo 'nan' por None
#             # Construir valores garantindo validação dos campos
#             values = (
#                 tratar_valor(empresa._categoria_doc),
#                 tratar_valor(empresa._codigo_cvm),
#                 tratar_valor(empresa._cnpj_companhia),
#                 tratar_valor(empresa._descricao_atividade),
#                 tratar_valor(empresa._especie_controle_acionario),
#                 tratar_valor(empresa._identificador_documento),
#                 tratar_valor(empresa._mes_encerramento_exercicio_social, tipo='int'),
#                 tratar_valor(empresa._nome_empresa),
#                 tratar_valor(empresa._nome_anterior_empresa),
#                 tratar_valor(empresa._pagina_web),
#                 tratar_valor(empresa._pais_custodia_valores_mobiliarios),
#                 tratar_valor(empresa._pais_origem),
#                 tratar_valor(empresa._setor_atividade),
#                 tratar_valor(empresa._situacao_emissor),
#                 tratar_valor(empresa._situacao_registro_cvm),
#                 tratar_valor(empresa._versao, tipo='int'),
#                 tratar_valor(empresa._data_registro_cvm, tipo='date'),
#                 tratar_valor(empresa._data_nome_empresarial, tipo='date'),
#                 tratar_valor(empresa._data_categoria_registro_cvm, tipo='date'),
#                 tratar_valor(empresa._data_situacao_registro_cvm, tipo='date'),
#                 tratar_valor(empresa._data_constituicao, tipo='date'),
#                 tratar_valor(empresa.data_especie_controle_acionario, tipo='date'),
#                 tratar_valor(empresa._data_referencia_documento, tipo='date'),
#                 tratar_valor(empresa._data_situacao_emissor, tipo='date'),
#                 tratar_valor(empresa.data_alteracao_exercicio_social, tipo='date'),
#                 tratar_valor(empresa._dia_encerramento_exercicio_social, tipo='int'),
#                 tratar_valor(empresa._data_doc, tipo='date'),
#                 tratar_valor(empresa._mes_doc, tipo='int'),
#                 tratar_valor(empresa._ano_doc, tipo='int'),
#             )
#             print("\n\n")
#             # Gerar query SQL formatada para depuração
#             formatted_query = query.replace("%s", "{}").format(*[
#                 f"'{v}'" if v is not None else "NULL" for v in values
#             ])
#             print("SQL gerado para execução:\n", formatted_query)
            

#             cursor.execute(query, values)
#             self.connection.commit()
#             # escrever_linha_em_branco()
#             # escrever_linha_separador()
#             # escrever_linha_em_branco()
#             # self.logger.info(f"Empresa {empresa._nome_empresa} do ano {empresa._ano_doc} inserida com sucesso.")
#             # escrever_linha_em_branco()
#             print(f"Empresa {empresa._nome_empresa} inserida com sucesso.")
#         except Error as e:
#             escrever_linha_em_branco()
#             escrever_linha_separador()
#             escrever_linha_em_branco()
#             self.logger.error(f"Erro ao inserir empresa {empresa._nome_empresa} do ano {empresa._ano_doc}, erro: {e}.")
#             escrever_linha_em_branco()
#             print(f"Erro ao inserir empresa {empresa._nome_empresa} do ano {empresa._ano_doc}, erro: {e}.")

# def tratar_valor(valor, tipo=None):
#         """
#         Trata um valor, convertendo 'nan' ou valores inválidos em None.
#         Opcionalmente, converte o valor para o tipo especificado.
        
#         :param valor: O valor a ser tratado.
#         :param tipo: O tipo esperado (str, int, float, etc.) ou 'date' para datas.
#         :return: O valor tratado ou None.
#         """
#         if str(valor).lower() == 'nan' or valor is None:
#             return None
        
#         if tipo == 'int':
#             try:
#                 return int(valor)
#             except (ValueError, TypeError):
#                 return None
#         elif tipo == 'date':
#             try:
#                 # Garantir que o valor seja uma string válida para data
#                 return str(valor) if str(valor) != '' else None
#             except (ValueError, TypeError):
#                 return None
#         else:
#             return valor  # Retorna o valor original se não precisa de conversão


import mysql.connector
from mysql.connector import Error
from sqlalchemy import null
import os
from datetime import datetime
import logging
from utils.logger import escrever_linha_em_branco, escrever_linha_separador


class ConexaoBanco:
    """Classe para gerenciar a conexão com o banco de dados MySQL."""

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.log_sucesso, self.log_erro = self._setup_logger()


    def _setup_logger(self, log_dir="logs/logs_insercao"):
        # Diretórios para logs de sucesso e erro
        hoje = datetime.now().strftime("%Y-%m-%d")
        log_sucesso_dir = os.path.join(log_dir, hoje)
        log_erro_dir = os.path.join(log_dir, hoje)

        os.makedirs(log_sucesso_dir, exist_ok=True)
        os.makedirs(log_erro_dir, exist_ok=True)

        # Configuração do logger de sucesso
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

        # Configuração do logger de erro
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
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            if self.connection.is_connected():
                print("Conexão com o banco de dados estabelecida com sucesso.")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def desconectar(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")

    def inserir_empresa(self, empresa):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO empresas (
                    categoria_doc, codigo_cvm, cnpj_companhia, descricao_atividade, especie_controle_acionario,
                    identificador_documento, mes_encerramento_exercicio_social, nome_empresa, nome_anterior_empresa,
                    pagina_web, pais_custodia_valores_mobiliarios, pais_origem, setor_atividade, situacao_emissor,
                    situacao_registro_cvm, versao, data_registro_cvm, data_nome_empresarial, data_categoria_registro_cvm,
                    data_situacao_registro_cvm, data_constituicao, data_especie_controle_acionario,
                    data_referencia_documento, data_situacao_emissor, data_alteracao_exercicio_social,
                    dia_encerramento_exercicio_social, data_doc, mes_doc, ano_doc
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
            """
            # Construir valores garantindo que não haja extras e substituindo 'nan' por None
            # Construir valores garantindo validação dos campos
            values = (
                tratar_valor(empresa._categoria_doc),
                tratar_valor(empresa._codigo_cvm),
                tratar_valor(empresa._cnpj_companhia),
                tratar_valor(empresa._descricao_atividade),
                tratar_valor(empresa._especie_controle_acionario),
                tratar_valor(empresa._identificador_documento),
                tratar_valor(empresa._mes_encerramento_exercicio_social, tipo='int'),
                tratar_valor(empresa._nome_empresa),
                tratar_valor(empresa._nome_anterior_empresa),
                tratar_valor(empresa._pagina_web),
                tratar_valor(empresa._pais_custodia_valores_mobiliarios),
                tratar_valor(empresa._pais_origem),
                tratar_valor(empresa._setor_atividade),
                tratar_valor(empresa._situacao_emissor),
                tratar_valor(empresa._situacao_registro_cvm),
                tratar_valor(empresa._versao, tipo='int'),
                tratar_valor(empresa._data_registro_cvm, tipo='date'),
                tratar_valor(empresa._data_nome_empresarial, tipo='date'),
                tratar_valor(empresa._data_categoria_registro_cvm, tipo='date'),
                tratar_valor(empresa._data_situacao_registro_cvm, tipo='date'),
                tratar_valor(empresa._data_constituicao, tipo='date'),
                tratar_valor(empresa.data_especie_controle_acionario, tipo='date'),
                tratar_valor(empresa._data_referencia_documento, tipo='date'),
                tratar_valor(empresa._data_situacao_emissor, tipo='date'),
                tratar_valor(empresa.data_alteracao_exercicio_social, tipo='date'),
                tratar_valor(empresa._dia_encerramento_exercicio_social, tipo='int'),
                tratar_valor(empresa._data_doc, tipo='date'),
                tratar_valor(empresa._mes_doc, tipo='int'),
                tratar_valor(empresa._ano_doc, tipo='int'),
            )
            print("\n\n")
            # Gerar query SQL formatada para depuração
            formatted_query = query.replace("%s", "{}").format(*[
                f"'{v}'" if v is not None else "NULL" for v in values
            ])
            print("SQL gerado para execução:\n", formatted_query)
            

            cursor.execute(query, values)
            self.connection.commit()
            # escrever_linha_em_branco()
            # escrever_linha_separador()
            # escrever_linha_em_branco()
            # self.logger.info(f"Empresa {empresa._nome_empresa} do ano {empresa._ano_doc} inserida com sucesso.")
            # escrever_linha_em_branco()
            self.log_sucesso.info(f"Periodicos e Eventuais {empresa._nome_empresa}, do CNPJ: {empresa._cnpj_companhia} e do ano {empresa._ano_doc} inserida com sucesso.")
            print(f"Empresa {empresa._nome_empresa} inserida com sucesso.")
        except Error as e:
            escrever_linha_em_branco(self.log_erro)
            escrever_linha_separador(self.log_erro)
            escrever_linha_em_branco(self.log_erro)
            self.log_erro.error(f"Erro ao inserir empresa {empresa._nome_empresa} do ano {empresa._ano_doc}, erro: {e}.")
            escrever_linha_em_branco(self.log_erro)
            print(f"Erro ao inserir empresa {empresa._nome_empresa} do ano {empresa._ano_doc}, erro: {e}.")


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



