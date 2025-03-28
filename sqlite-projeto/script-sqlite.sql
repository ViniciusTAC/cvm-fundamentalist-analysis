PRAGMA foreign_keys = ON;

-- Tabela: planos_contas
CREATE TABLE IF NOT EXISTS planos_contas (
  codigo_conta TEXT PRIMARY KEY,
  descricao_conta TEXT NOT NULL
);

-- Tabela: grupo_demonstrativo_financeiro
CREATE TABLE IF NOT EXISTS grupo_demonstrativo_financeiro (
  codigo_grupo_dfp TEXT PRIMARY KEY,
  grupo_dfp TEXT NOT NULL
);

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
CREATE TABLE IF NOT EXISTS empresas (
  categoria_doc TEXT,
  codigo_cvm TEXT NOT NULL,
  cnpj_companhia TEXT NOT NULL UNIQUE,
  descricao_atividade TEXT,
  especie_controle_acionario TEXT,
  identificador_documento INTEGER,
  mes_encerramento_exercicio_social INTEGER,
  nome_empresa TEXT,
  nome_anterior_empresa TEXT,
  pagina_web TEXT,
  pais_custodia_valores_mobiliarios TEXT,
  pais_origem TEXT,
  setor_atividade TEXT,
  situacao_emissor TEXT,
  situacao_registro_cvm TEXT,
  versao INTEGER,
  data_registro_cvm TEXT,
  data_nome_empresarial TEXT,
  data_categoria_registro_cvm TEXT,
  data_situacao_registro_cvm TEXT,
  data_constituicao TEXT,
  data_especie_controle_acionario TEXT,
  data_referencia_documento TEXT,
  data_situacao_emissor TEXT,
  data_alteracao_exercicio_social TEXT,
  dia_encerramento_exercicio_social INTEGER,
  data_doc TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  PRIMARY KEY (codigo_cvm, cnpj_companhia)
);

-- Tabela: demonstrativo_financeiro
CREATE TABLE IF NOT EXISTS demonstrativo_financeiro (
  codigo_conta TEXT NOT NULL,
  cnpj_companhia TEXT NOT NULL,
  codigo_cvm TEXT,
  escala_monetaria TEXT,
  grupo_dfp TEXT NOT NULL,
  moeda INTEGER,
  ordem_exercicio TEXT,
  conta_fixa TEXT,
  versao INTEGER,
  data_inicio_exercicio TEXT,
  data_fim_exercicio TEXT,
  data_referencia_doc TEXT,
  valor_conta REAL,
  data_doc TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_conta) REFERENCES planos_contas (codigo_conta),
  FOREIGN KEY (grupo_dfp) REFERENCES grupo_demonstrativo_financeiro (codigo_grupo_dfp),
  FOREIGN KEY (cnpj_companhia) REFERENCES empresas (cnpj_companhia)
);

-- Tabela: informacao_trimestral
CREATE TABLE IF NOT EXISTS informacao_trimestral (
  codigo_conta TEXT NOT NULL,
  cnpj_companhia TEXT NOT NULL,
  codigo_cvm TEXT,
  escala_monetaria TEXT,
  grupo_dfp TEXT NOT NULL,
  moeda INTEGER,
  ordem_exercicio TEXT,
  conta_fixa TEXT,
  versao INTEGER,
  data_inicio_exercicio TEXT,
  data_fim_exercicio TEXT,
  data_referencia_doc TEXT,
  valor_conta REAL,
  data_doc TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_conta) REFERENCES planos_contas (codigo_conta),
  FOREIGN KEY (grupo_dfp) REFERENCES grupo_demonstrativo_financeiro (codigo_grupo_dfp),
  FOREIGN KEY (cnpj_companhia) REFERENCES empresas (cnpj_companhia)
);

-- Tabela: parecer_demonstrativo
CREATE TABLE IF NOT EXISTS parecer_demonstrativo (
  cnpj_companhia TEXT,
  num_linha_parecer_declaracao INTEGER,
  tipo_parecer_declaracao TEXT,
  tipo_relatorio_auditor TEXT,
  texto_parecer_declaracao TEXT,
  versao INTEGER,
  data_referencia_doc TEXT,
  data_doc TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (cnpj_companhia) REFERENCES empresas (cnpj_companhia)
);

-- Tabela: parecer_trimestral
CREATE TABLE IF NOT EXISTS parecer_trimestral (
  cnpj_companhia TEXT NOT NULL,
  num_linha_parecer_declaracao INTEGER,
  tipo_parecer_declaracao TEXT,
  tipo_relatorio_especial TEXT,
  texto_parecer_declaracao TEXT,
  versao INTEGER,
  data_referencia_doc TEXT,
  data_doc TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (cnpj_companhia) REFERENCES empresas (cnpj_companhia)
);

-- Tabela: formulario_referencia
CREATE TABLE IF NOT EXISTS formulario_referencia (
  cnpj_companhia TEXT NOT NULL,
  categoria_doc TEXT,
  denominacao_companhia TEXT,
  id_doc INTEGER,
  link_doc TEXT,
  versao REAL,
  data_recebimento_doc TEXT,
  data_referencia_doc TEXT,
  data_doc TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (cnpj_companhia) REFERENCES empresas (cnpj_companhia)
);

-- Tabela: periodicos_eventuais
CREATE TABLE IF NOT EXISTS periodicos_eventuais (
  cnpj_companhia TEXT NOT NULL,
  codigo_cvm TEXT,
  assunto TEXT,
  categoria_doc TEXT,
  especie TEXT,
  link_doc TEXT,
  nome_companhia TEXT,
  protocolo_entrega TEXT,
  tipo TEXT,
  tipo_apresentacao TEXT,
  versao INTEGER,
  data_entrega_doc TEXT,
  data_referencia_doc TEXT,
  data_doc TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (cnpj_companhia) REFERENCES empresas (cnpj_companhia)
);

-- Tabela: numeros_acoes
CREATE TABLE IF NOT EXISTS numeros_acoes (
  fonte_dados TEXT,
  cnpj_companhia TEXT NOT NULL UNIQUE,
  denominacao_companhia TEXT,
  qtd_acoes_ordinarias_capital_integralizado INTEGER,
  qtd_acoes_preferenciais_capital_integralizado INTEGER,
  qtd_total_acoes_capital_integralizado INTEGER,
  qtd_acoes_ordinarias_tesouro INTEGER,
  qtd_acoes_preferenciais_tesouro INTEGER,
  qtd_total_acoes_tesouro INTEGER,
  versao INTEGER,
  data_referencia_doc TEXT,
  data_doc TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (cnpj_companhia) REFERENCES empresas (cnpj_companhia)
);
