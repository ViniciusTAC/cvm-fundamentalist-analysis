import os
import pandas as pd
from datetime import datetime
from models.tipo_relatorio_especial import Tipo_relatorio_especial


def process_csv_files(base_path):
    descricao_unica_set = set()
    tipo_relatorio_especial_list = []

    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and file.startswith("itr_cia_aberta_parecer"):
                file_path = os.path.join(year_path, file)

                try:
                    df = pd.read_csv(
                        file_path, encoding="latin1", delimiter=";", on_bad_lines="skip"
                    )
                except (pd.errors.ParserError, UnicodeDecodeError) as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    continue

                for _, row in df.iterrows():
                    descricao = row.get("TP_RELAT_ESP")
                    if pd.notnull(descricao) and descricao not in descricao_unica_set:
                        descricao_unica_set.add(descricao)
                        tipo_relatorio_especial = Tipo_relatorio_especial(
                            _descricao=descricao
                        )
                        tipo_relatorio_especial_list.append(tipo_relatorio_especial)

    return tipo_relatorio_especial_list


def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
