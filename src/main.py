# # import os
# # import sys
# # import subprocess
# # import threading
# # import argparse
# # import logging
# # from utils.logger import (
# #     configurar_logger,
# #     escrever_linha_em_branco,
# #     escrever_linha_separador,
# # )

# # from collectors.coletor import Coletor

# # from service.empresas_service import process_csv_files as process_empresas
# # from repository.empresas_repository import ConexaoBanco as BancoEmpresas

# # from service.periodicos_eventuais_service import process_csv_files as process_ipe
# # from repository.periodicos_eventuais_repository import ConexaoBanco as BancoIPE

# # from service.formulario_referencia_service import process_csv_files as process_fre
# # from repository.formulario_referencia_repository import ConexaoBanco as BancoFRE

# # from service.parecer_demonstrativo_service import process_csv_files as process_parecer_demo
# # from repository.parecer_demonstrativo_repository import ConexaoBanco as BancoParecerDemo

# # from service.parecer_trimestral_service import process_csv_files as process_parecer_trim
# # from repository.parecer_trimestral_repository import ConexaoBanco as BancoParecerTrim

# # from service.numeros_acoes_service import process_csv_files as process_num_acoes
# # from repository.numeros_acoes_repository import ConexaoBanco as BancoNumAcoes

# # from service.demostrativo_financeiro_service import process_dfp_files as process_dfp
# # from repository.demostrativo_financeiro_repository import ConexaoBanco as BancoDemostrativo

# # from service.informacao_trimestral_service import process_dfp_files as process_itr
# # from repository.informacao_trimestral_repository import ConexaoBanco as BancoInformacaoTri


# # def configurar_argumentos():
# #     parser = argparse.ArgumentParser(description="Processador CVM")
# #     parser.add_argument("-d", "--debug", action="store_true", help="Ativa modo debug")
# #     parser.add_argument("-v", "--verbose", action="store_true", help="Ativa modo verbose")
# #     return parser.parse_args()


# # CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")
# # cancelar_evento = threading.Event()

# # ETIQUETAS = {
# #     "coletar": "Coletar e Extrair Dados",
# #     "empresas": "Empresas",
# #     "ipe": "Periódicos Eventuais",
# #     "fre": "Formulários de Referência",
# #     "parecer_demo": "Parecer - Demonst. Financeiros",
# #     "parecer_trim": "Parecer - Inf. Trimestrais",
# #     "num_acoes": "Número de Ações",
# #     "dfp": "Demonstrativos Financeiros",
# #     "itr": "Informações Trimestrais",
# # }


# # def executar_script_inicial():
# #     if os.path.exists(CAMINHO_BANCO):
# #         print("⚠️ Banco de dados já existe. Pulando execução do script.")
# #         return
# #     try:
# #         subprocess.run(
# #             [sys.executable, "sqlite-projeto/script-automatizar-sqlite.py"], check=True
# #         )
# #         print("✅ Script de automação executado com sucesso.")
# #     except subprocess.CalledProcessError as e:
# #         logger.error(f"Erro no script inicial: {str(e)}", exc_info=True)
# #         print(f"❌ Erro ao executar o script:\n{str(e)}")
# #         sys.exit(1)


# # def executar_etapa(nome, base_path, processar, repositorio_cls, metodo_insercao, extras_repo=None):
# #     banco = None
# #     try:
# #         escrever_linha_separador(logger)
# #         logger.info(f"Iniciando etapa: {nome}")

# #         dados = processar(base_path)

# #         banco = repositorio_cls(CAMINHO_BANCO, *extras_repo) if extras_repo else repositorio_cls(CAMINHO_BANCO)
# #         banco.conectar()
# #         conn = banco.connection
# #         conn.execute("BEGIN")

# #         sucesso = falha = 0
# #         erros = []

# #         for dado in dados:
# #             if cancelar_evento.is_set():
# #                 conn.rollback()
# #                 banco.desconectar()
# #                 logger.warning(f"{nome} abortado com rollback.")
# #                 return f"{nome} abortado pelo usuário."
# #             try:
# #                 getattr(banco, metodo_insercao)(dado)
# #                 sucesso += 1
# #             except Exception as e:
# #                 falha += 1
# #                 erros.append(str(e))
# #                 logger.warning(f"Erro ao inserir {dado}: {str(e)}")

