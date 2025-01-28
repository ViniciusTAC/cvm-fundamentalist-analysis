import os

from datetime import datetime
from collectors.coletor import Coletor

# Empresas ---------------------------------------------------------------------------------------------------------------------
# from parsers.empresas_service import process_csv_files
# from storage.empresas_repository import ConexaoBanco


# IPE ---------------------------------------------------------------------------------------------------------------------
# from parsers.periodicos_eventuais_service import process_csv_files
# from storage.periodicos_eventuais_repository import ConexaoBanco


# # FRE ---------------------------------------------------------------------------------------------------------------------
# from parsers.formulario_referencia_service import process_csv_files
# from storage.formulario_referencia_repository import ConexaoBanco

# # Parecer Demonstrativo ---------------------------------------------------------------------------------------------------------------------
# from parsers.parecer_demonstrativo_service import process_csv_files
# from storage.parecer_demonstrativo_repository import ConexaoBanco

# # Parecer Trimestral ---------------------------------------------------------------------------------------------------------------------
# from parsers.parecer_trimestral_service import process_csv_files
# from storage.parecer_trimestral_repository import ConexaoBanco


# Numero de açoes ---------------------------------------------------------------------------------------------------------------------
from parsers.numeros_acoes_service import process_csv_files
from storage.numeros_acoes_repository import ConexaoBanco

def main():
    # # Instancia o coletor
    # coletor = Coletor()

    # # Inicia o processo de coleta de dados
    # coletor.collect_data()

# Empresas ---------------------------------------------------------------------------------------------------------------------    
    # base_path = os.path.join('data_extraido', 'FCA', 'sucesso')
    # empresas = process_csv_files(base_path)

    # for i in range(3):
    #     print(empresas[i].mostrarDados())

    # # Conectar ao banco e salvar os dados
    # banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

    # banco.conectar()
    # for empresa in empresas:
    #     banco.inserir_empresa(empresa)
    # banco.desconectar()

# IPE ---------------------------------------------------------------------------------------------------------------------
    # periodicos_eventuais = process_csv_files(base_path)

    # for i in range(3):
    #     print(periodicos_eventuais[i].mostrarDados())
    

    # # Conectar ao banco e salvar os dados
    # banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

    # banco.conectar()
    # for periodico in periodicos_eventuais:
    #     banco.inserir_periodicos_eventuais(periodico)
    # banco.desconectar()
    
# # FRE ---------------------------------------------------------------------------------------------------------------------
#     base_path = os.path.join('data_extraido', 'FRE', 'sucesso')
#     formulario_referencias = process_csv_files(base_path)

#     for i in range(3):
#         print(formulario_referencias[i].mostrarDados())

#     # Conectar ao banco e salvar os dados
#     banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

#     banco.conectar()
#     for formulario_referencia in formulario_referencias[:3]:
#         banco.inserir_formulario_referencia(formulario_referencia)
#     banco.desconectar()


# # Parecer Demonstrativo ---------------------------------------------------------------------------------------------------------------------
#     base_path = os.path.join('data_extraido', 'DFP', 'sucesso')
#     parecer_demonstrativos = process_csv_files(base_path)

#     for i in range(3):
#         print(parecer_demonstrativos[i].mostrarDados())

#     # Conectar ao banco e salvar os dados
#     banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

#     banco.conectar()
#     for parecer_demonstrativo in parecer_demonstrativos[:3]:
#         banco.inserir_parecer_demonstrativo(parecer_demonstrativo)
#     banco.desconectar()


# # Parecer Trimestral ---------------------------------------------------------------------------------------------------------------------
#     base_path = os.path.join('data_extraido', 'ITR', 'sucesso')
#     parecer_trimestrals = process_csv_files(base_path)

#     for parecer_trimestral in parecer_trimestrals[:3]:
#         print(parecer_trimestral.mostrarDados())

#     # Conectar ao banco e salvar os dados
#     banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

#     banco.conectar()
#     for parecer_trimestral in parecer_trimestrals[:3]:
#         banco.inserir_parecer_trimestral(parecer_trimestral)
#     banco.desconectar()

# Numero de Açoes ---------------------------------------------------------------------------------------------------------------------
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

    # Conectar ao banco e salvar os dados
    banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

    banco.conectar()
    for numero_acao in numeros_acoes:
        banco.inserir_numeros_acoes(numero_acao)
    banco.desconectar()

if __name__ == "__main__":
    main()
