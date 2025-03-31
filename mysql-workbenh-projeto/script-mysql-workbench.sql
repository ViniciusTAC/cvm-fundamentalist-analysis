-- Desabilita verificações temporárias para evitar conflitos
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Criação do schema
CREATE SCHEMA IF NOT EXISTS `cvm_dados` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `cvm_dados`;

-- Tabela: planos_contas
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

-- Tabela: grupo_demonstrativo_financeiro
CREATE TABLE IF NOT EXISTS `grupo_demonstrativo_financeiro` (
  `codigo_grupo_dfp` VARCHAR(15) NOT NULL,
  `grupo_dfp` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`codigo_grupo_dfp`)
) ENGINE=InnoDB;

-- Inserts para grupo_demonstrativo_financeiro
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

-- Tabela: empresas
CREATE TABLE IF NOT EXISTS `empresas` (
  `categoria_doc` VARCHAR(100),
  `codigo_cvm` CHAR(6) NOT NULL,
  `cnpj_companhia` VARCHAR(45) NOT NULL,
  `descricao_atividade` VARCHAR(200),
  `especie_controle_acionario` VARCHAR(100),
  `identificador_documento` INT,
  `mes_encerramento_exercicio_social` SMALLINT,
  `nome_empresa` VARCHAR(100),
  `nome_anterior_empresa` VARCHAR(100),
  `pagina_web` VARCHAR(100),
  `pais_custodia_valores_mobiliarios` VARCHAR(100),
  `pais_origem` VARCHAR(100),
  `setor_atividade` VARCHAR(100),
  `situacao_emissor` VARCHAR(100),
  `situacao_registro_cvm` VARCHAR(100),
  `versao` SMALLINT,
  `data_registro_cvm` DATE,
  `data_nome_empresarial` DATE,
  `data_categoria_registro_cvm` DATE,
  `data_situacao_registro_cvm` DATE,
  `data_constituicao` DATE,
  `data_especie_controle_acionario` DATE,
  `data_referencia_documento` DATE,
  `data_situacao_emissor` DATE,
  `data_alteracao_exercicio_social` DATE,
  `dia_encerramento_exercicio_social` SMALLINT,
  `data_doc` DATE,
  `mes_doc` VARCHAR(4),
  `ano_doc` VARCHAR(4),
  PRIMARY KEY (`codigo_cvm`, `cnpj_companhia`),
  UNIQUE KEY `cnpj_companhia_UNIQUE` (`cnpj_companhia`)
) ENGINE=InnoDB;

-- Tabela: demonstrativo_financeiro
CREATE TABLE IF NOT EXISTS `demonstrativo_financeiro` (
  `codigo_conta` VARCHAR(28) NOT NULL,
  `cnpj_companhia` VARCHAR(45) NOT NULL,
  `codigo_cvm` CHAR(6),
  `escala_monetaria` VARCHAR(100),
  `grupo_dfp` VARCHAR(15) NOT NULL,
  `moeda` INT,
  `ordem_exercicio` VARCHAR(9),
  `conta_fixa` VARCHAR(1),
  `versao` SMALLINT,
  `data_inicio_exercicio` DATE,
  `data_fim_exercicio` DATE,
  `data_referencia_doc` DATE,
  `valor_conta` DECIMAL(10,0),
  `data_doc` DATE,
  `mes_doc` VARCHAR(4),
  `ano_doc` VARCHAR(4),
  INDEX (`codigo_conta`),
  INDEX (`cnpj_companhia`),
  INDEX (`grupo_dfp`),
  FOREIGN KEY (`codigo_conta`) REFERENCES `planos_contas` (`codigo_conta`),
  FOREIGN KEY (`grupo_dfp`) REFERENCES `grupo_demonstrativo_financeiro` (`codigo_grupo_dfp`),
  FOREIGN KEY (`cnpj_companhia`) REFERENCES `empresas` (`cnpj_companhia`)
) ENGINE=InnoDB;

-- Tabela: informacao_trimestral
CREATE TABLE IF NOT EXISTS `informacao_trimestral` (
  `codigo_conta` VARCHAR(28) NOT NULL,
  `cnpj_companhia` VARCHAR(45) NOT NULL,
  `codigo_cvm` CHAR(6),
  `escala_monetaria` VARCHAR(100),
  `grupo_dfp` VARCHAR(15) NOT NULL,
  `moeda` INT,
  `ordem_exercicio` VARCHAR(9),
  `conta_fixa` VARCHAR(1),
  `versao` SMALLINT,
  `data_inicio_exercicio` DATE,
  `data_fim_exercicio` DATE,
  `data_referencia_doc` DATE,
  `valor_conta` DECIMAL(10,0),
  `data_doc` DATE,
  `mes_doc` VARCHAR(4),
  `ano_doc` VARCHAR(4),
  INDEX (`codigo_conta`),
  INDEX (`cnpj_companhia`),
  INDEX (`grupo_dfp`),
  FOREIGN KEY (`codigo_conta`) REFERENCES `planos_contas` (`codigo_conta`),
  FOREIGN KEY (`grupo_dfp`) REFERENCES `grupo_demonstrativo_financeiro` (`codigo_grupo_dfp`),
  FOREIGN KEY (`cnpj_companhia`) REFERENCES `empresas` (`cnpj_companhia`)
) ENGINE=InnoDB;

