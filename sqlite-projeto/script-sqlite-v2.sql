-- ==========================
-- TABELAS AUXILIARES
-- ==========================

CREATE TABLE escala_monetaria (
  id_escala INTEGER PRIMARY KEY,
  descricao TEXT UNIQUE
);

CREATE TABLE ordem_exercicio (
  id_ordem INTEGER PRIMARY KEY,
  descricao TEXT UNIQUE
);

CREATE TABLE moeda (
  id_moeda INTEGER PRIMARY KEY,
  sigla TEXT,
  descricao TEXT
);

CREATE TABLE especie_controle (
  id_especie INTEGER PRIMARY KEY,
  descricao TEXT UNIQUE
);

CREATE TABLE situacao_emissor (
  id_situacao INTEGER PRIMARY KEY,
  descricao TEXT UNIQUE
);

CREATE TABLE setor_atividade (
  id_setor INTEGER PRIMARY KEY,
  descricao TEXT UNIQUE
);

-- ==========================
-- TABELAS PRINCIPAIS
-- ==========================

CREATE TABLE empresas (
  codigo_cvm TEXT PRIMARY KEY,
  cnpj_companhia TEXT NOT NULL,
  nome_empresa TEXT,
  nome_anterior_empresa TEXT,
  descricao_atividade TEXT,
  id_especie INTEGER,
  id_situacao INTEGER,
  id_setor INTEGER,
  categoria_doc TEXT,
  versao INTEGER,
  pagina_web TEXT,
  pais_origem TEXT,
  pais_custodia_valores_mobiliarios TEXT,
  mes_encerramento_exercicio_social INTEGER,
  dia_encerramento_exercicio_social INTEGER,
  data_constituicao DATE,
  data_situacao_emissor DATE,
  data_registro_cvm DATE,
  data_categoria_registro_cvm DATE,
  data_situacao_registro_cvm DATE,
  data_nome_empresarial DATE,
  data_especie_controle_acionario DATE,
  data_alteracao_exercicio_social DATE,
  data_referencia_documento DATE,
  mes_doc TEXT,
  ano_doc TEXT,
  data_hora_insercao DATETIME,
  data_hora_atualizacao DATETIME,
  FOREIGN KEY (id_especie) REFERENCES especie_controle(id_especie),
  FOREIGN KEY (id_situacao) REFERENCES situacao_emissor(id_situacao),
  FOREIGN KEY (id_setor) REFERENCES setor_atividade(id_setor)
);

CREATE TABLE planos_contas (
  id_planos_contas INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo_conta TEXT NOT NULL UNIQUE,
  descricao_conta TEXT NOT NULL,
  comportamento TEXT NOT NULL
);

CREATE TABLE grupo_demonstrativo_financeiro (
  codigo_grupo_dfp TEXT PRIMARY KEY,
  grupo_dfp TEXT NOT NULL
);

CREATE TABLE demonstrativo_financeiro (
  codigo_conta TEXT NOT NULL,
  codigo_cvm TEXT NOT NULL,
  id_escala INTEGER,
  grupo_dfp TEXT NOT NULL,
  id_moeda INTEGER,
  id_ordem INTEGER,
  conta_fixa TEXT,
  versao INTEGER,
  data_inicio_exercicio DATE,
  data_fim_exercicio DATE,
  data_referencia_doc DATE,
  valor_conta REAL,
  data_doc DATE,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_conta) REFERENCES planos_contas (codigo_conta),
  FOREIGN KEY (grupo_dfp) REFERENCES grupo_demonstrativo_financeiro (codigo_grupo_dfp),
  FOREIGN KEY (codigo_cvm) REFERENCES empresas (codigo_cvm),
  FOREIGN KEY (id_escala) REFERENCES escala_monetaria(id_escala),
  FOREIGN KEY (id_moeda) REFERENCES moeda(id_moeda),
  FOREIGN KEY (id_ordem) REFERENCES ordem_exercicio(id_ordem)
);

CREATE TABLE informacao_trimestral (
  codigo_conta TEXT NOT NULL,
  codigo_cvm TEXT NOT NULL,
  id_escala INTEGER,
  grupo_dfp TEXT NOT NULL,
  id_moeda INTEGER,
  id_ordem INTEGER,
  conta_fixa TEXT,
  versao INTEGER,
  data_inicio_exercicio DATE,
  data_fim_exercicio DATE,
  data_referencia_doc DATE,
  valor_conta REAL,
  data_doc DATE,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_conta) REFERENCES planos_contas (codigo_conta),
  FOREIGN KEY (grupo_dfp) REFERENCES grupo_demonstrativo_financeiro (codigo_grupo_dfp),
  FOREIGN KEY (codigo_cvm) REFERENCES empresas (codigo_cvm),
  FOREIGN KEY (id_escala) REFERENCES escala_monetaria(id_escala),
  FOREIGN KEY (id_moeda) REFERENCES moeda(id_moeda),
  FOREIGN KEY (id_ordem) REFERENCES ordem_exercicio(id_ordem)
);

