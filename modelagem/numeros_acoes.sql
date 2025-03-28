CREATE TABLE `numeros_acoes` (
  `fonte_dados` varchar(45) DEFAULT NULL,
  `cnpj_companhia` varchar(45) NOT NULL,
  `denominacao_companhia` varchar(255) DEFAULT NULL,
  `qtd_acoes_ordinarias_capital_integralizado` bigint DEFAULT NULL,
  `qtd_acoes_preferenciais_capital_integralizado` bigint DEFAULT NULL,
  `qtd_total_acoes_capital_integralizado` bigint DEFAULT NULL,
  `qtd_acoes_ordinarias_tesouro` bigint DEFAULT NULL,
  `qtd_acoes_preferenciais_tesouro` bigint DEFAULT NULL,
  `qtd_total_acoes_tesouro` bigint DEFAULT NULL,
  `versao` int DEFAULT NULL,
  `data_referencia_doc` date DEFAULT NULL,
  `data_doc` date DEFAULT NULL,
  `mes_doc` varchar(4) DEFAULT NULL,
  `ano_doc` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