-- Tabela: parecer_demonstrativo
CREATE TABLE IF NOT EXISTS `parecer_demonstrativo` (
  `cnpj_companhia` VARCHAR(20),
  `num_linha_parecer_declaracao` SMALLINT,
  `tipo_parecer_declaracao` VARCHAR(101),
  `tipo_relatorio_auditor` VARCHAR(19),
  `texto_parecer_declaracao` VARCHAR(8000),
  `versao` SMALLINT,
  `data_referencia_doc` DATE,
  `data_doc` DATE,
  `mes_doc` VARCHAR(4),
  `ano_doc` VARCHAR(4),
  INDEX (`cnpj_companhia`),
  FOREIGN KEY (`cnpj_companhia`) REFERENCES `empresas` (`cnpj_companhia`)
) ENGINE=InnoDB;

-- Tabela: parecer_trimestral
CREATE TABLE IF NOT EXISTS `parecer_trimestral` (
  `cnpj_companhia` VARCHAR(20) NOT NULL,
  `num_linha_parecer_declaracao` SMALLINT,
  `tipo_parecer_declaracao` VARCHAR(101),
  `tipo_relatorio_especial` VARCHAR(19),
  `texto_parecer_declaracao` VARCHAR(8000),
  `versao` SMALLINT,
  `data_referencia_doc` DATE,
  `data_doc` DATE,
  `mes_doc` VARCHAR(4),
  `ano_doc` VARCHAR(4),
  INDEX (`cnpj_companhia`),
  FOREIGN KEY (`cnpj_companhia`) REFERENCES `empresas` (`cnpj_companhia`)
) ENGINE=InnoDB;

-- Tabela: formulario_referencia
CREATE TABLE IF NOT EXISTS `formulario_referencia` (
  `cnpj_companhia` VARCHAR(20) NOT NULL,
  `categoria_doc` VARCHAR(20),
  `denominacao_companhia` VARCHAR(100),
  `id_doc` INT,
  `link_doc` VARCHAR(121),
  `versao` DECIMAL,
  `data_recebimento_doc` DATE,
  `data_referencia_doc` DATE,
  `data_doc` DATE,
  `mes_doc` VARCHAR(4),
  `ano_doc` VARCHAR(4),
  INDEX (`cnpj_companhia`),
  FOREIGN KEY (`cnpj_companhia`) REFERENCES `empresas` (`cnpj_companhia`)
) ENGINE=InnoDB;

-- Tabela: periodicos_eventuais
CREATE TABLE IF NOT EXISTS `periodicos_eventuais` (
  `cnpj_companhia` VARCHAR(20) NOT NULL,
  `codigo_cvm` VARCHAR(6),
  `assunto` TEXT,
  `categoria_doc` VARCHAR(100),
  `especie` VARCHAR(100),
  `link_doc` VARCHAR(168),
  `nome_companhia` VARCHAR(100),
  `protocolo_entrega` CHAR(30),
  `tipo` VARCHAR(100),
  `tipo_apresentacao` VARCHAR(33),
  `versao` SMALLINT,
  `data_entrega_doc` DATE,
  `data_referencia_doc` DATE,
  `data_doc` DATE,
  `mes_doc` VARCHAR(4),
  `ano_doc` VARCHAR(4),
  INDEX (`cnpj_companhia`),
  FOREIGN KEY (`cnpj_companhia`) REFERENCES `empresas` (`cnpj_companhia`)
) ENGINE=InnoDB;

-- Tabela: numeros_acoes
CREATE TABLE IF NOT EXISTS `numeros_acoes` (
  `fonte_dados` VARCHAR(45),
  `cnpj_companhia` VARCHAR(45) NOT NULL,
  `denominacao_companhia` VARCHAR(255),
  `qtd_acoes_ordinarias_capital_integralizado` BIGINT,
  `qtd_acoes_preferenciais_capital_integralizado` BIGINT,
  `qtd_total_acoes_capital_integralizado` BIGINT,
  `qtd_acoes_ordinarias_tesouro` BIGINT,
  `qtd_acoes_preferenciais_tesouro` BIGINT,
  `qtd_total_acoes_tesouro` BIGINT,
  `versao` INT,
  `data_referencia_doc` DATE,
  `data_doc` DATE,
  `mes_doc` VARCHAR(4),
  `ano_doc` VARCHAR(4),
  UNIQUE KEY `cnpj_companhia_UNIQUE` (`cnpj_companhia`),
  FOREIGN KEY (`cnpj_companhia`) REFERENCES `empresas` (`cnpj_companhia`)
) ENGINE=InnoDB;

-- Restaura configurações anteriores
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


