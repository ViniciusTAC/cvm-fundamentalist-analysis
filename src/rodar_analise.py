import os
import sqlite3
import pandas as pd
from datetime import datetime

# Caminhos
CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")
CAMINHO_SQL = "analise_fundamenstalista_v2.sql"

def carregar_sqls():
    with open(CAMINHO_SQL, "r", encoding="utf-8") as f:
        sql_content = f.read()

    # Parte 1: CREATE TABLEs
    partes = sql_content.split('-- ---------------------------------------------------------------------------------------------\n-- ITR')
    create_part = partes[0].strip()

    # Parte 2: ITR e DFP
    itr_dfp_rest = partes[1].strip().split('-- ---------------------------------------------------------------------------------------------\n-- DFP')
    itr_sql = itr_dfp_rest[0].strip()
    dfp_sql = itr_dfp_rest[1].strip()

    return create_part, itr_sql, dfp_sql

def criar_tabelas(create_sql: str, conn: sqlite3.Connection):
    print("🔧 Criando tabelas analise_itr e analise_dfp (se não existirem)...")
    cursor = conn.cursor()
    for stmt in create_sql.split(";"):
        stmt = stmt.strip()
        if stmt:
            cursor.execute(stmt)
    conn.commit()
    print("✅ Tabelas verificadas/criadas.")

def upsert_dataframe(df: pd.DataFrame, table_name: str, conn: sqlite3.Connection):
    cursor = conn.cursor()
    novos, atualizados = 0, 0

    for _, row in df.iterrows():
        agora = datetime.now().isoformat(sep=' ', timespec='seconds')
        try:
            cursor.execute(f"""
                INSERT INTO {table_name} (
                    cnpj_companhia, ano, mes,
                    acoes_em_circulacao, lpa, lc, db, dl,
                    data_hora_insercao
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row["cnpj_companhia"], row["ano"], row["mes"],
                row["acoes_em_circulacao"], row["lpa"], row["lc"], row["db"], row["dl"],
                agora
            ))
            novos += 1
        except sqlite3.IntegrityError:
            cursor.execute(f"""
                UPDATE {table_name}
                SET
                    acoes_em_circulacao = ?,
                    lpa = ?,
                    lc = ?,
                    db = ?,
                    dl = ?,
                    data_hora_atualizacao = ?
                WHERE cnpj_companhia = ? AND ano = ? AND mes = ?
            """, (
                row["acoes_em_circulacao"], row["lpa"], row["lc"], row["db"], row["dl"],
                agora,
                row["cnpj_companhia"], row["ano"], row["mes"]
            ))
            atualizados += 1

    conn.commit()
    print(f"✅ Tabela {table_name}: {novos} inseridos, {atualizados} atualizados.")

def main():
    print("🚀 Iniciando processo de análise fundamentalista...")
    conn = sqlite3.connect(CAMINHO_BANCO)

    create_sql, itr_sql, dfp_sql = carregar_sqls()

    criar_tabelas(create_sql, conn)

    print("📥 Executando consulta ITR...")
    df_itr = pd.read_sql_query(itr_sql, conn)
    upsert_dataframe(df_itr, "analise_itr", conn)

    print("📥 Executando consulta DFP...")
    df_dfp = pd.read_sql_query(dfp_sql, conn)
    upsert_dataframe(df_dfp, "analise_dfp", conn)

    conn.close()
    print("🏁 Processo finalizado com sucesso!")

if __name__ == "__main__":
    main()
