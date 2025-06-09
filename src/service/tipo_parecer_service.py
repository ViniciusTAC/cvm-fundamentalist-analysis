import os
import re
import pandas as pd
from models.tipo_parecer import Tipo_parecer


def process_tipo_parecer(base_path, regex_arquivo, nome_campo):
    descricao_unica_set = set()
    tipo_parecer_list = []

    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and re.match(regex_arquivo, file):
                file_path = os.path.join(year_path, file)

                try:
                    df = pd.read_csv(
                        file_path, encoding="latin1", delimiter=";", on_bad_lines="skip"
                    )
                except (pd.errors.ParserError, UnicodeDecodeError) as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    continue

                for _, row in df.iterrows():
                    descricao = row.get(nome_campo)
                    if pd.notnull(descricao) and descricao not in descricao_unica_set:
                        descricao_unica_set.add(descricao)
                        tipo_parecer = Tipo_parecer(_descricao=descricao)
                        tipo_parecer_list.append(tipo_parecer)

    return tipo_parecer_list