import os
import pandas as pd
from datetime import datetime
from models.especie_controle import Especie_controle

def process_csv_files(base_path):
    descricao_unica_set = set()
    especie_controle_list = []

    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and file.startswith("fca_cia_aberta_geral"):
                file_path = os.path.join(year_path, file)

                try:
                    df = pd.read_csv(file_path, encoding='latin1', delimiter=';', on_bad_lines='skip')
                except (pd.errors.ParserError, UnicodeDecodeError) as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    continue

                for _, row in df.iterrows():
                    descricao = row.get('Especie_Controle_Acionario')
                    if pd.notnull(descricao) and descricao not in descricao_unica_set:
                        descricao_unica_set.add(descricao)
                        especie_controle = Especie_controle(_descricao=descricao)
                        especie_controle_list.append(especie_controle)

    return especie_controle_list

def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None
