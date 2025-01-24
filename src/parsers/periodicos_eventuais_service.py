import os
import pandas as pd
from datetime import datetime
from models.periodicos_eventuais import Periodicos_eventuais

def process_csv_files(base_path):
    empresas_list = []
    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and file.startswith("ipe_cia_aberta"):
                file_path = os.path.join(year_path, file)

                try:
                    # Carregar o CSV com o delimitador correto
                    df = pd.read_csv(file_path, encoding='latin1', delimiter=';', on_bad_lines='skip')
                except pd.errors.ParserError as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    continue
                except UnicodeDecodeError as e:
                    print(f"Erro de codificação ao processar o arquivo {file_path}: {e}")
                    continue

                # Mapear cada linha para um objeto Periodicos e Eventuais
                for _, row in df.iterrows():
                   
                    periodicos_eventuais = Periodicos_eventuais(
                        _cnpj_companhia= row.get('CNPJ_Companhia'),
                        _codigo_cvm= row.get('Codigo_CVM'),
                        _assunto= row.get('Assunto'),
                        _categoria_doc= row.get('Categoria'),
                        _especie= row.get('Especie'),
                        _link_doc= row.get('Link_Download'),
                        _nome_companhia= row.get('Nome_Companhia'),
                        _protocolo_entrega= row.get('Protocolo_Entrega'),
                        _tipo= row.get('Tipo'),
                        _tipo_apresentacao= row.get('Tipo_Apresentacao'),
                        _versao= row.get('Versao'),
                        _data_entrega_doc= row.get('Data_Entrega'),
                        _data_referencia_doc= row.get('Data_Referencia'),
                        _data_doc=datetime.now().date(),
                        _mes_doc=row.get('Data_Referencia')[5:7],
                        _ano_doc=row.get('Data_Referencia')[:4]
                    )
                    # print(periodicos_eventuais.mostrarDados())
                    empresas_list.append(periodicos_eventuais)

    return empresas_list

def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None