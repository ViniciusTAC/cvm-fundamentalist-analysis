# import os
# import pandas as pd
# from datetime import datetime
# from models.escala_monetaria import Escala_monetaria


# def process_csv_files(base_path):
#     descricao_unica_set = set()
#     escala_monetaria_list = []

#     for year_folder in os.listdir(base_path):
#         year_path = os.path.join(base_path, year_folder)
#         if not os.path.isdir(year_path):
#             continue

#         for file in os.listdir(year_path):
#             if file.endswith(".csv") and file.startswith("dfp_cia_aberta"):
#                 file_path = os.path.join(year_path, file)

#                 try:
#                     df = pd.read_csv(
#                         file_path, encoding="latin1", delimiter=";", on_bad_lines="skip"
#                     )
#                 except (pd.errors.ParserError, UnicodeDecodeError) as e:
#                     print(f"Erro ao processar o arquivo {file_path}: {e}")
#                     continue

#                 for _, row in df.iterrows():
#                     descricao = row.get("ESCALA_MOEDA")
#                     if pd.notnull(descricao) and descricao not in descricao_unica_set:
#                         descricao_unica_set.add(descricao)
#                         escala_monetaria = Escala_monetaria(
#                             _descricao=descricao
#                         )
#                         escala_monetaria_list.append(escala_monetaria)

#     return escala_monetaria_list


# def parse_date(date_str):
#     if pd.isnull(date_str) or not date_str:
#         return None
#     try:
#         return datetime.strptime(date_str, "%Y-%m-%d").date()
#     except ValueError:
#         return None

import os
import pandas as pd
from models.escala_monetaria import Escala_monetaria

def carregar_grupos_demonstrativo(cursor):
    cursor.execute("SELECT codigo_grupo_dfp, grupo_dfp FROM grupo_demonstrativo_financeiro")
    rows = cursor.fetchall()
    return {codigo.upper(): descricao for codigo, descricao in rows}

def carregar_planos_contas(cursor):
    cursor.execute("SELECT comportamento, codigo_conta FROM planos_contas")
    rows = cursor.fetchall()

    planos = {}
    for comportamento, codigo in rows:
        if comportamento not in planos:
            planos[comportamento] = []
        planos[comportamento].append(codigo)
    return planos

def identificar_comportamento(arquivo_nome, grupo_demostrativo):
    arquivo_nome = arquivo_nome.upper()
    for sigla in grupo_demostrativo:
        if sigla in arquivo_nome:
            return sigla[:3]  # BPA, BPP, DRE, DVA
    return None

def process_csv_files(base_path, conexao, campo="ESCALA_MOEDA"):
    cursor = conexao.connection.cursor()
    grupo_demostrativo = carregar_grupos_demonstrativo(cursor)
    planos_contas = carregar_planos_contas(cursor)

    valores_unicos = set()

    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if not file.endswith(".csv"):
                continue

            comportamento = identificar_comportamento(file, grupo_demostrativo)
            if comportamento is None or comportamento not in planos_contas:
                continue

            file_path = os.path.join(year_path, file)

            try:
                df = pd.read_csv(file_path, encoding="latin1", delimiter=";", on_bad_lines="skip")
            except (pd.errors.ParserError, UnicodeDecodeError) as e:
                print(f"[ERRO] {file_path}: {e}")
                continue

            contas_desejadas = planos_contas[comportamento]

            df_filtrado = df[
                df["CD_CONTA"].astype(str).isin(contas_desejadas)
                | df["DS_CONTA"].astype(str).isin(contas_desejadas)
            ]

            for valor in df_filtrado[campo].dropna().unique():
                valores_unicos.add(str(valor).strip())

    # Transformar os valores únicos em objetos Escala_monetaria
    return [Escala_monetaria(_descricao=valor) for valor in valores_unicos]