# #         conn.commit()
# #         banco.desconectar()
# #         logger.info(f"{nome} finalizado com sucesso. Inseridos: {sucesso}, Falhas: {falha}")
# #         if falha:
# #             return f"{nome}: {sucesso} inseridos, {falha} com erro.\nErros: {erros[:3]}"
# #         return f"{nome}: Todos os {sucesso} registros inseridos com sucesso."

# #     except Exception as e:
# #         logger.error(f"Erro na etapa {nome}: {str(e)}", exc_info=True)
# #         try:
# #             if "conn" in locals():
# #                 conn.rollback()
# #         except:  # noqa: E722
# #             pass
# #         if banco:
# #             banco.desconectar()
# #         escrever_linha_em_branco(logger)
# #         return f"Erro fatal em {nome}: {str(e)}"


# # def run_processos_selecionados(vars):
# #     print("🔄 Executando...\n")
# #     mensagens = []
# #     executar_script_inicial()

# #     etapas = [
# #         (
# #             "empresas",
# #             "Empresas",
# #             "data_extraido/FCA/sucesso",
# #             process_empresas,
# #             BancoEmpresas,
# #             "inserir_ou_atualizar_empresa",
# #             [nivel_log],
# #         ),
# #         (
# #             "ipe",
# #             "Periódicos Eventuais",
# #             "data_extraido/IPE/sucesso",
# #             process_ipe,
# #             BancoIPE,
# #             "inserir_periodicos_eventuais",
# #             [nivel_log],
# #         ),
# #         (
# #             "fre",
# #             "Formulários de Referência",
# #             "data_extraido/FRE/sucesso",
# #             process_fre,
# #             BancoFRE,
# #             "inserir_formulario_referencia",
# #             [nivel_log],
# #         ),
# #         (
# #             "parecer_demo",
# #             "Parecer - Demonst. Financeiros",
# #             "data_extraido/DFP/sucesso",
# #             process_parecer_demo,
# #             BancoParecerDemo,
# #             "inserir_parecer_demonstrativo",
# #             [nivel_log],
# #         ),
# #         (
# #             "parecer_trim",
# #             "Parecer - Inf. Trimestrais",
# #             "data_extraido/ITR/sucesso",
# #             process_parecer_trim,
# #             BancoParecerTrim,
# #             "inserir_parecer_trimestral",
# #             [nivel_log],
# #         ),
# #     ]

# #     for chave, nome, caminho, func, banco_cls, metodo, extras in etapas:
# #         if vars[chave].get():
# #             msg = (
# #                 executar_etapa(nome, caminho, func, banco_cls, metodo, extras_repo=extras)
# #                 or f"{nome}: Nenhuma ação executada."
# #             )
# #             mensagens.append(msg)

# #     print("\n✅ Execução finalizada com sucesso.\n")
# #     resumo_texto = "\n\n".join(mensagens)
# #     print("===== RESUMO DA EXECUÇÃO =====")
# #     print(resumo_texto)
# #     with open("resumo_execucao.log", "w", encoding="utf-8") as f:
# #         f.write(resumo_texto)


# # if __name__ == "__main__":
# #     args = configurar_argumentos()

# #     if args.debug:
# #         nivel_log = logging.DEBUG
# #     elif args.verbose:
# #         nivel_log = logging.INFO
# #     else:
# #         nivel_log = logging.WARNING

# #     logger = configurar_logger(nivel=nivel_log)

# #     try:
# #         vars = {
# #             chave: type("BoolVar", (), {"get": lambda self=True: True})()
# #             for chave in ETIQUETAS.keys()
# #         }
# #         cancelar_evento.clear()
# #         run_processos_selecionados(vars)
# #     except KeyboardInterrupt:
# #         cancelar_evento.set()
# #         print("⏹ Execução cancelada pelo usuário.")
# import os
# import sys
# import subprocess
# import threading
# import argparse
# import logging
# from utils.logger import configurar_logger, escrever_linha_em_branco, escrever_linha_separador

# from collectors.coletor import Coletor

# from service.empresas_service import process_csv_files as process_empresas
# from repository.empresas_repository import ConexaoBanco as BancoEmpresas

# from service.periodicos_eventuais_service import process_csv_files as process_ipe
# from repository.periodicos_eventuais_repository import ConexaoBanco as BancoIPE

