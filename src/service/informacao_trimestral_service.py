import os
import pandas as pd
from datetime import datetime
from models.informacao_trimestral import Informacao_trimestral

# from models.planos_contas import PlanosContas  # Se quiser cruzar com o banco depois

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
    print("arquivo_nome: " + str(arquivo_nome))
    for sigla in grupo_demostrativo:
        if sigla in arquivo_nome:
            return sigla[:3]  # BPA, BPP, DRE, DVA
    return None


def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
    
def process_dfp_files(base_path, conexao):
    informacao_tri_list = []

    cursor = conexao.connection.cursor()
    grupo_demostrativo = carregar_grupos_demonstrativo(cursor)
    planos_contas = carregar_planos_contas(cursor)

    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if not file.endswith(".csv"):
                continue

            comportamento = identificar_comportamento(file, grupo_demostrativo)
            print("comportamento: " + str(comportamento))
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

            for _, row in df_filtrado.iterrows():
                informacao_tri = Informacao_trimestral(
                    _codigo_conta=row.get("CD_CONTA"),
                    _cnpj_companhia=row.get("CNPJ_CIA"),
                    _codigo_cvm=row.get("CD_CVM"),
                    _escala_monetaria=row.get("ESCALA_MOEDA"),
                    _grupo_dfp=row.get("GRUPO_DFP"),
                    _moeda=row.get("MOEDA"),
                    _ordem_exercicio=row.get("ORDEM_EXERC"),
                    _conta_fixa=row.get("CONTA_FIXA"),
                    _versao=row.get("VERSAO"),
                    _data_inicio_exercicio=parse_date(row.get("DT_INI_EXERC")),
                    _data_fim_exercicio=parse_date(row.get("DT_FIM_EXERC")),
                    _data_referencia_doc=parse_date(row.get("DT_REFER")),
                    _valor_conta=row.get("VL_CONTA"),
                    _data_doc=datetime.now().date(),
                    _mes_doc=str(row.get("DT_REFER"))[5:7] if row.get("DT_REFER") else None,
                    _ano_doc=str(row.get("DT_REFER"))[:4] if row.get("DT_REFER") else None
                )

                informacao_tri_list.append(informacao_tri)

    return informacao_tri_list

