Planos de Contas

1.01.04.05 - Almoxarifado e Outros
1.01.04.05 - Estoques de Materiais
1.01.04.05 - Provisão p/ perdas nos estoques M.Prima
1.01.04.05 - Estoques em Poder de Terceiros
1.01.04.05 - SFH - Sistema Financeiro da Habitação



valores_a_manter = ['Ativo Total','Ativo Circulante','Disponibilidades','Caixa e Equivalentes de Caixa']
valores_a_manter = ['1','1.01','1.01.01']









Segue uma sugestão de mensagem para enviar ao seu professor do TCC via Telegram:

---

Bom dia, Marcos,

Espero que esteja bem! Estou avançando com o trabalho do TCC e gostaria de compartilhar uma atualização sobre a abordagem que estou planejando adotar. Inicialmente, o objetivo era abranger todos os planos de contas presentes nos demonstrativos financeiros e informações trimestrais disponibilizados pela CVM. No entanto, analisando melhor, percebi que seria mais interessante focar nos planos de contas específicos, pois eles oferecem uma base mais estruturada para realizar análises fundamentalistas.

Os principais itens que estou considerando incluir são:

- Balanço Patrimonial Ativo (BPA): Ativo Total, Ativo Circulante, Disponibilidades.
- Balanço Patrimonial Passivo (BPP): Passivo Total, Passivo Circulante, Passivo Não Circulante, Patrimônio Líquido.
- Demonstração do Resultado do Exercício (DRE): Receita Líquida, Custo dos Produtos Vendidos, Despesas Operacionais, Resultado Financeiro, Imposto de Renda, Lucro Líquido e Outros Resultados.
- Demonstração de Valor Adicionado (DVA): Juros sobre o Capital Próprio, Dividendos.

Com essa abordagem, acredito que posso extrair dados mais relevantes e direcionados, possibilitando análises financeiras mais robustas, como avaliação de rentabilidade, estrutura de capital e fluxo de caixa. Gostaria de saber se o senhor considera essa proposta adequada ou se sugere algum ajuste.

Desde já, agradeço pela atenção e pela orientação! 

Atenciosamente,  
[Seu Nome]

---

Se precisar, podemos ajustar mais alguma coisa no texto! 😊





23.041.875/0001-37


# BPA ---------------

# Defina a lista de valores que deseja manter
# valores_a_manter = ['Ativo Total','Ativo Circulante','Disponibilidades','Caixa e Equivalentes de Caixa']
valores_a_manter = ["1", "1.01", "1.01.01"]
# Mantenha as linhas que contêm os valores da lista na coluna 'DS_CONTA' e exclua as demais
BPA_itr = BPA_itr.loc[BPA_itr["CD_CONTA"].isin(valores_a_manter)]

# Defina a lista de valores que deseja manter
# valores_a_manter = ['Ativo Total','Ativo Circulante','Disponibilidades','Caixa e Equivalentes de Caixa']
valores_a_manter = ["1", "1.01", "1.01.01"]
# Mantenha as linhas que contêm os valores da lista na coluna 'DS_CONTA' e exclua as demais
BPA_dfp = BPA_dfp.loc[BPA_dfp["CD_CONTA"].isin(valores_a_manter)]



# BPP ----------------------------------------------------
# Defina a lista de valores que deseja manter
# valores_a_manter = ['Passivo Total','Passivo Circulante'']
valores_a_manter = ["2", "2.01", "2.02"]  # ,'2.05','2.07'
# Mantenha as linhas que contêm os valores da lista na coluna 'DS_CONTA' e exclua as demais
BPP_itr_1 = BPP_itr.loc[BPP_itr["CD_CONTA"].isin(valores_a_manter)]

# valores_a_manter = ['Patrimônio Líquido']
valores_a_manter = ["Patrimônio Líquido"]
# Mantenha as linhas que contêm os valores da lista na coluna 'DS_CONTA' e exclua as demais
BPP_itr_2 = BPP_itr.loc[BPP_itr["DS_CONTA"].isin(valores_a_manter)]

# Defina a lista de valores que deseja manter
# valores_a_manter = ['Passivo Total','Passivo Circulante'']
valores_a_manter = ["2", "2.01", "2.02"]  # ,'2.05','2.07'
# Mantenha as linhas que contêm os valores da lista na coluna 'DS_CONTA' e exclua as demais
BPP_dfp_1 = BPP_dfp.loc[BPP_dfp["CD_CONTA"].isin(valores_a_manter)]

# valores_a_manter = ['Patrimônio Líquido']
valores_a_manter = ["Patrimônio Líquido"]
# Mantenha as linhas que contêm os valores da lista na coluna 'DS_CONTA' e exclua as demais
BPP_dfp_2 = BPP_dfp.loc[BPP_dfp["DS_CONTA"].isin(valores_a_manter)]



# DVA ----------
# Defina a lista de valores que deseja manter
valores_a_manter = ["Juros sobre o Capital Próprio", "Dividendos"]
# Mantenha as linhas que contêm os valores da lista na coluna 'DS_CONTA' e exclua as demais
DVA_itr = DVA_itr.loc[DVA_itr["DS_CONTA"].isin(valores_a_manter)]

# Defina a lista de valores que deseja manter
valores_a_manter = ["Juros sobre o Capital Próprio", "Dividendos"]
# Mantenha as linhas que contêm os valores da lista na coluna 'DS_CONTA' e exclua as demais
DVA_dfp = DVA_dfp.loc[DVA_dfp["DS_CONTA"].isin(valores_a_manter)]


# DVA ----------
valores_a_manter = ["3.01", "3.03", "3.05", "3.07", "3.11", "3.13", "3.99"]
DRE_itr = DRE_itr.loc[DRE_itr["CD_CONTA"].isin(valores_a_manter)]

valores_a_manter = ["3.01", "3.03", "3.05", "3.07", "3.11", "3.13", "3.99"]
DRE_dfp = DRE_dfp.loc[DRE_dfp["CD_CONTA"].isin(valores_a_manter)]



    "1": "Ativo Total",
    "1.01": "Ativo Circulante",
    "1.01.01": "Disponibilidades",
    "2": "Passivo Total",
    "2.01": "Passivo Circulante",
    "2.02": "Passivo Não Circulante",
    "Patrimônio Líquido": "Patrimônio Líquido",
    "3.01": "Receita Líquida",
    "3.03": "Custo dos Produtos Vendidos",
    "3.05": "Despesas Operacionais",
    "3.07": "Resultado Financeiro",
    "3.11": "Imposto de Renda",
    "3.13": "Lucro Líquido",
    "3.99": "Outros Resultados",
    "Juros sobre o Capital Próprio": "Juros sobre o Capital Próprio",
    "Dividendos": "Dividendos"