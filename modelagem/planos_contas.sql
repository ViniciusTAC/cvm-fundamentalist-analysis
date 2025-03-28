CREATE TABLE `planos_contas` (
  `id_planos_contas` int NOT NULL AUTO_INCREMENT,
  `codigo_conta` varchar(30) NOT NULL,
  `descricao_conta` varchar(100) NOT NULL,
  `comportamento` varchar(255) NOT NULL,
  PRIMARY KEY (`codigo_conta`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



INSERT INTO planos_contas (codigo_conta, descricao_conta, comportamento)
VALUES
    ("1", "Ativo Total", "BPA"),
    ("1.01", "Ativo Circulante", "BPA"),
    ("1.01.01", "Disponibilidades", "BPA"),
    ("2", "Passivo Total", "BPP"),
    ("2.01", "Passivo Circulante", "BPP"),
    ("2.02", "Passivo Não Circulante", "BPP"),
    ("Patrimônio Líquido", "Patrimônio Líquido", "BPP"),
    ("3.01", "Receita Líquida", "DRE"),
    ("3.03", "Custo dos Produtos Vendidos", "DRE"),
    ("3.05", "Despesas Operacionais", "DRE"),
    ("3.07", "Resultado Financeiro", "DRE"),
    ("3.11", "Imposto de Renda", "DRE"),
    ("3.13", "Lucro Líquido", "DRE"),
    ("3.99", "Outros Resultados", "DRE"),
    ("Juros sobre o Capital Próprio", "Juros sobre o Capital Próprio", "DVA"),
    ("Dividendos", "Dividendos", "DVA");