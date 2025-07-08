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


