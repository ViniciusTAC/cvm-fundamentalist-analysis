PRAGMA foreign_keys = ON;

-- Tabela: planos_contas
CREATE TABLE planos_contas (
  id_planos_contas INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo_conta TEXT NOT NULL,
  descricao_conta TEXT NOT NULL,
  comportamento TEXT NOT NULL,
  UNIQUE(codigo_conta)
);

INSERT INTO planos_contas (codigo_conta, descricao_conta, comportamento)
VALUES
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


-- Tabela: grupo_demonstrativo_financeiro
CREATE TABLE IF NOT EXISTS grupo_demonstrativo_financeiro (
  codigo_grupo_dfp TEXT PRIMARY KEY,
  grupo_dfp TEXT NOT NULL
);

-- Inserts para grupo_demonstrativo_financeiro
INSERT INTO grupo_demonstrativo_financeiro (codigo_grupo_dfp, grupo_dfp)
VALUES
  ("BPA_IND", "DF Individual - Ativo"),
  ("BPA_CON", "DF Consolidado - Ativo"),
  ("BPP_IND", "DF Individual - Passivo"),
  ("BPP_CON", "DF Consolidado - Passivo"),
  ("DVA_IND", "DF Individual - Demonstração de Valor Adicionado"),
  ("DVA_CON", "DF Consolidado - Demonstração de Valor Adicionado"),
  ("DRE_IND", "DF Individual - Demonstração do Resultado"),
  ("DRE_CON", "DF Consolidado - Demonstração do Resultado");

-- Tabela: empresas
CREATE TABLE IF NOT EXISTS empresas (
  categoria_doc TEXT,
  codigo_cvm TEXT NOT NULL,
  cnpj_companhia TEXT NOT NULL,
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
  data_situacao_emissor TEXT,
  data_alteracao_exercicio_social TEXT,
  dia_encerramento_exercicio_social INTEGER,
  data_referencia_documento TEXT,
  mes_doc TEXT,
  ano_doc TEXT,
  data_hora_insercao DATETIME,
  data_hora_atualizacao DATETIME,
  PRIMARY KEY (cnpj_companhia, mes_doc, ano_doc)
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
  cnpj_companhia TEXT NOT NULL,
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
  FOREIGN KEY (cnpj_companhia) REFERENCES empresas (cnpj_companhia),
  UNIQUE(fonte_dados, cnpj_companhia, data_referencia_doc, data_doc, mes_doc, ano_doc)
);



DROP INDEX IF EXISTS idx_unico_demonstrativo_financeiro;

CREATE UNIQUE INDEX idx_unico_demonstrativo_financeiro
ON demonstrativo_financeiro (
    cnpj_companhia,
    codigo_conta,
    grupo_dfp,
    conta_fixa,
    mes_doc,
    ano_doc
);

DROP INDEX IF EXISTS idx_unico_informacao_trimestral;

CREATE UNIQUE INDEX idx_unico_informacao_trimestral
ON informacao_trimestral (
    cnpj_companhia,
    codigo_conta,
    grupo_dfp,
    conta_fixa,
    mes_doc,
    ano_doc
);