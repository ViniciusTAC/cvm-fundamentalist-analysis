# # import os
# # import pandas as pd
# # import numpy as np
# # import xml.etree.ElementTree as ET
# # import requests
# # import zipfile

# # # Caminhos base
# # BASE_FOLDER = r"C:\\Users\\vinicius.costa\\OneDrive - Sitio Recanto do Queijo\\Documentos\\cvm-fundamentalist-analysis\\data_extraido\\ITR\\sucesso\\"
# # OUTPUT_FOLDER = 'CVM'
# # DOWNLOAD_FOLDER = 'Download_XML'

# # # Criar pastas necessárias
# # os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
# # os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# # # Função para baixar arquivos
# # def fazer_download_arquivo(url, nome_arquivo):
# #     try:
# #         print(f"Tentando baixar: {url}")
# #         print(nome_arquivo)
# #         response = requests.get(url, stream=True, timeout=60)
# #         response.raise_for_status()

# #         # Salvar o arquivo
# #         with open(nome_arquivo, 'wb') as arquivo:
# #             for chunk in response.iter_content(chunk_size=8192):
# #                 arquivo.write(chunk)

# #         # Verificar se o arquivo foi baixado completamente
# #         if os.path.exists(nome_arquivo) and os.path.getsize(nome_arquivo) > 0:
# #             print(f"Arquivo baixado: {nome_arquivo}")
# #             return True
# #         else:
# #             print(f"Falha ao baixar o arquivo {url}: Arquivo vazio.")
# #             return False
# #     except requests.exceptions.RequestException as e:
# #         print(f"Erro ao baixar o arquivo {url}: {e}")
# #         return False

# # # Função para processar arquivos ZIP e XML
# # def processar_arquivo(nome_arquivo, pasta_download):
# #     try:
# #         # Se for ZIP, extrair
# #         if zipfile.is_zipfile(nome_arquivo):
# #             with zipfile.ZipFile(nome_arquivo, 'r') as zip_ref:
# #                 zip_ref.extractall(pasta_download)
# #                 print(f"Arquivo ZIP extraído: {nome_arquivo}")
# #         else:
# #             print(f"Arquivo não é ZIP, processando como XML direto.")
# #         return True
# #     except Exception as e:
# #         print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")
# #         return False

# # # Função para processar arquivos XML
# # def processar_xml(caminho_xml):
# #     try:
# #         tree = ET.parse(caminho_xml)
# #         root = tree.getroot()
# #         acoes_on = root.find('.//CaptalIntegralizado/Ordinarias').text if root.find('.//CaptalIntegralizado/Ordinarias') is not None else None
# #         acoes_pn = root.find('.//CaptalIntegralizado/Preferenciais').text if root.find('.//CaptalIntegralizado/Preferenciais') is not None else None
# #         tes_on = root.find('.//Tesouraria/Ordinarias').text if root.find('.//Tesouraria/Ordinarias') is not None else None
# #         tes_pn = root.find('.//Tesouraria/Preferenciais').text if root.find('.//Tesouraria/Preferenciais') is not None else None
# #         return acoes_on, acoes_pn, tes_on, tes_pn
# #     except Exception as e:
# #         print(f"Erro ao processar XML {caminho_xml}: {e}")
# #         return None, None, None, None

# # # Função principal para processar os dados
# # def processar_csv_files(base_path):
# #     dados_finais = []
# #     for year_folder in os.listdir(base_path):
# #         year_path = os.path.join(base_path, year_folder)
# #         if not os.path.isdir(year_path):
# #             continue

# #         for file in os.listdir(year_path):
# #             if file.endswith(".csv") and file.startswith("itr_cia_aberta"):
# #                 file_path = os.path.join(year_path, file)

# #                 try:
# #                     # Carregar o CSV com o delimitador correto
# #                     df = pd.read_csv(file_path, encoding='latin1', delimiter=';', on_bad_lines='skip')

