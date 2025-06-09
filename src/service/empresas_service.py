import os
import pandas as pd
import re
from models.empresas import Empresas


def carregar_mapas_auxiliares(conexao):
    cursor = conexao.connection.cursor()

    def carregar_tabela(nome_tabela, nome_id_coluna):
        cursor.execute(f"SELECT {nome_id_coluna}, descricao FROM {nome_tabela}")
        return {desc.lower().strip(): id_ for id_, desc in cursor.fetchall()}

    mapas = {
        "categoria_doc": carregar_tabela("categoria_documento", "id_categoria_doc"),
        "especie": carregar_tabela("especie_controle", "id_especie"),
        "situacao": carregar_tabela("situacao_emissor", "id_situacao"),
        "setor": carregar_tabela("setor_atividade", "id_setor"),
    }

    # conn.close()
    return mapas


def process_csv_files(base_path, conexao):
    empresas_list = []
    mapas = carregar_mapas_auxiliares(conexao)

    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if not os.path.isdir(year_path):
            continue

        for file in os.listdir(year_path):
            if file.endswith(".csv") and file.startswith("fca_cia_aberta_geral"):
                file_path = os.path.join(year_path, file)

                try:
                    df = pd.read_csv(
                        file_path, encoding="latin1", delimiter=";", on_bad_lines="skip"
                    )
                except (pd.errors.ParserError, UnicodeDecodeError) as e:
                    print(f"Erro ao processar o arquivo {file_path}: {e}")
                    continue

                for _, row in df.iterrows():
                    empresa = Empresas(
                        _id_categoria_doc=mapas["categoria_doc"].get(
                            str(row.get("Categoria_Registro_CVM")).lower().strip()
                        ),
                        _codigo_cvm=row.get("Codigo_CVM"),
                        _cnpj_companhia=re.sub(
                            r"\D", "", row.get("CNPJ_Companhia") or ""
                        ),
                        _descricao_atividade=row.get("Descricao_Atividade"),
                        _id_especie=mapas["especie"].get(
                            str(row.get("Especie_Controle_Acionario")).lower().strip()
                        ),
                        _identificador_documento=row.get("ID_Documento"),
                        _mes_encerramento_exercicio_social=row.get(
                            "Mes_Encerramento_Exercicio_Social"
                        ),
                        _nome_empresa=row.get("Nome_Empresarial"),
                        _nome_anterior_empresa=row.get("Nome_Empresarial_Anterior"),
                        _pagina_web=row.get("Pagina_Web"),
                        _pais_custodia_valores_mobiliarios=row.get(
                            "Pais_Custodia_Valores_Mobiliarios"
                        ),
                        _pais_origem=row.get("Pais_Origem"),
                        _id_setor=mapas["setor"].get(
                            str(row.get("Setor_Atividade")).lower().strip()
                        ),
                        _id_situacao=mapas["situacao"].get(
                            str(row.get("Situacao_Emissor")).lower().strip()
                        ),
                        _situacao_registro_cvm=row.get("Situacao_Registro_CVM"),
                        _versao=row.get("Versao"),
                        _data_registro_cvm=row.get("Data_Registro_CVM"),
                        _data_nome_empresarial=row.get("Data_Nome_Empresarial"),
                        _data_categoria_registro_cvm=row.get(
                            "Data_Categoria_Registro_CVM"
                        ),
                        _data_situacao_registro_cvm=row.get(
                            "Data_Situacao_Registro_CVM"
                        ),
                        _data_constituicao=row.get("Data_Constituicao"),
                        _data_especie_controle_acionario=row.get(
                            "Data_Especie_Controle_Acionario"
                        ),
                        _data_referencia_documento=row.get("Data_Referencia"),
                        _data_situacao_emissor=row.get("Data_Situacao_Emissor"),
                        _data_alteracao_exercicio_social=row.get(
                            "Data_Alteracao_Exercicio_Social"
                        ),
                        _dia_encerramento_exercicio_social=row.get(
                            "Dia_Encerramento_Exercicio_Social"
                        ),
                        _mes_doc=row.get("Data_Referencia")[5:7],
                        _ano_doc=row.get("Data_Referencia")[:4],
                    )

                    empresas_list.append(empresa)

    return empresas_list
