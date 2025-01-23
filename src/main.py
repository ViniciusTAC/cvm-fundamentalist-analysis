from storage.database import ConexaoBanco
from datetime import datetime
from collectors.coletor import Coletor
from parsers.base_parser import process_csv_files


def main():
    # Instancia o coletor
    coletor = Coletor()

    # Inicia o processo de coleta de dados
    coletor.collect_data()

    # base_path = "data_extraido/FCA"
    # empresas = process_csv_files(base_path)

    # # Conectar ao banco e salvar os dados
    # banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')

    # banco.conectar()
    # for empresa in empresas:
    #     banco.inserir_empresa(empresa)
    # banco.desconectar()

if __name__ == "__main__":
    main()