# #                     # Processar cada link de documento XML ou ZIP
# #                     df[['Acoes_ON', 'Acoes_PN', 'Tes_ON', 'Tes_PN']] = np.nan
# #                     for index, row in df.iterrows():
# #                         link_doc = row['LINK_DOC']
# #                         nome_arquivo_temp = os.path.join(DOWNLOAD_FOLDER, f"arquivo_{index}.zip")

# #                         if fazer_download_arquivo(link_doc, nome_arquivo_temp):
# #                             if processar_arquivo(nome_arquivo_temp, DOWNLOAD_FOLDER):
# #                                 arquivos_extracao = [arq for arq in os.listdir(DOWNLOAD_FOLDER) if arq.endswith('.xml')]
# #                                 if arquivos_extracao:
# #                                     caminho_xml = os.path.join(DOWNLOAD_FOLDER, arquivos_extracao[0])
# #                                     acoes_on, acoes_pn, tes_on, tes_pn = processar_xml(caminho_xml)
# #                                     df.loc[index, ['Acoes_ON', 'Acoes_PN', 'Tes_ON', 'Tes_PN']] = [acoes_on, acoes_pn, tes_on, tes_pn]

# #                         # Limpar arquivos temporários
# #                         for arquivo in os.listdir(DOWNLOAD_FOLDER):
# #                             os.remove(os.path.join(DOWNLOAD_FOLDER, arquivo))

# #                     dados_finais.append(df)

# #                 except pd.errors.ParserError as e:
# #                     print(f"Erro ao processar o arquivo {file_path}: {e}")
# #                 except UnicodeDecodeError as e:
# #                     print(f"Erro de codificação ao processar o arquivo {file_path}: {e}")

# #     # Consolidar os dados
# #     if dados_finais:
# #         df_consolidado = pd.concat(dados_finais, ignore_index=True)
# #         df_consolidado = df_consolidado.drop_duplicates()

# #         # Salvar o DataFrame final
# #         caminho_saida = os.path.join(OUTPUT_FOLDER, 'dados_consolidados.csv')
# #         df_consolidado.to_csv(caminho_saida, index=False)
# #         print(f"Dados consolidados salvos em {caminho_saida}")

# # # Executar o processamento com base nos dados existentes
# # processar_csv_files(BASE_FOLDER)


# from importlib.metadata import files
# import os
# import pandas as pd
# import numpy as np
# import xml.etree.ElementTree as ET
# import requests
# import zipfile

# # Caminhos base
# BASE_FOLDER = r"C:\\Users\\vinicius.costa\\OneDrive - Sitio Recanto do Queijo\\Documentos\\cvm-fundamentalist-analysis\\data_extraido\\ITR\\sucesso\\"
# OUTPUT_FOLDER = 'CVM'
# DOWNLOAD_FOLDER = 'Download_XML'

# # Criar pastas necessárias
# os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
# os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# # Função para baixar arquivos
# def fazer_download_arquivo(url, nome_arquivo):
#     try:
#         print(f"Tentando baixar: {url}")
#         response = requests.get(url, stream=True, timeout=60)
#         response.raise_for_status()

#         # Salvar o arquivo
#         with open(nome_arquivo, 'wb') as arquivo:
#             for chunk in response.iter_content(chunk_size=8192):
#                 arquivo.write(chunk)

#         # Verificar se o arquivo foi baixado completamente
#         if os.path.exists(nome_arquivo) and os.path.getsize(nome_arquivo) > 0:
#             print(f"Arquivo baixado: {nome_arquivo}")
#             return True
#         else:
#             print(f"Falha ao baixar o arquivo {url}: Arquivo vazio.")
#             return False
#     except requests.exceptions.RequestException as e:
#         print(f"Erro ao baixar o arquivo {url}: {e}")
#         return False

# # Função para extrair arquivos ZIP
# def extrair_arquivo_zip(caminho_zip, pasta_destino):
#     try:
#         with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
#             zip_ref.extractall(pasta_destino)
#             print(f"Arquivo ZIP extraído: {caminho_zip}")
#         return True
#     except Exception as e:
#         print(f"Erro ao extrair o arquivo ZIP {caminho_zip}: {e}")
#         return False

