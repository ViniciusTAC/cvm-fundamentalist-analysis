# import os
# import pandas as pd
# from datetime import datetime
# from models.formulario_referencia import Formulario_referencia

# def process_csv_files(base_path):
#     formulario_referencia_list = []
#     for year_folder in os.listdir(base_path):
#         year_path = os.path.join(base_path, year_folder)
#         if not os.path.isdir(year_path):
#             continue

#         for file in os.listdir(year_path):
#             if file.endswith(".csv") and file.startswith("fre_cia_aberta"):
#                 file_path = os.path.join(year_path, file)

#                 try:
#                     # Carregar o CSV com o delimitador correto
#                     df = pd.read_csv(file_path, encoding='latin1', delimiter=';', on_bad_lines='skip')
#                     print(data.head())
#                 except pd.errors.ParserError as e:
#                     print(f"Erro ao processar o arquivo {file_path}: {e}")
#                     continue
#                 except UnicodeDecodeError as e:
#                     print(f"Erro de codificação ao processar o arquivo {file_path}: {e}")
#                     continue

#                 # Mapear cada linha para um objeto Periodicos e Eventuais
#                 for _, row in df.iterrows():
#                     formulario_referencia = Formulario_referencia(
#                         _cnpj_companhia= row.get('CNPJ_CIA'),
#                         _categoria_doc= row.get('CATEG_DOC'),
#                         _denominacao_companhia= row.get('DENOM_CIA'),
#                         _id_doc= row.get('ID_DOC'),
#                         _link_doc= row.get('LINK_DOC'),
#                         _versao= row.get('VERSAO'),
#                         _data_recebimento_doc= row.get('DT_RECEB'),
#                         _data_referencia_doc= row.get('DT_REFER'),
#                         _data_doc=datetime.now().date(),
#                         _mes_doc=str(row.get('DT_REFER')[5:7]),
#                         _ano_doc=str(row.get('DT_REFER')[:4])
#                     )
#                     # print(formulario_referencia.mostrarDados())
#                     formulario_referencia_list.append(formulario_referencia)

#     return formulario_referencia_list

# def parse_date(date_str):
#     if pd.isnull(date_str) or not date_str:
#         return None
#     try:
#         return datetime.strptime(date_str, '%Y-%m-%d').date()
#     except ValueError:
#         return None

import os
import pandas as pd
from datetime import datetime
from models.formulario_referencia import Formulario_referencia

def process_csv_files(base_path):
    formulario_referencia_list = []
    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and file.startswith("fre_cia_aberta"):
                file_path = os.path.join(year_path, file)

                try:
                    # Carregar o CSV com o delimitador correto
                    df = pd.read_csv(file_path, encoding='latin1', delimiter=';', on_bad_lines='skip')
                    print(df.head())  # Certifique-se de que os dados foram carregados corretamente
                except pd.errors.ParserError as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    continue
                except UnicodeDecodeError as e:
                    print(f"Erro de codificação ao processar o arquivo {file_path}: {e}")
                    continue

                # Mapear cada linha para um objeto Formulario_referencia
                for _, row in df.iterrows():
                    dt_refer = row.get('DT_REFER')

                    # Garantir que 'DT_REFER' é uma string e tem o formato esperado
                    if dt_refer and isinstance(dt_refer, str) and len(dt_refer) >= 7:
                        _mes_doc = dt_refer[5:7]
                        _ano_doc = dt_refer[:4]
                    else:
                        _mes_doc = None
                        _ano_doc = None

                    formulario_referencia = Formulario_referencia(
                        _cnpj_companhia=row.get('CNPJ_CIA'),
                        _categoria_doc=row.get('CATEG_DOC'),
                        _denominacao_companhia=row.get('DENOM_CIA'),
                        _id_doc=row.get('ID_DOC'),
                        _link_doc=row.get('LINK_DOC'),
                        _versao=row.get('VERSAO'),
                        _data_recebimento_doc=row.get('DT_RECEB'),
                        _data_referencia_doc=dt_refer,
                        _data_doc=datetime.now().date(),
                        _mes_doc=_mes_doc,
                        _ano_doc=_ano_doc
                    )
                    # print(formulario_referencia.mostrarDados())
                    formulario_referencia_list.append(formulario_referencia)

    return formulario_referencia_list

def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None