# from service.formulario_referencia_service import process_csv_files as process_fre
# from repository.formulario_referencia_repository import ConexaoBanco as BancoFRE

# from service.parecer_demonstrativo_service import (
#     process_csv_files as process_parecer_demo,
# )
# from repository.parecer_demonstrativo_repository import ConexaoBanco as BancoParecerDemo

# from service.parecer_trimestral_service import process_csv_files as process_parecer_trim
# from repository.parecer_trimestral_repository import ConexaoBanco as BancoParecerTrim

# from service.numeros_acoes_service import process_csv_files as process_num_acoes
# from repository.numeros_acoes_repository import ConexaoBanco as BancoNumAcoes

# from service.demostrativo_financeiro_service import process_dfp_files as process_dfp
# from repository.demostrativo_financeiro_repository import (
#     ConexaoBanco as BancoDemostrativo,
# )

# from service.informacao_trimestral_service import process_dfp_files as process_itr
# from repository.informacao_trimestral_repository import (
#     ConexaoBanco as BancoInformacaoTri,
# )


# def configurar_argumentos():
#     parser = argparse.ArgumentParser(description="Processador CVM")
#     parser.add_argument("-d", "--debug", action="store_true", help="Ativa modo debug")
#     parser.add_argument("-v", "--verbose", action="store_true", help="Ativa modo verbose")
#     return parser.parse_args()

# CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")
# cancelar_evento = threading.Event()

# ETIQUETAS = {
#     "coletar": "Coletar e Extrair Dados",
#     "empresas": "Empresas",
#     "ipe": "Periódicos Eventuais",
#     "fre": "Formulários de Referência",
#     "parecer_demo": "Parecer - Demonst. Financeiros",
#     "parecer_trim": "Parecer - Inf. Trimestrais",
#     "num_acoes": "Número de Ações",
#     "dfp": "Demonstrativos Financeiros",
#     "itr": "Informações Trimestrais",
# }


# def executar_script_inicial():
#     if os.path.exists(CAMINHO_BANCO):
#         print("⚠️ Banco de dados já existe. Pulando execução do script.")
#         return
#     try:
#         subprocess.run(
#             [sys.executable, "sqlite-projeto/script-automatizar-sqlite.py"], check=True
#         )
#         print("✅ Script de automação executado com sucesso.")
#     except subprocess.CalledProcessError as e:
#         logger.error(f"Erro no script inicial: {str(e)}", exc_info=True)
#         print(f"❌ Erro ao executar o script:\n{str(e)}")
#         sys.exit(1)


# def executar_etapa(
#     nome, base_path, processar, repositorio_cls, metodo_insercao, extras=None
# ):
#     try:
#         escrever_linha_separador(logger)
#         logger.info(f"Iniciando etapa: {nome}")
#         dados = (
#             processar(base_path) if extras is None else processar(base_path, *extras)
#         )
#         banco = repositorio_cls(db_path=CAMINHO_BANCO)
#         banco.conectar()
#         conn = banco.connection
#         conn.execute("BEGIN")

#         sucesso = 0
#         falha = 0
#         erros = []

#         for dado in dados:
#             if cancelar_evento.is_set():
#                 conn.rollback()
#                 banco.desconectar()
#                 logger.warning(f"{nome} abortado com rollback.")
#                 return f"{nome} abortado pelo usuário."
#             try:
#                 # print(dado.mostrarDados())
#                 getattr(banco, metodo_insercao)(dado)
#                 sucesso += 1
#             except Exception as e:
#                 falha += 1
#                 erros.append(str(e))
#                 logger.warning(f"Erro ao inserir {dado}: {str(e)}")

#         conn.commit()
#         banco.desconectar()
#         logger.info(
#             f"{nome} finalizado com sucesso. Inseridos: {sucesso}, Falhas: {falha}"
#         )
#         if falha:
#             return f"{nome}: {sucesso} inseridos, {falha} com erro.\nErros: {erros[:3]}"
#         return f"{nome}: Todos os {sucesso} registros inseridos com sucesso."

#     except Exception as e:
#         logger.error(f"Erro na etapa {nome}: {str(e)}", exc_info=True)
#         try:
#             if "conn" in locals():
#                 conn.rollback()
#         except:  # noqa: E722
#             pass
#         banco.desconectar()
#         escrever_linha_em_branco(logger)
#         return f"Erro fatal em {nome}: {str(e)}"