CREATE TABLE parecer_demonstrativo (
  codigo_cvm TEXT NOT NULL,
  num_linha_parecer_declaracao INTEGER,
  tipo_parecer_declaracao TEXT,
  tipo_relatorio_auditor TEXT,
  texto_parecer_declaracao TEXT,
  versao INTEGER,
  data_referencia_doc DATE,
  data_doc DATE,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_cvm) REFERENCES empresas (codigo_cvm)
);

CREATE TABLE parecer_trimestral (
  codigo_cvm TEXT NOT NULL,
  num_linha_parecer_declaracao INTEGER,
  tipo_parecer_declaracao TEXT,
  tipo_relatorio_especial TEXT,
  texto_parecer_declaracao TEXT,
  versao INTEGER,
  data_referencia_doc DATE,
  data_doc DATE,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_cvm) REFERENCES empresas (codigo_cvm)
);

CREATE TABLE formulario_referencia (
  codigo_cvm TEXT NOT NULL,
  categoria_doc TEXT,
  denominacao_companhia TEXT,
  id_doc INTEGER,
  link_doc TEXT,
  versao REAL,
  data_recebimento_doc DATE,
  data_referencia_doc DATE,
  data_doc DATE,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_cvm) REFERENCES empresas (codigo_cvm)
);

CREATE TABLE periodicos_eventuais (
  codigo_cvm TEXT NOT NULL,
  assunto TEXT,
  categoria_doc TEXT,
  especie TEXT,
  link_doc TEXT,
  nome_companhia TEXT,
  protocolo_entrega TEXT,
  tipo TEXT,
  tipo_apresentacao TEXT,
  versao INTEGER,
  data_entrega_doc DATE,
  data_referencia_doc DATE,
  data_doc DATE,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_cvm) REFERENCES empresas (codigo_cvm)
);

CREATE TABLE numeros_acoes (
  fonte_dados TEXT,
  codigo_cvm TEXT NOT NULL,
  denominacao_companhia TEXT,
  qtd_acoes_ordinarias_capital_integralizado INTEGER,
  qtd_acoes_preferenciais_capital_integralizado INTEGER,
  qtd_total_acoes_capital_integralizado INTEGER,
  qtd_acoes_ordinarias_tesouro INTEGER,
  qtd_acoes_preferenciais_tesouro INTEGER,
  qtd_total_acoes_tesouro INTEGER,
  versao INTEGER,
  data_referencia_doc DATE,
  data_doc DATE,
  mes_doc TEXT,
  ano_doc TEXT,
  FOREIGN KEY (codigo_cvm) REFERENCES empresas (codigo_cvm),
  UNIQUE(fonte_dados, codigo_cvm, data_referencia_doc, data_doc, mes_doc, ano_doc)
);

-- ==========================
-- ÍNDICES
-- ==========================

CREATE UNIQUE INDEX idx_unico_demonstrativo_financeiro
ON demonstrativo_financeiro (
  codigo_cvm,
  codigo_conta,
  grupo_dfp,
  conta_fixa,
  mes_doc,
  ano_doc
);

CREATE UNIQUE INDEX idx_unico_informacao_trimestral
ON informacao_trimestral (
  codigo_cvm,
  codigo_conta,
  grupo_dfp,
  conta_fixa,
  mes_doc,
  ano_doc
);

-- ==========================
-- INSERTS
-- ==========================

INSERT INTO grupo_demonstrativo_financeiro (codigo_grupo_dfp, grupo_dfp) VALUES
  ("BPA_IND", "DF Individual - Ativo"),
  ("BPA_CON", "DF Consolidado - Ativo"),
  ("BPP_IND", "DF Individual - Passivo"),
  ("BPP_CON", "DF Consolidado - Passivo"),
  ("DVA_IND", "DF Individual - Demonstração de Valor Adicionado"),
  ("DVA_CON", "DF Consolidado - Demonstração de Valor Adicionado"),
  ("DRE_IND", "DF Individual - Demonstração do Resultado"),
  ("DRE_CON", "DF Consolidado - Demonstração do Resultado");

INSERT INTO planos_contas (codigo_conta, descricao_conta, comportamento) VALUES
  ('1', 'Ativo Total', 'BPA'),
  ('1.01', 'Ativo Circulante', 'BPA'),
  ('1.01.01', 'Disponibilidades', 'BPA'),
  ('2', 'Passivo Total', 'BPP'),
  ('2.01', 'Passivo Circulante', 'BPP'),
  ('2.02', 'Passivo Não Circulante', 'BPP'),
  ('Patrimônio Líquido', 'Patrimônio Líquido', 'BPP'),
  ('3.01', 'Receita Líquida', 'DRE'),
  ('3.03', 'Custo dos Produtos Vendidos', 'DRE'),
  ('3.05', 'Despesas Operacionais', 'DRE'),
  ('3.07', 'Resultado Financeiro', 'DRE'),
  ('3.11', 'Imposto de Renda', 'DRE'),
  ('3.13', 'Lucro Líquido', 'DRE'),
  ('3.99', 'Outros Resultados', 'DRE'),
  ('Juros sobre o Capital Próprio', 'Juros sobre o Capital Próprio', 'DVA'),
  ('Dividendos', 'Dividendos', 'DVA');