# # Função para processar arquivos XML
# def processar_xml(caminho_xml):
#     try:
#         tree = ET.parse(caminho_xml)
#         root = tree.getroot()
#         acoes_on = root.find('.//CaptalIntegralizado/Ordinarias').text if root.find('.//CaptalIntegralizado/Ordinarias') is not None else None
#         acoes_pn = root.find('.//CaptalIntegralizado/Preferenciais').text if root.find('.//CaptalIntegralizado/Preferenciais') is not None else None
#         tes_on = root.find('.//Tesouraria/Ordinarias').text if root.find('.//Tesouraria/Ordinarias') is not None else None
#         tes_pn = root.find('.//Tesouraria/Preferenciais').text if root.find('.//Tesouraria/Preferenciais') is not None else None
#         return acoes_on, acoes_pn, tes_on, tes_pn
#     except Exception as e:
#         print(f"Erro ao processar XML {caminho_xml}: {e}")
#         return None, None, None, None

# # Função principal para processar os dados
# def processar_csv_files(base_path):
#     dados_finais = []
#     for year_folder in os.listdir(base_path):
#         year_path = os.path.join(base_path, year_folder)
#         if not os.path.isdir(year_path):
#             continue

#         for file in os.listdir(year_path):
#             if file.endswith(".csv") and file.startswith("itr_cia_aberta"):
#                 file_path = os.path.join(year_path, file)

#                 try:
#                     # Carregar o CSV com o delimitador correto
#                     df = pd.read_csv(file_path, encoding='latin1', delimiter=';', on_bad_lines='skip')

#                     # Adicionar colunas para os dados processados
#                     df[['Acoes_ON', 'Acoes_PN', 'Tes_ON', 'Tes_PN']] = np.nan

#                     for index, row in df.iterrows():
#                         link_doc = row['LINK_DOC']
#                         nome_arquivo_temp = os.path.join(DOWNLOAD_FOLDER, f"arquivo_{index}.zip")

#                         # Baixar e processar arquivo ZIP
#                         if fazer_download_arquivo(link_doc, nome_arquivo_temp):
#                             if extrair_arquivo_zip(nome_arquivo_temp, DOWNLOAD_FOLDER):
#                                 arquivos_extracao = [arq for arq in os.listdir(DOWNLOAD_FOLDER) if arq.endswith('.xml')]
#                                 for arquivo_xml in arquivos_extracao:
#                                     caminho_xml = os.path.join(DOWNLOAD_FOLDER, arquivo_xml)
#                                     print(caminho_xml)
#                                     acoes_on, acoes_pn, tes_on, tes_pn = processar_xml(caminho_xml)
#                                     df.loc[index, ['Acoes_ON', 'Acoes_PN', 'Tes_ON', 'Tes_PN']] = [acoes_on, acoes_pn, tes_on, tes_pn]

#                         # Limpar arquivos temporários
#                         for arquivo in os.listdir(DOWNLOAD_FOLDER):
#                             os.remove(os.path.join(DOWNLOAD_FOLDER, arquivo))

#                     dados_finais.append(df)

#                 except pd.errors.ParserError as e:
#                     print(f"Erro ao processar o arquivo {file_path}: {e}")
#                 except UnicodeDecodeError as e:
#                     print(f"Erro de codificação ao processar o arquivo {file_path}: {e}")

#     # Consolidar os dados
#     if dados_finais:
#         df_consolidado = pd.concat(dados_finais, ignore_index=True)
#         df_consolidado = df_consolidado.drop_duplicates()

#         # Salvar o DataFrame final
#         caminho_saida = os.path.join(OUTPUT_FOLDER, 'dados_consolidados.csv')
#         df_consolidado.to_csv(caminho_saida, index=False)
#         print(f"Dados consolidados salvos em {caminho_saida}")

# # Executar o processamento com base nos dados existentes
# processar_csv_files(BASE_FOLDER)

# import os
# import xml.etree.ElementTree as ET

