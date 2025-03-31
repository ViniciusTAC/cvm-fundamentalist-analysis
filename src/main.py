import os

from datetime import datetime
from collectors.coletor import Coletor
from utils.logger import logger, escrever_linha_em_branco, escrever_linha_separador

# Empresas ---------------------------------------------------------------------------------------------------------------------
from service.empresas_service import process_csv_files
from repository.empresas_repository import ConexaoBanco


# IPE ---------------------------------------------------------------------------------------------------------------------
from service.periodicos_eventuais_service import process_csv_files
from repository.periodicos_eventuais_repository import ConexaoBanco


# FRE ---------------------------------------------------------------------------------------------------------------------
from service.formulario_referencia_service import process_csv_files
from repository.formulario_referencia_repository import ConexaoBanco

# Parecer Demonstrativo ---------------------------------------------------------------------------------------------------------------------
from service.parecer_demonstrativo_service import process_csv_files
from repository.parecer_demonstrativo_repository import ConexaoBanco

# Parecer Trimestral ---------------------------------------------------------------------------------------------------------------------
from service.parecer_trimestral_service import process_csv_files
from repository.parecer_trimestral_repository import ConexaoBanco


## Numero de açoes ---------------------------------------------------------------------------------------------------------------------
from service.numeros_acoes_service import process_csv_files
from repository.numeros_acoes_repository import ConexaoBanco


def main():
    try:
        escrever_linha_separador(logger)
        logger.info("Processo iniciado de cadastro/atualização de Empresas.")
        base_path = os.path.join("data_extraido", "FCA", "sucesso")
        empresas = process_csv_files(base_path)

        # Exibe alguns registros para verificação
        for i in range(min(3, len(empresas))):
            print(empresas[i].mostrarDados())

        # Caminho do arquivo SQLite
        caminho_banco = os.path.join(
            "sqlite-projeto", "cvm-dados.db"
        )  # Ex: pasta 'data', arquivo 'cvm_dados.db'
        banco = ConexaoBanco(db_path=caminho_banco)

        banco.conectar()
        for empresa in empresas:
            banco.inserir_ou_atualizar_empresa(empresa)
        banco.desconectar()

        logger.info(
            "Processo de cadastro/atualização de Empresas finalizado com sucesso."
        )
    except Exception as e:
        logger.error(
            f"Erro durante o processo de cadastro/atualização de Empresas: {str(e)}",
            exc_info=True,
        )

    escrever_linha_em_branco(logger)


# IPE ---------------------------------------------------------------------------------------------------------------------
    try:
        escrever_linha_separador(logger)
        logger.info("Processo iniciado de cadastro/atualização de IPE (Periódicos e Eventuais).")

        base_path = os.path.join("data_extraido", "IPE", "sucesso")
        periodicos_eventuais = process_csv_files(base_path)

        for i in range(min(3, len(periodicos_eventuais))):
            print(periodicos_eventuais[i].mostrarDados())

        # Caminho do arquivo SQLite
        caminho_banco = os.path.join("sqlite-projeto", "cvm-dados.db")
        banco = ConexaoBanco(db_path=caminho_banco)

        banco.conectar()
        for periodico in periodicos_eventuais:
            banco.inserir_periodicos_eventuais(periodico)
        banco.desconectar()

        logger.info("Processo de cadastro/atualização de IPE finalizado com sucesso.")
    except Exception as e:
        logger.error(
            f"Erro durante o processo de cadastro/atualização de IPE: {str(e)}",
            exc_info=True,
        )

    escrever_linha_em_branco(logger)


# FRE ---------------------------------------------------------------------------------------------------------------------
    try:
        escrever_linha_separador(logger)
        logger.info("Processo iniciado de cadastro/atualização de FRE (Formulário de Referência).")

        base_path = os.path.join("data_extraido", "FRE", "sucesso")
        formulario_referencias = process_csv_files(base_path)

        for i in range(min(3, len(formulario_referencias))):
            print(formulario_referencias[i].mostrarDados())

        # Caminho do arquivo SQLite
        caminho_banco = os.path.join("sqlite-projeto", "cvm-dados.db")
        banco = ConexaoBanco(db_path=caminho_banco)

        banco.conectar()
        for formulario_referencia in formulario_referencias:
            banco.inserir_formulario_referencia(formulario_referencia)
        banco.desconectar()

        logger.info("Processo de cadastro/atualização de FRE finalizado com sucesso.")
    except Exception as e:
        logger.error(
            f"Erro durante o processo de cadastro/atualização de FRE: {str(e)}",
            exc_info=True,
        )

    escrever_linha_em_branco(logger)


