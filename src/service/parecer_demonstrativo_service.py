import os
import pandas as pd
from datetime import datetime
from models.parecer_demonstrativo import Parecer_demonstrativo
import sqlite3
import re


def carregar_mapas_auxiliares(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    def carregar_tabela(nome_tabela, nome_id_coluna):
        cursor.execute(f"SELECT {nome_id_coluna}, descricao FROM {nome_tabela}")
        return {desc.lower().strip(): id_ for id_, desc in cursor.fetchall()}

    mapas = {
        "tipo_parecer": carregar_tabela("tipo_parecer", "id_tipo_parecer"),
        "tipo_relatorio_auditor": carregar_tabela(
            "tipo_relatorio_auditor", "id_tipo_rel_auditor"
        ),
    }

    conn.close()
    return mapas


def process_csv_files(base_path, db_path):
    parecer_demonstrativo_list = []
    mapas = carregar_mapas_auxiliares(db_path)
    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and file.startswith("dfp_cia_aberta_parecer"):
                file_path = os.path.join(year_path, file)

                try:
                    # Carregar o CSV com o delimitador correto
                    df = pd.read_csv(
                        file_path, encoding="latin1", delimiter=";", on_bad_lines="skip"
                    )
                except pd.errors.ParserError as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    continue
                except UnicodeDecodeError as e:
                    print(
                        f"Erro de codificação ao processar o arquivo {file_path}: {e}"
                    )
                    continue

                # Mapear cada linha para um objeto Periodicos e Eventuais
                for _, row in df.iterrows():
                    parecer_demonstrativo = Parecer_demonstrativo(
                        _cnpj_companhia=re.sub(r"\D", "", row.get("CNPJ_CIA") or ""),
                        _num_linha_parecer_declaracao=row.get("NUM_ITEM_PARECER_DECL"),
                        _id_tipo_parecer=mapas["tipo_parecer"].get(
                            str(row.get("TP_PARECER_DECL")).lower().strip()
                        ),
                        _id_tipo_rel_auditor=mapas["tipo_relatorio_auditor"].get(
                            str(row.get("TP_RELAT_AUD")).lower().strip()
                        ),
                        _texto_parecer_declaracao=row.get("TXT_PARECER_DECL"),
                        _versao=row.get("VERSAO"),
                        _data_referencia_doc=row.get("DT_REFER"),
                        _mes=str(row.get("DT_REFER"))[5:7],
                        _ano=str(row.get("DT_REFER"))[:4],
                    )
                    # print(parecer_demonstrativo.mostrarDados())
                    parecer_demonstrativo_list.append(parecer_demonstrativo)

    return parecer_demonstrativo_list


def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
