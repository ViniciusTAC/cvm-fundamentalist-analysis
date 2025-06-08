import os
import pandas as pd
from datetime import datetime
from models.periodicos_eventuais import Periodicos_eventuais
import sqlite3
import re


def carregar_mapas_auxiliares(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    def carregar_tabela(nome_tabela, nome_id_coluna):
        cursor.execute(f"SELECT {nome_id_coluna}, descricao FROM {nome_tabela}")
        return {desc.lower().strip(): id_ for id_, desc in cursor.fetchall()}

    mapas = {
        "categoria_documento": carregar_tabela(
            "categoria_documento", "id_categoria_doc"
        ),
        "assunto_prensa": carregar_tabela("assunto_prensa", "id_assunto"),
        "especie_documento_eventual": carregar_tabela(
            "especie_documento_eventual", "id_especie_eventual"
        ),
        "tipo_evento": carregar_tabela("tipo_evento", "id_tipo_evento"),
        "tipo_apresentacao_evento": carregar_tabela(
            "tipo_apresentacao_evento", "id_tipo_apres"
        ),
    }

    conn.close()
    return mapas


def process_csv_files(base_path, db_path):
    empresas_list = []
    mapas = carregar_mapas_auxiliares(db_path)
    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and file.startswith("ipe_cia_aberta"):
                file_path = os.path.join(year_path, file)

                try:
                    df = pd.read_csv(
                        file_path, encoding="latin1", delimiter=";", on_bad_lines="skip"
                    )
                except (pd.errors.ParserError, UnicodeDecodeError) as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    continue

                for _, row in df.iterrows():
                    periodicos_eventuais = Periodicos_eventuais(
                        _cnpj_companhia=re.sub(
                            r"\D", "", row.get("CNPJ_Companhia") or ""
                        ),
                        _id_assunto=mapas["assunto_prensa"].get(
                            str(row.get("Assunto")).lower().strip()
                        ),
                        _id_categoria_doc=mapas["categoria_documento"].get(
                            str(row.get("Categoria")).lower().strip()
                        ),
                        _id_especie_eventual=mapas["especie_documento_eventual"].get(
                            str(row.get("Especie")).lower().strip()
                        ),
                        _link_doc=row.get("Link_Download"),
                        _protocolo_entrega=row.get("Protocolo_Entrega"),
                        _id_tipo_evento=mapas["tipo_evento"].get(
                            str(row.get("Tipo")).lower().strip()
                        ),
                        _id_tipo_apres=mapas["tipo_apresentacao_evento"].get(
                            str(row.get("Tipo_Apresentacao")).lower().strip()
                        ),
                        _versao=row.get("Versao"),
                        _data_entrega=parse_date(row.get("Data_Entrega")),
                        _data_referencia=parse_date(row.get("Data_Referencia")),
                        _data_doc=datetime.now().date(),
                        _mes=row.get("Data_Referencia")[5:7]
                        if row.get("Data_Referencia")
                        else None,
                        _ano=row.get("Data_Referencia")[:4]
                        if row.get("Data_Referencia")
                        else None,
                    )
                    empresas_list.append(periodicos_eventuais)

    return empresas_list


def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