# def run_processos_selecionados(vars):
#     print("🔄 Executando...\n")
#     mensagens = []
#     executar_script_inicial()

#     if vars["coletar"].get():
#         coletor = Coletor(nivel=nivel_log)
#         coletor.collect_data()
#         mensagens.append("Coleta e extração concluídas.")

#     etapas = [
#         (
#             "empresas",
#             "Empresas",
#             "data_extraido/FCA/sucesso",
#             process_empresas,
#             BancoEmpresas,
#             "inserir_ou_atualizar_empresa",
#         ),
#         (
#             "ipe",
#             "Periódicos Eventuais",
#             "data_extraido/IPE/sucesso",
#             process_ipe,
#             BancoIPE,
#             "inserir_periodicos_eventuais",
#         ),
#         (
#             "fre",
#             "Formulários de Referência",
#             "data_extraido/FRE/sucesso",
#             process_fre,
#             BancoFRE,
#             "inserir_formulario_referencia",
#         ),
#         (
#             "parecer_demo",
#             "Parecer - Demonst. Financeiros",
#             "data_extraido/DFP/sucesso",
#             process_parecer_demo,
#             BancoParecerDemo,
#             "inserir_parecer_demonstrativo",
#         ),
#         (
#             "parecer_trim",
#             "Parecer - Inf. Trimestrais",
#             "data_extraido/ITR/sucesso",
#             process_parecer_trim,
#             BancoParecerTrim,
#             "inserir_parecer_trimestral",
#         ),
#     ]

#     for chave, nome, caminho, func, banco_cls, metodo in etapas:
#         if vars[chave].get():
#             msg = (
#                 executar_etapa(nome, caminho, func, banco_cls, metodo)
#                 or f"{nome}: Nenhuma ação executada."
#             )
#             mensagens.append(msg)

#     if vars["num_acoes"].get():
#         try:
#             escrever_linha_separador(logger)
#             logger.info("Iniciando etapa: Número de Ações")
#             dfp = process_num_acoes("data_extraido/DFP/sucesso", "DFP")
#             itr = process_num_acoes("data_extraido/ITR/sucesso", "ITR")
#             dados = dfp + itr
#             banco = BancoNumAcoes(db_path=CAMINHO_BANCO)
#             banco.conectar()
#             conn = banco.connection
#             conn.execute("BEGIN")
#             sucesso = falha = 0
#             erros = []

#             for dado in dados:
#                 if cancelar_evento.is_set():
#                     conn.rollback()
#                     banco.desconectar()
#                     mensagens.append("Número de Ações abortado.")
#                     break
#                 try:
#                     banco.inserir_numeros_acoes(dado)
#                     sucesso += 1
#                 except Exception as e:
#                     falha += 1
#                     erros.append(str(e))

#             conn.commit()
#             banco.desconectar()
#             msg = (
#                 f"Número de Ações: {sucesso} inseridos, {falha} com erro."
#                 if falha
#                 else f"Número de Ações: Todos os {sucesso} inseridos com sucesso."
#             )
#             mensagens.append(msg)
#         except Exception as e:
#             mensagens.append(f"Erro fatal em Número de Ações: {str(e)}")

#     if vars["dfp"].get():
#         banco = BancoDemostrativo(db_path=CAMINHO_BANCO)
#         banco.conectar()
#         conn = banco.connection
#         conn.execute("BEGIN")
#         dados = process_dfp("data_extraido/DFP/sucesso", banco)
#         sucesso = falha = 0
#         erros = []
#         for dado in dados:
#             if cancelar_evento.is_set():
#                 conn.rollback()
#                 banco.desconectar()
#                 mensagens.append("Demonstrativos Financeiros abortado.")
#                 break
#             try:
#                 banco.inserir_ou_atualizar_demonstrativo(dado)
#                 sucesso += 1
#             except Exception as e:
#                 falha += 1
#                 erros.append(str(e))
#         conn.commit()
#         banco.desconectar()
#         msg = (
#             f"Demonstrativos Financeiros: {sucesso} inseridos, {falha} com erro."
#             if falha
#             else f"Demonstrativos Financeiros: Todos os {sucesso} inseridos com sucesso."
#         )
#         mensagens.append(msg)