# # Altere este caminho para o seu diretório real SEM ASPAS
# pasta_xml = r'C:\Users\vinicius.costa\OneDrive - Sitio Recanto do Queijo\Documentos\cvm-fundamentalist-analysis\XML'

# # Listar todos os arquivos XML na pasta
# arquivos_xml = [arquivo for arquivo in os.listdir(pasta_xml) if arquivo.endswith('.xml')]

# # Processar cada arquivo XML
# for nome_arquivo in arquivos_xml:
#     caminho_completo = os.path.join(pasta_xml, nome_arquivo)
    
#     try:
#         # Fazer parsing do XML
#         tree = ET.parse(caminho_completo)
#         root = tree.getroot()
        
#         # Extrair dados
#         codigo_cvm = root.find('.//DadosEmpresa/CodigoCvm').text or 'N/A'
#         nome_empresa = root.find('.//DadosEmpresa/RazaoSocialEmpresa').text or 'N/A'
#         cnpj_empresa = root.find('.//DadosEmpresa/CnpjEmpresa').text or 'N/A'
#         data_referencia = root.find('.//DadosITR/DataReferencia').text or 'N/A'
#         acoes_on = root.find('.//CaptalIntegralizado/Ordinarias').text or 'N/A'
#         acoes_pn = root.find('.//CaptalIntegralizado/Preferenciais').text or 'N/A'
#         tes_on = root.find('.//Tesouraria/Ordinarias').text or 'N/A'
#         tes_pn = root.find('.//Tesouraria/Preferenciais').text or 'N/A'
        
#         # Exibir resultados
#         print(f'\nArquivo: {nome_arquivo}')
#         print('-' * 40)
#         print(f' Codigo CVM =  {codigo_cvm}')
#         print(f' Nome empresa =  {nome_empresa}')
#         print(f' CNPJ empresa =  {cnpj_empresa}')
#         print(f' Data Referencia =  {data_referencia}')
#         print(f' total de ações Acoes_ON =  {acoes_on}')
#         print(f' total de ações Acoes_PN =  {acoes_pn}')
#         print(f' total de ações Tes_ON =  {tes_on}')
#         print(f' total de ações Tes_PN =  {tes_pn}')
        
#     except Exception as e:
#         print(f'\nErro ao processar {nome_arquivo}: {str(e)}')

# print('\nProcessamento concluído!')

import os
import csv
import requests
import zipfile
from xml.etree import ElementTree as ET

# Diretórios e caminhos principais
base_path = r'C:\Users\vinicius.costa\OneDrive - Sitio Recanto do Queijo\Documentos\cvm-fundamentalist-analysis'
data_xml_path = os.path.join(base_path, 'data_xml')

# Garantir que o diretório principal exista
os.makedirs(data_xml_path, exist_ok=True)

# Localizar pastas com nome itr_cia_aberta_(ano)
sucesso_path = os.path.join(base_path, 'data_extraido', 'ITR', 'sucesso')
pastas_ano = [
    folder for folder in os.listdir(sucesso_path) if folder.startswith('itr_cia_aberta_')
]

if not pastas_ano:
    print("Nenhuma pasta 'itr_cia_aberta_(ano)' encontrada!")
    exit()

