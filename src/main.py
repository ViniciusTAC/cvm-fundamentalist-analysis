import os
from utils.logger import logger, escrever_linha_em_branco, escrever_linha_separador
from collectors.coletor import Coletor

# Imports dos serviços e repositórios
from service.empresas_service import process_csv_files as process_empresas
from repository.empresas_repository import ConexaoBanco as BancoEmpresas

from service.periodicos_eventuais_service import process_csv_files as process_ipe
from repository.periodicos_eventuais_repository import ConexaoBanco as BancoIPE

from service.formulario_referencia_service import process_csv_files as process_fre
from repository.formulario_referencia_repository import ConexaoBanco as BancoFRE

from service.parecer_demonstrativo_service import process_csv_files as process_parecer_demo
from repository.parecer_demonstrativo_repository import ConexaoBanco as BancoParecerDemo

from service.parecer_trimestral_service import process_csv_files as process_parecer_trim
from repository.parecer_trimestral_repository import ConexaoBanco as BancoParecerTrim

from service.numeros_acoes_service import process_csv_files as process_num_acoes
from repository.numeros_acoes_repository import ConexaoBanco as BancoNumAcoes


CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")


def executar_etapa(nome, base_path, processar, repositorio_cls, metodo_insercao, extras=None):
    try:
        escrever_linha_separador(logger)
        logger.info(f"Processo iniciado de cadastro/atualização de {nome}.")

        dados = processar(base_path) if extras is None else processar(base_path, *extras)

        for i in range(min(3, len(dados))):
            print(dados[i].mostrarDados() if hasattr(dados[i], 'mostrarDados') else dados[i])

        banco = repositorio_cls(db_path=CAMINHO_BANCO)
        banco.conectar()
        for dado in dados[:100]:
            getattr(banco, metodo_insercao)(dado)
        banco.desconectar()

        logger.info(f"Processo de cadastro/atualização de {nome} finalizado com sucesso.")
    except Exception as e:
        logger.error(f"Erro durante o processo de cadastro/atualização de {nome}: {str(e)}", exc_info=True)
    escrever_linha_em_branco(logger)



def main():
    # Instancia o coletor
    coletor = Coletor()

    # Inicia o processo de coleta de dados
    coletor.collect_data()

    executar_etapa("Empresas", os.path.join("data_extraido", "FCA", "sucesso"), process_empresas, BancoEmpresas, "inserir_ou_atualizar_empresa")
    executar_etapa("IPE", os.path.join("data_extraido", "IPE", "sucesso"), process_ipe, BancoIPE, "inserir_periodicos_eventuais")
    executar_etapa("FRE", os.path.join("data_extraido", "FRE", "sucesso"), process_fre, BancoFRE, "inserir_formulario_referencia")
    executar_etapa("Parecer Demonstrativo", os.path.join("data_extraido", "DFP", "sucesso"), process_parecer_demo, BancoParecerDemo, "inserir_parecer_demonstrativo")
    executar_etapa("Parecer Trimestral", os.path.join("data_extraido", "ITR", "sucesso"), process_parecer_trim, BancoParecerTrim, "inserir_parecer_trimestral")

    # Número de Ações (DFP + ITR)
    try:
        escrever_linha_separador(logger)
        logger.info("Processo iniciado de cadastro/atualização de Numero de Ações.")

        dfp_base = os.path.join("data_extraido", "DFP", "sucesso")
        itr_base = os.path.join("data_extraido", "ITR", "sucesso")

        dfp = process_num_acoes(dfp_base, "DFP")
        itr = process_num_acoes(itr_base, "ITR")
        numeros_acoes = dfp + itr

        for numero_acao in numeros_acoes[:3]:
            print(numero_acao)

        banco = BancoNumAcoes(db_path=CAMINHO_BANCO)
        banco.conectar()
        for numero_acao in numeros_acoes:
            banco.inserir_numeros_acoes(numero_acao)
        banco.desconectar()

        logger.info("Processo de cadastro/atualização de Numero de Ações finalizado com sucesso.")
    except Exception as e:
        logger.error(f"Erro durante o processo de cadastro/atualização de Numero de Ações: {str(e)}", exc_info=True)
    escrever_linha_em_branco(logger)



if __name__ == "__main__":
    main()