#     if vars["itr"].get():
#         banco = BancoInformacaoTri(db_path=CAMINHO_BANCO)
#         banco.conectar()
#         conn = banco.connection
#         conn.execute("BEGIN")
#         dados = process_itr("data_extraido/ITR/sucesso", banco)
#         sucesso = falha = 0
#         erros = []
#         for dado in dados:
#             if cancelar_evento.is_set():
#                 conn.rollback()
#                 banco.desconectar()
#                 mensagens.append("Informações Trimestrais abortado.")
#                 break
#             try:
#                 banco.inserir_ou_atualizar_informacao_tri(dado)
#                 sucesso += 1
#             except Exception as e:
#                 falha += 1
#                 erros.append(str(e))
#         conn.commit()
#         banco.desconectar()
#         msg = (
#             f"Informações Trimestrais: {sucesso} inseridos, {falha} com erro."
#             if falha
#             else f"Informações Trimestrais: Todos os {sucesso} inseridos com sucesso."
#         )
#         mensagens.append(msg)


#     if vars["num_acoes"].get():
#         try:
#             escrever_linha_separador(logger)
#             logger.info("Iniciando etapa: Número de Ações")
#             dfp = process_num_acoes("data_extraido/DFP/sucesso", "DFP")
#             itr = process_num_acoes("data_extraido/ITR/sucesso", "ITR")
#             dados = dfp + itr
#             banco = BancoNumAcoes(CAMINHO_BANCO, nivel_log)
#             banco.conectar()
#             conn = banco.connection
#             conn.execute("BEGIN")
#             sucesso = falha = 0
#             erros = []

#             for dado in dados:
#                 if cancelar_evento.is_set():
#                     conn.rollback()
#                     banco.desconectar()
#                     mensagens.append("Número de Ações abortado.")
#                     break
#                 try:
#                     banco.inserir_numeros_acoes(dado)
#                     sucesso += 1
#                 except Exception as e:
#                     falha += 1
#                     erros.append(str(e))

#             conn.commit()
#             banco.desconectar()
#             msg = (
#                 f"Número de Ações: {sucesso} inseridos, {falha} com erro."
#                 if falha
#                 else f"Número de Ações: Todos os {sucesso} inseridos com sucesso."
#             )
#             mensagens.append(msg)
#         except Exception as e:
#             mensagens.append(f"Erro fatal em Número de Ações: {str(e)}")

#     if vars["dfp"].get():
#         banco = BancoDemostrativo(CAMINHO_BANCO, nivel_log)
#         banco.conectar()
#         conn = banco.connection
#         conn.execute("BEGIN")
#         dados = process_dfp("data_extraido/DFP/sucesso", banco)
#         sucesso = falha = 0
#         erros = []
#         for dado in dados:
#             if cancelar_evento.is_set():
#                 conn.rollback()
#                 banco.desconectar()
#                 mensagens.append("Demonstrativos Financeiros abortado.")
#                 break
#             try:
#                 banco.inserir_ou_atualizar_demonstrativo(dado)
#                 sucesso += 1
#             except Exception as e:
#                 falha += 1
#                 erros.append(str(e))
#         conn.commit()
#         banco.desconectar()
#         msg = (
#             f"Demonstrativos Financeiros: {sucesso} inseridos, {falha} com erro."
#             if falha
#             else f"Demonstrativos Financeiros: Todos os {sucesso} inseridos com sucesso."
#         )
#         mensagens.append(msg)

#     if vars["itr"].get():
#         banco = BancoInformacaoTri(CAMINHO_BANCO, nivel_log)
#         banco.conectar()
#         conn = banco.connection
#         conn.execute("BEGIN")
#         dados = process_itr("data_extraido/ITR/sucesso", banco)
#         sucesso = falha = 0
#         erros = []
#         for dado in dados:
#             if cancelar_evento.is_set():
#                 conn.rollback()
#                 banco.desconectar()
#                 mensagens.append("Informações Trimestrais abortado.")
#                 break
#             try:
#                 banco.inserir_ou_atualizar_informacao_tri(dado)
#                 sucesso += 1
#             except Exception as e:
#                 falha += 1
#                 erros.append(str(e))
#         conn.commit()
#         banco.desconectar()
#         msg = (
#             f"Informações Trimestrais: {sucesso} inseridos, {falha} com erro."
#             if falha
#             else f"Informações Trimestrais: Todos os {sucesso} inseridos com sucesso."
#         )
#         mensagens.append(msg)

