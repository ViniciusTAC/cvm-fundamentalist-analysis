# # from datetime import datetime
# from collectors.coletor import Coletor

# from models.empresas import Empresas
# from parsers.base_parser import process_csv_files

# if __name__ == "__main__":
#     # Instancia o coletor
#     # Coletor = Coletor()

#     # Inicia o processo de coleta de dados
#     # Coletor.collect_data()

#     base_path = "data_extraido/FCA"
#     empresas = process_csv_files(base_path)
#     print(f"Total de empresas processadas: {len(empresas)}")


# from storage.database import ConexaoBanco
# from collectors.coletor_cvm import ColetorCVM
# from parsers.base_parser import MapeadorCVM

# def main():
#     # Configuração do banco
#     conexao = ConexaoBanco(host="localhost", database="cvm_dados", user="root", password="31415")
#     conexao.conectar()

#     # Download e extração de arquivos
#     coletor = ColetorCVM()
#     coletor.baixar_arquivo(
#         "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FCA/DADOS/fca_cia_aberta_2025.zip",
#         "dados_cvm/fca_cia_aberta_2025.zip"
#     )
#     coletor.extrair_arquivo("dados_cvm/fca_cia_aberta_2025.zip", "dados_cvm/extracao")

#     # Inserção de dados no banco
#     mapeador = MapeadorCVM(conexao)
#     dados_exemplo = [
#         {"codigo_cvm": "000001", "cnpj_companhia": "12345678000100", "nome_empresa": "Empresa Exemplo"}
#     ]
#     mapeador.inserir_dados("empresas", dados_exemplo)

#     conexao.desconectar()

# if __name__ == "__main__":
#     main()






from storage.database import ConexaoBanco
# from datetime import datetime
from collectors.coletor import Coletor
from parsers.base_parser import process_csv_files


def main():
    # # Instancia o coletor
    # coletor = Coletor()

    # # Inicia o processo de coleta de dados
    # coletor.collect_data()

    base_path = "data_extraido/FCA"
    empresas = process_csv_files(base_path)

    # for empresa in empresas:
    #     print(empresa.mostrarDados())

    # Conectar ao banco e salvar os dados
    banco = ConexaoBanco(host='localhost', database='cvm_dados', user='root', password='31415')
    banco.conectar()
    # for i in range(3):
    #     banco.inserir_empresa(empresas[i])
    for empresa in empresas:
        banco.inserir_empresa(empresa)
    banco.desconectar()

if __name__ == "__main__":
    main()
