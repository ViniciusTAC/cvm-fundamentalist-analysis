CREATE TABLE `grupo_demonstrativo_financeiro` (
  `id_grupo_dfp` int NOT NULL AUTO_INCREMENT,
  `codigo_grupo_dfp` varchar(15) NOT NULL,
  `grupo_dfp` varchar(255) NOT NULL,
  PRIMARY KEY (`codigo_grupo_dfp`),
  UNIQUE KEY `id_grupo_dfp_UNIQUE` (`id_grupo_dfp`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO grupo_demonstrativo_financeiro (codigo_grupo_dfp, grupo_dfp)
VALUES
    ("BPA-IND", "DF Individual - Ativo"),
    ("BPA-CON", "DF Consolidado - Ativo"),
    ("BPP-IND", "DF Individual - Passivo"),
    ("BPP-CON", "DF Consolidado - Passivo"),
    ("DVA-IND", "DF Individual - Demonstração de Valor Adicionado"),
    ("DVA-CON", "DF Consolidado - Demonstração de Valor Adicionado"),
    ("DRE-IND", "DF Individual - Demonstração do Resultado"),
    ("DRE-CON", "DF Consolidado - Demonstração do Resultado");