#     print("\n✅ Execução finalizada com sucesso.\n")
#     resumo_texto = "\n\n".join(mensagens)
#     print("===== RESUMO DA EXECUÇÃO =====")
#     print(resumo_texto)
#     with open("resumo_execucao.log", "w", encoding="utf-8") as f:
#         f.write(resumo_texto)


# if __name__ == "__main__":
#     args = configurar_argumentos()

#     if args.debug:
#         nivel_log = logging.DEBUG
#     elif args.verbose:
#         nivel_log = logging.INFO
#     else:
#         nivel_log = logging.WARNING

#     logger = configurar_logger(nivel=nivel_log)

#     try:
#         # Marca todas as etapas como True (simulando os checkboxes)
#         vars = {
#             chave: type("BoolVar", (), {"get": lambda self=True: True})()
#             for chave in ETIQUETAS.keys()
#         }
#         cancelar_evento.clear()
#         run_processos_selecionados(vars)
#     except KeyboardInterrupt:
#         cancelar_evento.set()
#         print("⏹ Execução cancelada pelo usuário.")
import os
import sys
import subprocess
import threading
import argparse
import logging
from utils.logger import (
    configurar_logger,
    escrever_linha_em_branco,
    escrever_linha_separador,
)

from collectors.coletor import Coletor

from service.empresas_service import process_csv_files as process_empresas
from repository.empresas_repository import ConexaoBanco as BancoEmpresas

from service.periodicos_eventuais_service import process_csv_files as process_ipe
from repository.periodicos_eventuais_repository import ConexaoBanco as BancoIPE

from service.formulario_referencia_service import process_csv_files as process_fre
from repository.formulario_referencia_repository import ConexaoBanco as BancoFRE

from service.parecer_demonstrativo_service import (
    process_csv_files as process_parecer_demo,
)
from repository.parecer_demonstrativo_repository import ConexaoBanco as BancoParecerDemo

from service.parecer_trimestral_service import process_csv_files as process_parecer_trim
from repository.parecer_trimestral_repository import ConexaoBanco as BancoParecerTrim

from service.numeros_acoes_service import process_csv_files as process_num_acoes
from repository.numeros_acoes_repository import ConexaoBanco as BancoNumAcoes

from service.demostrativo_financeiro_service import process_dfp_files as process_dfp
from repository.demostrativo_financeiro_repository import (
    ConexaoBanco as BancoDemostrativo,
)

from service.informacao_trimestral_service import process_dfp_files as process_itr
from repository.informacao_trimestral_repository import (
    ConexaoBanco as BancoInformacaoTri,
)

from service.especie_controle_service import (
    process_csv_files as process_especie_controle,
)
from repository.especie_controle_repository import ConexaoBanco as BancoEspecie_controle

from service.situacao_emissor_service import (
    process_csv_files as process_situacao_emissor,
)
from repository.situacao_emissor_repository import ConexaoBanco as BancoSituacao_emissor

from service.setor_atividade_service import process_csv_files as process_setor_atividade
from repository.setor_atividade_repository import ConexaoBanco as BancoSetor_atividade

from service.categoria_documento_service import (
    process_csv_files as process_categoria_documento,
)
from repository.categoria_documento_repository import (
    ConexaoBanco as BancoCategoria_documento,
)


def configurar_argumentos():
    parser = argparse.ArgumentParser(description="Processador CVM")
    parser.add_argument("-d", "--debug", action="store_true", help="Ativa modo debug")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Ativa modo verbose"
    )
    return parser.parse_args()


CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")
cancelar_evento = threading.Event()

ETIQUETAS = {
    "coletar": "Coletar e Extrair Dados",
    "empresas": "Empresas",
    "ipe": "Periódicos Eventuais",
    "fre": "Formulários de Referência",
    "parecer_demo": "Parecer - Demonst. Financeiros",
    "parecer_trim": "Parecer - Inf. Trimestrais",
    "num_acoes": "Número de Ações",
    "dfp": "Demonstrativos Financeiros",
    "itr": "Informações Trimestrais",
}


