import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
from utils.logger import logger, escrever_linha_em_branco, escrever_linha_separador
from collectors.coletor import Coletor

# Imports dos serviços e repositórios
# Cada serviço é responsável por processar arquivos CSV específicos
# Cada repositório é responsável por interagir com o banco de dados
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


# ---------------
from service.demostrativo_financeiro_service import process_dfp_files
from repository.demostrativo_financeiro_repository import ConexaoBanco as BancoDemostrativo

# Caminho para o banco de dados SQLite
CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")


# Função genérica para executar uma etapa do processo
# `nome`: Nome da etapa (ex.: "Empresas")
# `base_path`: Caminho base dos arquivos CSV
# `processar`: Função para processar os arquivos CSV
# `repositorio_cls`: Classe do repositório para interagir com o banco de dados
# `metodo_insercao`: Nome do método do repositório para inserir os dados
# `extras`: Parâmetros extras para a função de processamento (opcional)
def executar_etapa(nome, base_path, processar, repositorio_cls, metodo_insercao, extras=None):
    try:
        # Escreve um separador no log para organizar as mensagens
        escrever_linha_separador(logger)
        logger.info(f"Processo iniciado de cadastro/atualização de {nome}.")

        # Processa os arquivos CSV e obtém os dados
        dados = processar(base_path) if extras is None else processar(base_path, *extras)

        # Exibe os primeiros 3 registros processados no console (para depuração)
        for i in range(min(3, len(dados))):
            print(dados[i].mostrarDados() if hasattr(dados[i], 'mostrarDados') else dados[i])

        # Conecta ao banco de dados
        banco = repositorio_cls(db_path=CAMINHO_BANCO)
        banco.conectar()

        # Insere os dados no banco de dados (limite de 100 registros para evitar sobrecarga)
        for dado in dados[:100]:
            getattr(banco, metodo_insercao)(dado)

        # Desconecta do banco de dados
        banco.desconectar()

        logger.info(f"Processo de cadastro/atualização de {nome} finalizado com sucesso.")
    except Exception as e:
        # Registra erros no log
        logger.error(f"Erro durante o processo de cadastro/atualização de {nome}: {str(e)}", exc_info=True)
    # Escreve uma linha em branco no log para separar as mensagens
    escrever_linha_em_branco(logger)


def executar_script_inicial():
    # Inicializa o tkinter para poder usar messagebox
    root = tk.Tk()
    root.withdraw()

    db_path = os.path.join("sqlite-projeto", "cvm-dados.db")

    if os.path.exists(db_path):
        msg = "Banco de dados já existe. Pulando execução do script."
        print(msg)
        messagebox.showinfo("Banco de Dados", msg)
        return

    try:
        subprocess.run(
            [sys.executable, "sqlite-projeto/script-automatizar-sqlite.py"],
            check=True
        )
        print("Script de automação executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o script:", e)
        print("Arquivo com erro:", "sqlite-projeto/script-automatizar-sqlite.py")
        messagebox.showerror("Erro", f"❌ Erro ao executar o script:\n{str(e)}")
        sys.exit(1)


# Função principal do programa
def main():
    # print("Executando a função principal...")
    



    # # Instancia o coletor de dados
    # coletor = Coletor()

    # # Inicia o processo de coleta de dados
    # coletor.collect_data()

    # # Executa as etapas de processamento e inserção de dados para cada tipo de informação
    # executar_etapa("Empresas", os.path.join("data_extraido", "FCA", "sucesso"), process_empresas, BancoEmpresas, "inserir_ou_atualizar_empresa")
    # executar_etapa("IPE", os.path.join("data_extraido", "IPE", "sucesso"), process_ipe, BancoIPE, "inserir_periodicos_eventuais")
    # executar_etapa("FRE", os.path.join("data_extraido", "FRE", "sucesso"), process_fre, BancoFRE, "inserir_formulario_referencia")
    # executar_etapa("Parecer Demonstrativo", os.path.join("data_extraido", "DFP", "sucesso"), process_parecer_demo, BancoParecerDemo, "inserir_parecer_demonstrativo")
    # executar_etapa("Parecer Trimestral", os.path.join("data_extraido", "ITR", "sucesso"), process_parecer_trim, BancoParecerTrim, "inserir_parecer_trimestral")

    # # Processa e insere os dados de Número de Ações (DFP + ITR)
    # try:
    #     escrever_linha_separador(logger)
    #     logger.info("Processo iniciado de cadastro/atualização de Numero de Ações.")

    #     # Caminhos para os arquivos DFP e ITR
    #     dfp_base = os.path.join("data_extraido", "DFP", "sucesso")
    #     itr_base = os.path.join("data_extraido", "ITR", "sucesso")

    #     # Processa os arquivos de Número de Ações
    #     dfp = process_num_acoes(dfp_base, "DFP")
    #     itr = process_num_acoes(itr_base, "ITR")
    #     numeros_acoes = dfp + itr

    #     # Exibe os primeiros 3 registros processados no console
    #     for numero_acao in numeros_acoes[:3]:
    #         print(numero_acao)

    #     # Conecta ao banco de dados e insere os dados
    #     banco = BancoNumAcoes(db_path=CAMINHO_BANCO)
    #     banco.conectar()
    #     for numero_acao in numeros_acoes:
    #         banco.inserir_numeros_acoes(numero_acao)
    #     banco.desconectar()

    #     logger.info("Processo de cadastro/atualização de Numero de Ações finalizado com sucesso.")
    # except Exception as e:
    #     # Registra erros no log
    #     logger.error(f"Erro durante o processo de cadastro/atualização de Numero de Ações: {str(e)}", exc_info=True)
    # # Escreve uma linha em branco no log
    # escrever_linha_em_branco(logger)

    print("Iniciando processamento dos demonstrativos financeiros...")
    
    
    conexao = BancoDemostrativo(db_path=CAMINHO_BANCO)
    conexao.conectar()

    lista = process_dfp_files("data_extraido/DFP/sucesso", conexao)
    for a in lista[:3]:
        print(a.mostrarDados())
        
    for demonstrativo in lista[:3]:
        conexao.inserir_ou_atualizar_demonstrativo(demonstrativo)

    conexao.desconectar()
    print("Processamento concluído.")


# Ponto de entrada do programa
if __name__ == "__main__":
    # executar_script_inicial()
    main()
