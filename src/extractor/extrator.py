import zipfile
import os

def extrair_arquivo_zip(caminho_zip, diretorio_base):
    """
    Extrai os arquivos de um arquivo ZIP para uma estrutura organizada.

    Parâmetros:
        caminho_zip (str): Caminho para o arquivo ZIP.
        diretorio_base (str): Diretório base onde as categorias serão organizadas.
        categoria (str): Nome da categoria (por exemplo, "FCA").
    """
    # Extrai o nome do ano a partir do arquivo ZIP (assumindo que o nome do arquivo contém o ano)
    nome_zip = os.path.basename(caminho_zip)
    ano = nome_zip.split('.')[0]  # Ajuste conforme o padrão do nome dos arquivos

    # Cria o caminho completo para a categoria e o ano
    caminho_destino = os.path.join(diretorio_base, ano)
    os.makedirs(caminho_destino, exist_ok=True)

    # Extrai os arquivos para o destino
    with zipfile.ZipFile(caminho_zip, 'r') as arquivo_zip:
        arquivo_zip.extractall(caminho_destino)
        print(f'Arquivos extraídos para: {caminho_destino}')