def executar_script_inicial():
    if os.path.exists(CAMINHO_BANCO):
        print("⚠️ Banco de dados já existe. Pulando execução do script.")
        return
    try:
        subprocess.run(
            [sys.executable, "sqlite-projeto/script-automatizar-sqlite.py"], check=True
        )
        print("✅ Script de automação executado com sucesso.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro no script inicial: {str(e)}", exc_info=True)
        print(f"❌ Erro ao executar o script:\n{str(e)}")
        sys.exit(1)


def executar_etapa(
    nome, base_path, processar, repositorio_cls, metodo_insercao, extras=None
):
    banco = None
    try:
        escrever_linha_separador(logger)
        logger.info(f"Iniciando etapa: {nome}")
        dados = processar(base_path, *extras) if extras else processar(base_path)
        banco = repositorio_cls(db_path=CAMINHO_BANCO)
        banco.conectar()
        conn = banco.connection
        conn.execute("BEGIN")

        sucesso, falha, erros = 0, 0, []
        for dado in dados:
            if cancelar_evento.is_set():
                conn.rollback()
                banco.desconectar()
                logger.warning(f"{nome} abortado com rollback.")
                return f"{nome} abortado pelo usuário."
            try:
                getattr(banco, metodo_insercao)(dado)
                sucesso += 1
            except Exception as e:
                falha += 1
                erros.append(str(e))
                logger.warning(f"Erro ao inserir {dado}: {str(e)}")

        conn.commit()
        banco.desconectar()
        logger.info(f"{nome} finalizado. Sucesso: {sucesso}, Falha: {falha}")
        if falha:
            return f"{nome}: {sucesso} inseridos, {falha} com erro. Erros: {erros[:3]}"
        return f"{nome}: Todos os {sucesso} registros inseridos com sucesso."

    except Exception as e:
        logger.error(f"Erro na etapa {nome}: {str(e)}", exc_info=True)
        if banco:
            try:
                banco.connection.rollback()
                banco.desconectar()
            except:  # noqa: E722
                pass
        escrever_linha_em_branco(logger)
        return f"Erro fatal em {nome}: {str(e)}"


