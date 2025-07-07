import sqlite3
import os

CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")

def calcular_lpa(caminho_banco, cnpj, ano, mes):
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()

    # Buscar o id_plano_conta correspondente a 'Lucro Líquido'
    cursor.execute("""
        SELECT codigo_conta
        FROM planos_contas
        WHERE descricao_conta = 'Lucro Líquido'
    """)
    resultado = cursor.fetchone()
    if not resultado:
        raise ValueError("Plano de conta 'Lucro Líquido' não encontrado.")
    id_lucro_liquido = resultado[0]
    print(id_lucro_liquido)

    # Buscar o lucro líquido da empresa no período
    cursor.execute("""
        SELECT valor_conta
        FROM demonstrativo_financeiro
        WHERE cnpj_companhia = ?
          AND ano = ?
          AND mes = ?
          AND id_plano_conta = ?
    """, (cnpj, ano, mes, id_lucro_liquido))
    resultado = cursor.fetchone()
    if not resultado:
        raise ValueError("Lucro líquido não encontrado para os parâmetros informados.")
    lucro_liquido = resultado[0]

    # Buscar os dados de ações
    cursor.execute("""
        SELECT qtd_total_acoes_capital_integralizado, qtd_total_acoes_tesouro
        FROM numeros_acoes
        WHERE cnpj_companhia = ?
          AND ano = ?
          AND mes = ?
        ORDER BY data_referencia DESC
        LIMIT 1
    """, (cnpj, ano, mes))
    resultado = cursor.fetchone()
    if not resultado:
        raise ValueError("Dados de ações não encontrados.")

    total_acoes = resultado[0]
    acoes_tesouro = resultado[1] if resultado[1] is not None else 0

    acoes_em_circulacao = total_acoes - acoes_tesouro
    if acoes_em_circulacao <= 0:
        raise ValueError("Número de ações em circulação inválido.")

    lpa = lucro_liquido / acoes_em_circulacao

    conn.close()
    return lpa

# Exemplo de uso:
if __name__ == "__main__":
    try:
        cnpj = '97837181000147'  # Substitua pelo CNPJ real da companhia
        ano = 2024
        mes = 12
        lpa = calcular_lpa(CAMINHO_BANCO, cnpj, ano, mes)
        print(f"LPA da empresa {cnpj} em {mes}/{ano}: {lpa:.4f}")
    except Exception as e:
        print(f"Erro: {e}")
