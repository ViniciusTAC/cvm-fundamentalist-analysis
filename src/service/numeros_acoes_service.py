import os
import pandas as pd
from datetime import datetime
import re

from models.numeros_acoes import Numeros_Acoes


def process_csv_files(base_path, fonte_dados):
    numero_acoes_list = []  # Lista para armazenar os dados processados
    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)

        # Verifica se é um diretório
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            # Verifica se o arquivo é um CSV relevante
            if file.endswith(".csv") and file.startswith(
                f"{str.lower(fonte_dados)}_cia_aberta_composicao_capital"
            ):
                file_path = os.path.join(year_path, file)

                try:
                    # Carrega o CSV com o delimitador correto
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

                # Processa cada linha do DataFrame
                for _, row in df.iterrows():
                    numero_acoes = Numeros_Acoes(
                        _fonte_dados=fonte_dados,                        _cnpj_companhia=re.sub(
                            r"\D", "", row.get("CNPJ_CIA") or ""
                        ),
                        # _cnpj_companhia=row.get("CNPJ_CIA", None),
                        _qtd_acoes_ordinarias_capital_integralizado=row.get(
                            "QT_ACAO_ORDIN_CAP_INTEGR", None
                        ),
                        _qtd_acoes_preferenciais_capital_integralizado=row.get(
                            "QT_ACAO_PREF_CAP_INTEGR", None
                        ),
                        _qtd_total_acoes_capital_integralizado=row.get(
                            "QT_ACAO_TOTAL_CAP_INTEGR", None
                        ),
                        _qtd_acoes_ordinarias_tesouro=row.get(
                            "QT_ACAO_ORDIN_TESOURO", None
                        ),
                        _qtd_acoes_preferenciais_tesouro=row.get(
                            "QT_ACAO_PREF_TESOURO", None
                        ),
                        _qtd_total_acoes_tesouro=row.get("QT_ACAO_TOTAL_TESOURO", None),
                        _versao=row.get("VERSAO", None),
                        _data_referencia=row.get("DT_REFER", None),
                        _mes=str(row.get("DT_REFER"))[5:7],
                        _ano=str(row.get("DT_REFER"))[:4],
                    )
                    # Adiciona os dados à lista
                    numero_acoes_list.append(numero_acoes)

    return numero_acoes_list


def parse_date(date_str):
    """Função para converter uma string de data em um objeto datetime.date."""
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print(f"Erro ao converter data: {date_str}")
        return None