for pasta in pastas_ano:
    ano = pasta.split('_')[-1]  # Extrair o ano do nome da pasta
    pasta_ano_path = os.path.join(sucesso_path, pasta)
    xml_zip_path = os.path.join(data_xml_path, f'xml_zip_{ano}')
    output_csv_path = os.path.join(data_xml_path, f'dados_processados_{ano}.csv')

    # Garantir que as pastas específicas por ano existam
    os.makedirs(xml_zip_path, exist_ok=True)

    # Localizar o arquivo CSV dentro da pasta
    csv_file = None
    for file in os.listdir(pasta_ano_path):
        if file.startswith('itr_cia_aberta_') and file.endswith('.csv'):
            csv_file = os.path.join(pasta_ano_path, file)
            break

    if not csv_file:
        print(f"Arquivo CSV não encontrado na pasta '{pasta}'!")
        continue

    # Ler o arquivo CSV com delimitador correto (;)
    links = []
    with open(csv_file, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f, delimiter=';')
        print(f"Colunas disponíveis no arquivo CSV ({ano}):", reader.fieldnames)
        for row in reader:
            if 'LINK_DOC' in row:
                links.append(row['LINK_DOC'])
            else:
                print(f"A coluna 'LINK_DOC' não foi encontrada no arquivo CSV para o ano {ano}.")
                continue

    print(f"Encontrados {len(links)} links para download para o ano {ano}.")

    subset = links[:2] + links[-2:]
    for idx, link in enumerate(subset):
        try:
            print(f"Baixando arquivo {idx + 1}/{len(subset)} ({ano}): {link}")
            response = requests.get(link)
            if response.status_code == 200:
                zip_name = os.path.join(xml_zip_path, f'arquivo_{idx}.zip')
                with open(zip_name, 'wb') as zip_file:
                    zip_file.write(response.content)
                print(f"Arquivo ZIP {zip_name} baixado com sucesso.")
            else:
                print(f"Falha ao baixar o arquivo ({ano}): {link}. Status HTTP: {response.status_code}")
        except Exception as e:
            print(f"Erro ao baixar o arquivo ({ano}): {link}, erro: {e}")

    # Extrair os arquivos ZIP
    for file in os.listdir(xml_zip_path):
        if file.endswith('.zip'):
            zip_file_path = os.path.join(xml_zip_path, file)
            extract_path = os.path.join(xml_zip_path, file.replace('.zip', ''))
            os.makedirs(extract_path, exist_ok=True)
            try:
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                print(f"Arquivos extraídos em: {extract_path}")
            except Exception as e:
                print(f"Erro ao extrair o arquivo {zip_file_path}: {e}")

    # Processar os arquivos XML
    dados = []
    for root_dir, dirs, files in os.walk(xml_zip_path):
        for file in files:
            if file.endswith('.xml'):
                xml_file_path = os.path.join(root_dir, file)
                try:
                    tree = ET.parse(xml_file_path)
                    root = tree.getroot()

                    # Extrair os dados necessários
                    codigo_cvm = root.find('.//DadosEmpresa/CodigoCvm').text or 'N/A'
                    nome_empresa = root.find('.//DadosEmpresa/RazaoSocialEmpresa').text or 'N/A'
                    cnpj_empresa = root.find('.//DadosEmpresa/CnpjEmpresa').text or 'N/A'
                    data_referencia = root.find('.//DadosITR/DataReferencia').text or 'N/A'
                    acoes_on = root.find('.//CaptalIntegralizado/Ordinarias').text or 'N/A'
                    acoes_pn = root.find('.//CaptalIntegralizado/Preferenciais').text or 'N/A'
                    tes_on = root.find('.//Tesouraria/Ordinarias').text or 'N/A'
                    tes_pn = root.find('.//Tesouraria/Preferenciais').text or 'N/A'

                    # Salvar os dados em uma lista
                    dados.append({
                        'Codigo CVM': codigo_cvm,
                        'Nome Empresa': nome_empresa,
                        'CNPJ Empresa': cnpj_empresa,
                        'Data Referencia': data_referencia,
                        'Acoes ON': acoes_on,
                        'Acoes PN': acoes_pn,
                        'Tes ON': tes_on,
                        'Tes PN': tes_pn,
                    })

                except Exception as e:
                    print(f"Erro ao processar o arquivo XML {xml_file_path}: {e}")

    # Salvar os dados em um arquivo CSV
    with open(output_csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'Codigo CVM', 'Nome Empresa', 'CNPJ Empresa', 'Data Referencia',
            'Acoes ON', 'Acoes PN', 'Tes ON', 'Tes PN'
        ])
        writer.writeheader()
        writer.writerows(dados)

    print(f"Processamento concluído para o ano {ano}! Dados salvos em {output_csv_path}")


