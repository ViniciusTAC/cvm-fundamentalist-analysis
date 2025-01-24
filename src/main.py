from datetime import datetime
from collectors.coletor import Coletor
from parsers.empresas_service import process_csv_files
from storage.empresas_repository import ConexaoBanco

import os
# from parsers.periodicos_eventuais_service import process_csv_files
# from storage.periodicos_eventuais_repository import ConexaoBanco

def main():
    # # Instancia o coletor
    # coletor = Coletor()

    # Inicia o processo de coleta de dados
    # coletor.collect_data()

    
    base_path = os.path.join('data_extraido', 'FCA', 'sucesso')
    empresas = process_csv_files(base_path)

    for i in range(3):
        print(empresas[i].mostrarDados())

    # Conectar ao banco e salvar os dados
    banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

    banco.conectar()
    for empresa in empresas:
        banco.inserir_empresa(empresa)
    banco.desconectar()


    # base_path = os.path.join('data_extraido', 'IPE', 'sucesso')
    # periodicos_eventuais = process_csv_files(base_path)

    # for i in range(3):
    #     print(periodicos_eventuais[i].mostrarDados())
    

    # # Conectar ao banco e salvar os dados
    # banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

    # banco.conectar()
    # for periodico in periodicos_eventuais:
    #     banco.inserir_periodicos_eventuais(periodico)
    # banco.desconectar()


if __name__ == "__main__":
    main()