def run_processos_selecionados(vars):
    # if vars["coletar"].get():
    #     coletor = Coletor(nivel=nivel_log)
    #     coletor.collect_data()
    #     print("📦 Coleta e extração concluídas.")
    print("🔄 Executando...\n")
    mensagens = []
    executar_script_inicial()

    tabelas_auxiliares = [
        (
            "Espécies de Controle",
            process_especie_controle,
            BancoEspecie_controle,
            "inserir_ou_ignorar_especie_controle",
        ),
        (
            "Situação do Emissor",
            process_situacao_emissor,
            BancoSituacao_emissor,
            "inserir_ou_ignorar_situacao_emissor",
        ),
        (
            "Setor de Atividade",
            process_setor_atividade,
            BancoSetor_atividade,
            "inserir_ou_ignorar_setor_atividade",
        ),
        (
            "Categoria de Documento",
            process_categoria_documento,
            BancoCategoria_documento,
            "inserir_ou_ignorar_categoria_documento",
        ),
    ]

    for nome, func, banco_cls, metodo in tabelas_auxiliares:
        msg = executar_etapa(nome, "data_extraido/FCA/sucesso", func, banco_cls, metodo)
        mensagens.append(msg)

    etapas = [
        (
            "empresas",
            "Empresas",
            "data_extraido/FCA/sucesso",
            process_empresas,
            BancoEmpresas,
            "inserir_ou_atualizar_empresa",
            [CAMINHO_BANCO],
        ),
        (
            "ipe",
            "Periódicos Eventuais",
            "data_extraido/IPE/sucesso",
            process_ipe,
            BancoIPE,
            "inserir_periodicos_eventuais",
            None,
        ),
        (
            "fre",
            "Formulários de Referência",
            "data_extraido/FRE/sucesso",
            process_fre,
            BancoFRE,
            "inserir_formulario_referencia",
            None,
        ),
        (
            "parecer_demo",
            "Parecer - Demonst. Financeiros",
            "data_extraido/DFP/sucesso",
            process_parecer_demo,
            BancoParecerDemo,
            "inserir_parecer_demonstrativo",
            None,
        ),
        (
            "parecer_trim",
            "Parecer - Inf. Trimestrais",
            "data_extraido/ITR/sucesso",
            process_parecer_trim,
            BancoParecerTrim,
            "inserir_parecer_trimestral",
            None,
        ),
    ]

    for chave, nome, caminho, func, banco_cls, metodo, extras in etapas:
        if vars[chave].get():
            msg = executar_etapa(nome, caminho, func, banco_cls, metodo, extras)
            mensagens.append(msg)

    if vars["num_acoes"].get():
        try:
            escrever_linha_separador(logger)
            logger.info("Iniciando etapa: Número de Ações")
            dfp = process_num_acoes("data_extraido/DFP/sucesso", "DFP")
            itr = process_num_acoes("data_extraido/ITR/sucesso", "ITR")
            dados = dfp + itr
            banco = BancoNumAcoes(db_path=CAMINHO_BANCO)
            banco.conectar()
            conn = banco.connection
            conn.execute("BEGIN")
            sucesso = falha = 0
            erros = []
            for dado in dados:
                if cancelar_evento.is_set():
                    conn.rollback()
                    banco.desconectar()
                    mensagens.append("Número de Ações abortado.")
                    break
                try:
                    banco.inserir_numeros_acoes(dado)
                    sucesso += 1
                except Exception as e:
                    falha += 1
                    erros.append(str(e))
            conn.commit()
            banco.desconectar()
            msg = (
                f"Número de Ações: {sucesso} inseridos, {falha} com erro."
                if falha
                else f"Número de Ações: Todos os {sucesso} inseridos com sucesso."
            )
            mensagens.append(msg)
        except Exception as e:
            mensagens.append(f"Erro fatal em Número de Ações: {str(e)}")

    # Etapa: Demonstrativos Financeiros
    if vars["dfp"].get():
        banco = BancoDemostrativo(db_path=CAMINHO_BANCO)
        banco.conectar()
        conn = banco.connection
        conn.execute("BEGIN")
        dados = process_dfp("data_extraido/DFP/sucesso", banco)
        sucesso = falha = 0
        erros = []
        for dado in dados:
            if cancelar_evento.is_set():
                conn.rollback()
                banco.desconectar()
                mensagens.append("Demonstrativos Financeiros abortado.")
                break
            try:
                banco.inserir_ou_atualizar_demonstrativo(dado)
                sucesso += 1
            except Exception as e:
                falha += 1
                erros.append(str(e))
        conn.commit()
        banco.desconectar()
        msg = (
            f"Demonstrativos Financeiros: {sucesso} inseridos, {falha} com erro."
            if falha
            else f"Demonstrativos Financeiros: Todos os {sucesso} inseridos com sucesso."
        )
        mensagens.append(msg)

    # Etapa: Informações Trimestrais
    if vars["itr"].get():
        banco = BancoInformacaoTri(db_path=CAMINHO_BANCO)
        banco.conectar()
        conn = banco.connection
        conn.execute("BEGIN")
        dados = process_itr("data_extraido/ITR/sucesso", banco)
        sucesso = falha = 0
        erros = []
        for dado in dados:
            if cancelar_evento.is_set():
                conn.rollback()
                banco.desconectar()
                mensagens.append("Informações Trimestrais abortado.")
                break
            try:
                banco.inserir_ou_atualizar_informacao_tri(dado)
                sucesso += 1
            except Exception as e:
                falha += 1
                erros.append(str(e))
        conn.commit()
        banco.desconectar()
        msg = (
            f"Informações Trimestrais: {sucesso} inseridos, {falha} com erro."
            if falha
            else f"Informações Trimestrais: Todos os {sucesso} inseridos com sucesso."
        )
        mensagens.append(msg)

    print("✅ Execução finalizada com sucesso.")
    resumo_texto = "\n\n".join(mensagens)
    print("===== RESUMO DA EXECUÇÃO =====")
    print(resumo_texto)
    with open("resumo_execucao.log", "w", encoding="utf-8") as f:
        f.write(resumo_texto)


if __name__ == "__main__":
    args = configurar_argumentos()

    if args.debug:
        nivel_log = logging.DEBUG
    elif args.verbose:
        nivel_log = logging.INFO
    else:
        nivel_log = logging.WARNING

    logger = configurar_logger(nivel=nivel_log)

    try:
        vars = {
            chave: type("BoolVar", (), {"get": lambda self=True: True})()
            for chave in ETIQUETAS.keys()
        }
        cancelar_evento.clear()
        run_processos_selecionados(vars)
    except KeyboardInterrupt:
        cancelar_evento.set()
        print("⏹ Execução cancelada pelo usuário.")
