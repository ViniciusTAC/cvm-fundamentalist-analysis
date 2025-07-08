import os
import zipfile

# Caminhos de origem e destino
pasta_zip = r"CIA_ABERTA"
pasta_destino = os.path.join(os.path.dirname(pasta_zip), "CIA_ABERTA_extraida")

# Percorrer a pasta de origem
for root, _, files in os.walk(pasta_zip):
    for file in files:
        if file.endswith(".zip"):
            caminho_zip = os.path.join(root, file)

            # Caminho relativo da subpasta em relação à raiz da pasta_zip
            caminho_relativo = os.path.relpath(root, pasta_zip)

            # Criar o caminho correspondente na pasta de destino
            destino_subpasta = os.path.join(pasta_destino, caminho_relativo)
            os.makedirs(destino_subpasta, exist_ok=True)

            # Extrair o conteúdo do ZIP nesse caminho
            try:
                with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                    zip_ref.extractall(destino_subpasta)
                print(f"Extraído: {file} para {destino_subpasta}")
            except zipfile.BadZipFile:
                print(f"Erro: Arquivo ZIP inválido - {caminho_zip}")
