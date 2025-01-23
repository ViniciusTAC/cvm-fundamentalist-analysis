import os
import pandas as pd
from datetime import datetime
from models.empresas import Empresas

def process_csv_files(base_path):
    empresas_list = []

    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and file.startswith("fca_cia_aberta_geral"):
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

                # Mapear cada linha para um objeto Empresas
                for _, row in df.iterrows():
                    empresa = Empresas(
                        _categoria_doc=row.get('Categoria_Registro_CVM'),
                        _codigo_cvm=row.get('Codigo_CVM'),
                        _cnpj_companhia=row.get('CNPJ_Companhia'),
                        _descricao_atividade=row.get('Descricao_Atividade'),
                        _especie_controle_acionario=row.get('Especie_Controle_Acionario'),
                        _identificador_documento=row.get('ID_Documento'),
                        _mes_encerramento_exercicio_social=row.get('Mes_Encerramento_Exercicio_Social'),
                        _nome_empresa=row.get('Nome_Empresarial'),
                        _nome_anterior_empresa=row.get('Nome_Empresarial_Anterior'),
                        _pagina_web=row.get('Pagina_Web'),
                        _pais_custodia_valores_mobiliarios=row.get('Pais_Custodia_Valores_Mobiliarios'),
                        _pais_origem=row.get('Pais_Origem'),
                        _setor_atividade=row.get('Setor_Atividade'),
                        _situacao_emissor=row.get('Situacao_Emissor'),
                        _situacao_registro_cvm=row.get('Situacao_Registro_CVM'),
                        _versao=row.get('Versao'),
                        _data_registro_cvm=row.get('Data_Registro_CVM'),
                        _data_nome_empresarial=row.get('Data_Nome_Empresarial'),
                        _data_categoria_registro_cvm=row.get('Data_Categoria_Registro_CVM'),
                        _data_situacao_registro_cvm=row.get('Data_Situacao_Registro_CVM'),
                        _data_constituicao=row.get('Data_Constituicao'),
                        _data_especie_controle_acionario=row.get('Data_Especie_Controle_Acionario'),
                        _data_referencia_documento=row.get('Data_Referencia'),
                        _data_situacao_emissor=row.get('Data_Situacao_Emissor'),
                        _data_alteracao_exercicio_social=row.get('Data_Alteracao_Exercicio_Social'),
                        _dia_encerramento_exercicio_social=row.get('Dia_Encerramento_Exercicio_Social'),
                        _data_doc=datetime.now().date(),
                        _mes_doc=row.get('Data_Referencia')[5:7],
                        _ano_doc=row.get('Data_Referencia')[:4]
                    )
                    empresas_list.append(empresa)
                    # print(empresa.mostrarDados())

    return empresas_list

def parse_date(date_str):
    if pd.isnull(date_str) or not date_str:
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None