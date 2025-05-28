import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

# URL do diretório
url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FCA/DADOS/'

# Requisição HTTP
response = requests.get(url)
response.raise_for_status()

# Análise HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Regex para encontrar arquivos com data e tamanho
pattern = re.compile(r'<a href="(fca_cia_aberta_\d{4}\.zip)">.*?</a>\s+(\d{2}-\w{3}-\d{4} \d{2}:\d{2})\s+([\dKMG]+)')

matches = pattern.findall(response.text)

# Meses abreviados em inglês para conversão
for nome, data_str, tamanho in matches:
    # Converte a data para datetime e depois formata como ISO 8601
    dt = datetime.strptime(data_str, "%d-%b-%Y %H:%M")
    data_formatada = dt.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Nome do arquivo: {nome}")
    print(f"Data de modificação: {data_formatada}")
    print(f"Tamanho: {tamanho}")
    print(f"URL: {url}{nome}")
    print("-" * 60)
