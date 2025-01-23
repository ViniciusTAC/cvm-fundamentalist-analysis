# import mysql.connector
# from mysql.connector import Error

# class ConexaoBanco:
#     """Classe para gerenciar a conexão com o banco de dados MySQL."""

#     def __init__(self, host, database, user, password):
#         self.host = host
#         self.database = database
#         self.user = user
#         self.password = password
#         self.connection = None

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







import mysql.connector
from mysql.connector import Error
from sqlalchemy import null
# from utils.logger import escrever_linha_em_branco, escrever_linha_separador

class ConexaoBanco:
    """Classe para gerenciar a conexão com o banco de dados MySQL."""

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
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
            values = (
                empresa._categoria_doc,
                empresa._codigo_cvm,
                empresa._cnpj_companhia,
                empresa._descricao_atividade,
                empresa._especie_controle_acionario,
                empresa._identificador_documento,
                None if str(empresa._mes_encerramento_exercicio_social).lower() == 'nan' else int(empresa._mes_encerramento_exercicio_social),
                # int(empresa._mes_encerramento_exercicio_social) if empresa._mes_encerramento_exercicio_social else None,
                empresa._nome_empresa,
                None if str(empresa._nome_anterior_empresa).lower() == 'nan' else empresa._nome_anterior_empresa,
                empresa._pagina_web,
                empresa._pais_custodia_valores_mobiliarios,
                empresa._pais_origem,
                empresa._setor_atividade,
                empresa._situacao_emissor,
                empresa._situacao_registro_cvm,
                int(empresa._versao) if empresa._versao else None,
                str(empresa._data_registro_cvm) if empresa._data_registro_cvm else None,
                None if str(empresa._data_nome_empresarial).lower() == 'nan' else str(empresa._data_nome_empresarial),
                str(empresa._data_categoria_registro_cvm) if empresa._data_categoria_registro_cvm else None,
                str(empresa._data_situacao_registro_cvm) if empresa._data_situacao_registro_cvm else None,
                str(empresa._data_constituicao) if empresa._data_constituicao else None,
                None if str(empresa.data_especie_controle_acionario).lower() == 'nan' else empresa.data_especie_controle_acionario,
                str(empresa._data_referencia_documento) if empresa._data_referencia_documento else None,
                str(empresa._data_situacao_emissor) if empresa._data_situacao_emissor else None,
                None if str(empresa.data_alteracao_exercicio_social).lower() == 'nan' else empresa.data_alteracao_exercicio_social,
                None if str(empresa._dia_encerramento_exercicio_social).lower() == 'nan' else int(empresa._dia_encerramento_exercicio_social),
                # int(empresa._dia_encerramento_exercicio_social) if empresa._dia_encerramento_exercicio_social else None,
                str(empresa._data_doc) if empresa._data_doc else None,
                empresa._mes_doc,
                empresa._ano_doc,
            )
            print("\n\n")
            # Gerar query SQL formatada para depuração
            formatted_query = query.replace("%s", "{}").format(*[
                f"'{v}'" if v is not None else "NULL" for v in values
            ])
            print("SQL gerado para execução:\n", formatted_query)
            

            cursor.execute(query, values)
            self.connection.commit()
            print(f"Empresa {empresa._nome_empresa} inserida com sucesso.")
        except Error as e:
            print(f"Erro ao inserir empresa: {e}")





