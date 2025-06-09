import os
import re
import pandas as pd
from datetime import datetime
from models.formulario_referencia import Formulario_referencia
import sqlite3
import re


def carregar_mapas_auxiliares(conexao):
    cursor = conexao.connection.cursor()

    def carregar_tabela(nome_tabela, nome_id_coluna):
        cursor.execute(f"SELECT {nome_id_coluna}, descricao FROM {nome_tabela}")
        return {desc.lower().strip(): id_ for id_, desc in cursor.fetchall()}

    mapas = {
        "categoria_documento": carregar_tabela(
            "categoria_documento", "id_categoria_doc"
        ),
    }

    # conn.close()
    return mapas


def process_csv_files(base_path, conexao):
    formulario_referencia_list = []
    mapas = carregar_mapas_auxiliares(conexao)

    # Expressão regular para nome do arquivo no formato: fre_cia_aberta_<ano>.csv
    padrao_nome_arquivo = re.compile(r"^fre_cia_aberta_\d{4}\.csv$")

    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if not padrao_nome_arquivo.match(file):
                continue  # Pula arquivos que não seguem o padrão

            file_path = os.path.join(year_path, file)

            try:
                df = pd.read_csv(
                    file_path, encoding="latin1", delimiter=";", on_bad_lines="skip"
                )
            except pd.errors.ParserError as e:
                print(f"Erro ao processar o arquivo {file_path}: {e}")
                continue
            except UnicodeDecodeError as e:
                print(f"Erro de codificação ao processar o arquivo {file_path}: {e}")
                continue

            for _, row in df.iterrows():
                formulario_referencia = Formulario_referencia(
                    _cnpj_companhia=re.sub(r"\D", "", row.get("CNPJ_CIA") or ""),
                    _id_categoria_doc=mapas["categoria_documento"].get(
                        str(row.get("CATEG_DOC")).lower().strip()
                    ),
                    _id_doc=row.get("ID_DOC"),
                    _link_doc=row.get("LINK_DOC"),
                    _versao=row.get("VERSAO"),
                    _data_recebimento=row.get("DT_RECEB"),
                    _data_referencia=row.get("DT_REFER"),
                    _data_doc=datetime.now().date(),
                    _mes=str(row.get("DT_REFER"))[5:7]
                    if pd.notnull(row.get("DT_REFER"))
                    else None,
                    _ano=str(row.get("DT_REFER"))[:4]
                    if pd.notnull(row.get("DT_REFER"))
                    else None,
                )

                formulario_referencia_list.append(formulario_referencia)

    return formulario_referencia_list


def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