# Parecer Demonstrativo ---------------------------------------------------------------------------------------------------------------------
    try:
        escrever_linha_separador(logger)
        logger.info("Processo iniciado de cadastro/atualização de Parecer Demonstrativo.")

        base_path = os.path.join("data_extraido", "DFP", "sucesso")
        parecer_demonstrativos = process_csv_files(base_path)

        for i in range(min(3, len(parecer_demonstrativos))):
            print(parecer_demonstrativos[i].mostrarDados())

        # Caminho do arquivo SQLite
        caminho_banco = os.path.join("sqlite-projeto", "cvm-dados.db")
        banco = ConexaoBanco(db_path=caminho_banco)

        banco.conectar()
        for parecer_demonstrativo in parecer_demonstrativos[:3]:
            banco.inserir_parecer_demonstrativo(parecer_demonstrativo)
        banco.desconectar()

        logger.info("Processo de cadastro/atualização de Parecer Demonstrativo finalizado com sucesso.")
    except Exception as e:
        logger.error(
            f"Erro durante o processo de cadastro/atualização de Parecer Demonstrativo: {str(e)}",
            exc_info=True,
        )

    escrever_linha_em_branco(logger)
    


# Parecer Trimestral ---------------------------------------------------------------------------------------------------------------------
    try:
        escrever_linha_separador(logger)
        logger.info("Processo iniciado de cadastro/atualização de Parecer Trimestral.")

        base_path = os.path.join('data_extraido', 'ITR', 'sucesso')
        parecer_trimestrals = process_csv_files(base_path)

        for parecer_trimestral in parecer_trimestrals[:3]:
            print(parecer_trimestral.mostrarDados())

        # Caminho do arquivo SQLite
        caminho_banco = os.path.join("sqlite-projeto", "cvm-dados.db")
        banco = ConexaoBanco(db_path=caminho_banco)

        banco.conectar()
        for parecer_trimestral in parecer_trimestrals[:3]:
            banco.inserir_parecer_trimestral(parecer_trimestral)
        banco.desconectar()

        logger.info("Processo de cadastro/atualização de Parecer Trimestral finalizado com sucesso.")
    except Exception as e:
        logger.error(
            f"Erro durante o processo de cadastro/atualização de Parecer Trimestral: {str(e)}",
            exc_info=True,
        )

    escrever_linha_em_branco(logger)
    

## Numero de Açoes ---------------------------------------------------------------------------------------------------------------------

    try:
        escrever_linha_separador(logger)
        logger.info("Processo iniciado de cadastro/atualização de Numero de Ações.")

        # Processa os arquivos de ambas as pastas
        dfp_base_path = os.path.join('data_extraido', 'DFP', 'sucesso')
        itr_base_path = os.path.join('data_extraido', 'ITR', 'sucesso')

        dfp_numero_acoes = process_csv_files(dfp_base_path, "DFP")
        itr_numero_acoes = process_csv_files(itr_base_path, "ITR")

        # Combina os resultados de DFP e ITR
        numeros_acoes = dfp_numero_acoes + itr_numero_acoes

        # Exibe os primeiros 3 resultados
        for numero_acao in numeros_acoes[:3]:
            print(numero_acao)

        # Caminho do arquivo SQLite
        caminho_banco = os.path.join("sqlite-projeto", "cvm-dados.db")
        banco = ConexaoBanco(db_path=caminho_banco)

        banco.conectar()
        banco.conectar()
        for numero_acao in numeros_acoes:
            banco.inserir_numeros_acoes(numero_acao)
        banco.desconectar()

        logger.info("Processo de cadastro/atualização de Numero de Ações finalizado com sucesso.")
    except Exception as e:
        logger.error(
            f"Erro durante o processo de cadastro/atualização de Numero de Ações: {str(e)}",
            exc_info=True,
        )

    escrever_linha_em_branco(logger)

if __name__ == "__main__":
    main()
