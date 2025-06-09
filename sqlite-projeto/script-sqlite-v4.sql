-- ==========================
-- TABELAS AUXILIARES
-- ==========================

-- Tabela de categorias de documento (usada em diversas tabelas principais para padronizar categorias)
CREATE TABLE categoria_documento (
  id_categoria_doc   INTEGER PRIMARY KEY,      -- Identificador único da categoria de documento
  descricao          TEXT    UNIQUE NOT NULL    -- Descrição da categoria (ex.: 'BPA', 'DFP', 'ITR' etc.)
);

-- Tabela de tipos de parecer (utilizada em parecer_demonstrativo e parecer_trimestral para padronização)
CREATE TABLE tipo_parecer (
  id_tipo_parecer    INTEGER PRIMARY KEY,       -- Identificador único do tipo de parecer
  descricao          TEXT    UNIQUE NOT NULL     -- Descrição do tipo de parecer (ex.: 'Auditor Independente', 'Revisor Fiscal' etc.)
);

-- Tabela de tipos de relatório de auditoria em demonstrativos financeiros
CREATE TABLE tipo_relatorio_auditor (
  id_tipo_rel_auditor   INTEGER PRIMARY KEY,    -- Identificador único do tipo de relatório de auditoria
  descricao             TEXT    UNIQUE NOT NULL -- Descrição do relatório (ex.: 'Com Certificação', 'Sem Certificação' etc.)
);

-- Tabela de tipos de relatório especial para parecer trimestral
CREATE TABLE tipo_relatorio_especial (
  id_tipo_rel_especial  INTEGER PRIMARY KEY,    -- Identificador único do tipo de relatório especial
  descricao             TEXT    UNIQUE NOT NULL -- Descrição do relatório especial (ex.: 'Parecer Exigido', 'Parecer Facultativo' etc.)
);

-- Tabela de assuntos para periódicos eventuais (padroniza valores de assunto)
CREATE TABLE assunto_prensa (
  id_assunto          INTEGER PRIMARY KEY,      -- Identificador único do assunto
  descricao           TEXT    UNIQUE NOT NULL   -- Descrição do assunto (ex.: 'Assembleia Geral', 'Fato Relevante' etc.)
);

-- Tabela de espécies de documento para periódicos eventuais
CREATE TABLE especie_documento_eventual (
  id_especie_eventual INTEGER PRIMARY KEY,      -- Identificador único da espécie de documento eventual
  descricao           TEXT    UNIQUE NOT NULL   -- Descrição da espécie (ex.: 'Ofício', 'Carta Circular' etc.)
);

-- Tabela de tipos de eventos/periódicos (campo tipo em periodicos_eventuais)
CREATE TABLE tipo_evento (
  id_tipo_evento      INTEGER PRIMARY KEY,      -- Identificador único do tipo de evento
  descricao           TEXT    UNIQUE NOT NULL   -- Descrição do tipo de evento (ex.: 'Reunião de Conselho', 'Informação Contábil' etc.)
);

-- Tabela de tipos de apresentação para periódicos eventuais
CREATE TABLE tipo_apresentacao_evento (
  id_tipo_apres       INTEGER PRIMARY KEY,      -- Identificador único do tipo de apresentação
  descricao           TEXT    UNIQUE NOT NULL   -- Descrição do tipo (ex.: 'Eletrônico', 'Impresso' etc.)
);

-- Tabela de escala monetária (normaliza valores de escala, ex.: mil, milhão, etc.)
CREATE TABLE escala_monetaria (
  id_escala   INTEGER PRIMARY KEY,        -- Identificador da escala monetária
  descricao   TEXT    UNIQUE NOT NULL     -- Descrição da escala (ex.: 'Mil', 'Milhão' etc.)
);

-- Tabela de ordem de exercício (normaliza ordem dos exercícios, ex.: 'Exercício Atual', 'Exercício Anterior' etc.)
CREATE TABLE ordem_exercicio (
  id_ordem    INTEGER PRIMARY KEY,        -- Identificador da ordem de exercício
  descricao   TEXT    UNIQUE NOT NULL     -- Descrição da ordem de exercício
);

-- Tabela de moedas (padroniza moedas, ex.: 'BRL', 'USD' etc.)
CREATE TABLE moeda (
  id_moeda    INTEGER PRIMARY KEY,        -- Identificador da moeda
  descricao   TEXT    UNIQUE NOT NULL     -- Descrição completa da moeda (ex.: 'Real Brasileiro', 'Dólar Americano' etc.)
);

-- Tabela de espécies de controle acionário (padroniza tipos de controle, ex.: 'Estatal', 'Privado', etc.)
CREATE TABLE especie_controle (
  id_especie  INTEGER PRIMARY KEY,        -- Identificador da espécie de controle
  descricao   TEXT    UNIQUE NOT NULL     -- Descrição da espécie (ex.: 'Estatal', 'Privado' etc.)
);

-- Tabela de situação do emissor (padroniza status do emissor, ex.: 'Ativo', 'Inativo' etc.)
CREATE TABLE situacao_emissor (
  id_situacao INTEGER PRIMARY KEY,        -- Identificador da situação do emissor
  descricao   TEXT    UNIQUE NOT NULL     -- Descrição da situação do emissor (ex.: 'Ativo', 'Inativo' etc.)
);

-- Tabela de setor de atividade (padroniza setores econômicos, ex.: 'Financeiro', 'Industrial' etc.)
CREATE TABLE setor_atividade (
  id_setor    INTEGER PRIMARY KEY,        -- Identificador do setor de atividade
  descricao   TEXT    UNIQUE NOT NULL     -- Descrição do setor (ex.: 'Financeiro', 'Industrial' etc.)
);


-- ==========================
-- TABELAS PRINCIPAIS
-- ==========================

-- ========== empresas ==========
-- Armazena dados cadastrais de cada empresa (companhias abertas) com referências a tabelas auxiliares
CREATE TABLE empresas (
  codigo_cvm                              TEXT    NOT NULL,     -- Código CVM único da empresa
  cnpj_companhia                          TEXT    NOT NULL,     -- CNPJ da empresa
  nome_empresa                            TEXT,                 -- Nome atual da empresa
  nome_anterior_empresa                   TEXT,                 -- Nome anterior, se houver
  descricao_atividade                     TEXT,                 -- Descrição das atividades da empresa
  identificador_documento                 INTEGER,
  id_especie                              INTEGER,              -- FK para especie_controle(id_especie)
  id_situacao                             INTEGER,              -- FK para situacao_emissor(id_situacao)
  id_setor                                INTEGER,              -- FK para setor_atividade(id_setor)
  id_categoria_doc                        INTEGER,              -- FK para categoria_documento(id_categoria_doc)
  versao                                  INTEGER,              -- Versão do registro
  pagina_web                              TEXT,                 -- URL do site da empresa
  pais_origem                             TEXT,                 -- País de origem da empresa
  situacao_registro_cvm                   TEXT,
  pais_custodia_valores_mobiliarios       TEXT,                 -- País de custódia de valores mobiliários
  mes_encerramento_exercicio_social       INTEGER,              -- Mês de encerramento do exercício (1-12)
  dia_encerramento_exercicio_social       INTEGER,              -- Dia de encerramento do exercício social
  data_constituicao                       DATE,                 -- Data de constituição da empresa
  data_situacao_emissor                   DATE,                 -- Data de mudança de situação do emissor
  data_registro_cvm                       DATE,                 -- Data de registro na CVM
  data_categoria_registro_cvm             DATE,                 -- Data da categoria de registro CVM
  data_situacao_registro_cvm              DATE,                 -- Data da situação de registro CVM
  data_nome_empresarial                   DATE,                 -- Data de alteração de nome empresarial
  data_especie_controle_acionario         DATE,                 -- Data de alteração de espécie de controle acionário
  data_alteracao_exercicio_social         DATE,                 -- Data de alteração de exercício social
  data_referencia_documento               DATE,                 -- Data de referência do documento
  data_hora_insercao                      DATETIME,             -- Timestamp de inserção do registro
  data_hora_atualizacao                   DATETIME,             -- Timestamp de última atualização do registro
  mes                                     INTEGER NOT NULL,     -- Mês extraído de data_doc (1-12)
  ano                                     INTEGER NOT NULL,     -- Ano extraído de data_doc (ex.: 2020, 2021 etc.)

  -- Chave primária composta por cnpj_companhia, ano e mes
  PRIMARY KEY(cnpj_companhia, ano, mes),

  -- Chaves estrangeiras
  FOREIGN KEY (id_categoria_doc) REFERENCES categoria_documento(id_categoria_doc),
  FOREIGN KEY (id_especie)       REFERENCES especie_controle(id_especie),
  FOREIGN KEY (id_situacao)      REFERENCES situacao_emissor(id_situacao),
  FOREIGN KEY (id_setor)         REFERENCES setor_atividade(id_setor)
);

-- ========== planos_contas ==========
-- Define o plano de contas utilizado nos demonstrativos e informações trimestrais
CREATE TABLE planos_contas (
  id_plano_conta INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador interno do plano de contas
  codigo_conta     TEXT    NOT NULL UNIQUE,           -- Código do plano de contas (ex.: '1', '1.01', etc.)
  descricao_conta  TEXT    NOT NULL,                  -- Descrição da conta (ex.: 'Ativo Total', 'Passivo Circulante' etc.)
  comportamento    TEXT    NOT NULL                   -- Tipo de comportamento (ex.: 'BPA', 'DRE', 'DVA' etc.)
);

-- ========== grupo_demonstrativo_financeiro ==========
-- Mapeia os grupos de demonstrativos financeiros (ex.: BPA_IND, DRE_CON, etc.)
CREATE TABLE grupo_demonstrativo_financeiro (
  codigo_grupo_dfp TEXT    PRIMARY KEY, -- Código do grupo de DFP (ex.: 'BPA_IND')
  grupo_dfp        TEXT    NOT NULL    -- Descrição do grupo (ex.: 'DF Individual - Ativo', 'DF Consolidado - Passivo' etc.)
);

-- ========== demonstrativo_financeiro ==========
-- Armazena itens dos demonstrativos financeiros (DFP) vinculados a empresas e planos de contas
CREATE TABLE demonstrativo_financeiro (
  id_demonstrativo         INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador interno do registro
  cnpj_companhia           TEXT    NOT NULL,                  -- FK para empresas(cnpj_companhia, ano, mes)
  id_plano_conta         INTEGER NOT NULL,                  -- FK para planos_contas(id_planos_contas)
  id_escala                INTEGER,                           -- FK para escala_monetaria(id_escala)
  codigo_grupo_dfp         TEXT    NOT NULL,                  -- FK para grupo_demonstrativo_financeiro(codigo_grupo_dfp)
  id_moeda                 INTEGER,                           -- FK para moeda(id_moeda)
  id_ordem                 INTEGER,                           -- FK para ordem_exercicio(id_ordem)
  conta_fixa               TEXT,                              -- Indica se a conta é fixa (por exemplo, 'Y' ou valor específico)
  versao                   INTEGER,                           -- Versão do demonstrativo
  data_inicio_exercicio    DATE,                              -- Data de início do exercício considerado
  data_fim_exercicio       DATE,                              -- Data de fim do exercício considerado
  data_referencia_doc      DATE,                              -- Data de referência do documento
  valor_conta              REAL,                              -- Valor monetário do item
  mes                      INTEGER NOT NULL,                  -- Mês extraído de data_doc (1-12)
  ano                      INTEGER NOT NULL,                  -- Ano extraído de data_doc (ex.: 2020, 2021 etc.)
  FOREIGN KEY (cnpj_companhia, ano, mes)      REFERENCES empresas(cnpj_companhia, ano, mes),
  FOREIGN KEY (id_plano_conta)      REFERENCES planos_contas(id_plano_conta),
  FOREIGN KEY (codigo_grupo_dfp)    REFERENCES grupo_demonstrativo_financeiro(codigo_grupo_dfp),
  FOREIGN KEY (id_escala)           REFERENCES escala_monetaria(id_escala),
  FOREIGN KEY (id_moeda)            REFERENCES moeda(id_moeda),
  FOREIGN KEY (id_ordem)            REFERENCES ordem_exercicio(id_ordem)
);

-- ========== informacao_trimestral ==========
-- Armazena itens de informações trimestrais (ITR) com lógica idêntica a demonstrativo_financeiro
CREATE TABLE informacao_trimestral (
  id_informacao_trimestral  INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador interno do registro
  cnpj_companhia            TEXT    NOT NULL,                 -- FK para empresas(cnpj_companhia, ano, mes)
  id_plano_conta            INTEGER NOT NULL,                 -- FK para planos_contas(id_planos_contas)
  id_escala                 INTEGER,                          -- FK para escala_monetaria(id_escala)
  codigo_grupo_dfp          TEXT    NOT NULL,                 -- FK para grupo_demonstrativo_financeiro(codigo_grupo_dfp)
  id_moeda                  INTEGER,                          -- FK para moeda(id_moeda)
  id_ordem                  INTEGER,                          -- FK para ordem_exercicio(id_ordem)
  conta_fixa                TEXT,                             -- Conta fixa, se aplicável
  versao                    INTEGER,                          -- Versão do ITR
  data_inicio_exercicio     DATE,                             -- Data de início do exercício trimestral
  data_fim_exercicio        DATE,                             -- Data de fim do exercício trimestral
  data_referencia_doc       DATE,                             -- Data de referência do documento
  valor_conta               REAL,                             -- Valor contabilizado
  mes                       INTEGER NOT NULL,                 -- Mês extraído de data_doc (1-12)
  ano                       INTEGER NOT NULL,                 -- Ano extraído de data_doc (ex.: 2020, 2021 etc.)
  FOREIGN KEY (cnpj_companhia, ano, mes)      REFERENCES empresas(cnpj_companhia, ano, mes),
  FOREIGN KEY (id_plano_conta)      REFERENCES planos_contas(id_plano_conta),
  FOREIGN KEY (codigo_grupo_dfp)    REFERENCES grupo_demonstrativo_financeiro(codigo_grupo_dfp),
  FOREIGN KEY (id_escala)           REFERENCES escala_monetaria(id_escala),
  FOREIGN KEY (id_moeda)            REFERENCES moeda(id_moeda),
  FOREIGN KEY (id_ordem)            REFERENCES ordem_exercicio(id_ordem)
);

-- ========== parecer_demonstrativo ==========
-- Armazena texto de parecer sobre demonstrativos financeiros (DFP) de cada empresa
CREATE TABLE parecer_demonstrativo (
  id_parecer_demonstrativo          INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador interno do parecer
  cnpj_companhia                    TEXT    NOT NULL,                   -- FK para empresas(cnpj_companhia, ano, mes)
  num_linha_parecer_declaracao      INTEGER,                            -- Número da linha do texto do Parecer/Declaração
  id_tipo_parecer                   INTEGER,                            -- FK para tipo_parecer(id_tipo_parecer)
  id_tipo_rel_auditor               INTEGER,                            -- FK para tipo_relatorio_auditor(id_tipo_rel_auditor)
  texto_parecer_declaracao          TEXT,                               -- Texto completo do parecer/declaracao
  versao                            INTEGER,                            -- Versão do parecer
  data_referencia_doc               DATE,                               -- Data de referência do documento
  mes                               INTEGER NOT NULL,                   -- Mês extraído de data_doc (1-12)
  ano                               INTEGER NOT NULL,                   -- Ano extraído de data_doc (ex.: 2020, 2021 etc.)
  FOREIGN KEY (cnpj_companhia, ano, mes)      REFERENCES empresas(cnpj_companhia, ano, mes),
  FOREIGN KEY (id_tipo_parecer)    REFERENCES tipo_parecer(id_tipo_parecer),
  FOREIGN KEY (id_tipo_rel_auditor)REFERENCES tipo_relatorio_auditor(id_tipo_rel_auditor)
);

-- ========== parecer_trimestral ==========
-- Armazena texto de parecer trimestral (ITR) de cada empresa
CREATE TABLE parecer_trimestral (
  id_parecer_trimestral             INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador interno do parecer trimestral
  cnpj_companhia                    TEXT    NOT NULL,                   -- FK para empresas(cnpj_companhia, ano, mes)
  num_linha_parecer_declaracao      INTEGER,                            -- Número da linha do texto do Parecer/Declaração
  id_tipo_parecer                   INTEGER,                            -- FK para tipo_parecer(id_tipo_parecer)
  id_tipo_rel_especial              INTEGER,                            -- FK para tipo_relatorio_especial(id_tipo_rel_especial)
  texto_parecer_declaracao          TEXT,                               -- Texto completo do parecer/declaracao
  versao                            INTEGER,                            -- Versão do parecer
  data_referencia_doc               DATE,                               -- Data de referência do documento
  mes                               INTEGER NOT NULL,                   -- Mês extraído de data_doc (1-12)
  ano                               INTEGER NOT NULL,                   -- Ano extraído de data_doc (ex.: 2020, 2021 etc.)
  FOREIGN KEY (cnpj_companhia, ano, mes)      REFERENCES empresas(cnpj_companhia, ano, mes),
  FOREIGN KEY (id_tipo_parecer)    REFERENCES tipo_parecer(id_tipo_parecer),
  FOREIGN KEY (id_tipo_rel_especial) REFERENCES tipo_relatorio_especial(id_tipo_rel_especial)
);

-- ========== formulario_referencia ==========
-- Armazena metadados de formulários de referência (FRE) de cada empresa
CREATE TABLE formulario_referencia (
  id_formulario      INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador interno do formulário
  cnpj_companhia     TEXT    NOT NULL,                   -- FK para empresas(cnpj_companhia, ano, mes)
  id_categoria_doc   INTEGER,                            -- FK para categoria_documento(id_categoria_doc)
  id_doc             INTEGER,                            -- Identificador numérico do documento (se houver lógica interna)
  link_doc           TEXT,                               -- URL para download do documento
  versao             REAL,                               -- Versão do documento
  data_recebimento   DATE,                               -- Data em que o documento foi recebido
  data_referencia    DATE,                               -- Data de referência do documento
  data_doc           DATE    NOT NULL,                   -- Data do próprio documento
  mes                INTEGER NOT NULL,                   -- Mês extraído de data_doc (1-12)
  ano                INTEGER NOT NULL,                   -- Ano extraído de data_doc (ex.: 2020, 2021 etc.)
  FOREIGN KEY (cnpj_companhia, ano, mes)      REFERENCES empresas(cnpj_companhia, ano, mes),
  FOREIGN KEY (id_categoria_doc) REFERENCES categoria_documento(id_categoria_doc)
);

-- ========== periodicos_eventuais ==========
-- Armazena comunicados/periódicos eventuais publicados pelas empresas
CREATE TABLE periodicos_eventuais (
  id_periodico_eventual INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador interno do periódico eventual
  cnpj_companhia        TEXT    NOT NULL,                  -- FK para empresas(cnpj_companhia, ano, mes)
  id_assunto            INTEGER,                           -- FK para assunto_prensa(id_assunto)
  id_categoria_doc      INTEGER,                           -- FK para categoria_documento(id_categoria_doc)
  id_especie_eventual   INTEGER,                           -- FK para especie_documento_eventual(id_especie_eventual)
  link_doc              TEXT,                              -- URL do documento
  protocolo_entrega     TEXT,
  id_tipo_evento        INTEGER,                           -- FK para tipo_evento(id_tipo_evento)
  id_tipo_apres         INTEGER,                           -- FK para tipo_apresentacao_evento(id_tipo_apres)
  versao                INTEGER,                           -- Versão do documento
  data_entrega          DATE,                              -- Data de entrega/publicação do documento
  data_referencia       DATE,                              -- Data de referência do documento
  data_doc              DATE    NOT NULL,                  -- Data do documento
  mes                   INTEGER NOT NULL,                  -- Mês extraído de data_doc (1-12)
  ano                   INTEGER NOT NULL,                  -- Ano extraído de data_doc (ex.: 2020, 2021 etc.)
  FOREIGN KEY (cnpj_companhia, ano, mes)      REFERENCES empresas(cnpj_companhia, ano, mes),
  FOREIGN KEY (id_assunto)            REFERENCES assunto_prensa(id_assunto),
  FOREIGN KEY (id_categoria_doc)      REFERENCES categoria_documento(id_categoria_doc),
  FOREIGN KEY (id_especie_eventual)   REFERENCES especie_documento_eventual(id_especie_eventual),
  FOREIGN KEY (id_tipo_evento)        REFERENCES tipo_evento(id_tipo_evento),
  FOREIGN KEY (id_tipo_apres)         REFERENCES tipo_apresentacao_evento(id_tipo_apres)
);

-- ========== numeros_acoes ==========
-- Registra a quantidade de ações de cada empresa (ordinárias, preferenciais e totais)
CREATE TABLE numeros_acoes (
  id_numeros_acoes      INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador interno do registro
  fonte_dados           TEXT    NOT NULL,                  -- Fonte dos dados (ex.: 'ITR', 'BPA' etc.)
  cnpj_companhia        TEXT    NOT NULL,                  -- FK para empresas(cnpj_companhia, ano, mes)
  qtd_acoes_ordinarias_capital_integralizado      INTEGER, -- Quantidade de ações ordinárias em capital integralizado
  qtd_acoes_preferenciais_capital_integralizado   INTEGER, -- Quantidade de ações preferenciais em capital integralizado
  qtd_total_acoes_capital_integralizado            INTEGER, -- Quantidade total de ações em capital integralizado
  qtd_acoes_ordinarias_tesouro                     INTEGER, -- Quantidade de ações ordinárias em tesouraria
  qtd_acoes_preferenciais_tesouro                  INTEGER, -- Quantidade de ações preferenciais em tesouraria
  qtd_total_acoes_tesouro                          INTEGER, -- Quantidade total de ações em tesouraria
  versao                  INTEGER,                     -- Versão do relatório
  data_referencia         DATE,                        -- Data de referência do documento
  mes                     INTEGER NOT NULL,            -- Mês extraído de data_doc (1-12)
  ano                     INTEGER NOT NULL,            -- Ano extraído de data_doc (ex.: 2020, 2021 etc.)
  FOREIGN KEY (cnpj_companhia, ano, mes)      REFERENCES empresas(cnpj_companhia, ano, mes),
  UNIQUE (fonte_dados, cnpj_companhia, data_referencia) -- Garante unicidade por fonte, empresa e datas
);

-- ==========================
-- ÍNDICES PARA AS NOVAS TABELAS PRINCIPAIS
-- ==========================

-- Índice único no demonstrativo_financeiro para evitar duplicatas
CREATE UNIQUE INDEX idx_unico_demonstrativo_financeiro ON demonstrativo_financeiro (
  cnpj_companhia, 
  id_plano_conta, 
  codigo_grupo_dfp, 
  conta_fixa, 
  mes, 
  ano
);

-- Índice único na informacao_trimestral para evitar duplicatas
CREATE UNIQUE INDEX idx_unico_informacao_trimestral ON informacao_trimestral (
  cnpj_companhia, 
  id_plano_conta, 
  codigo_grupo_dfp, 
  conta_fixa, 
  mes, 
  ano
);

-- ==========================
-- INSERTS
-- ==========================

INSERT INTO grupo_demonstrativo_financeiro (codigo_grupo_dfp, grupo_dfp) VALUES
  ('BPA_IND', 'DF Individual - Ativo'),
  ('BPA_CON', 'DF Consolidado - Ativo'),
  ('BPP_IND', 'DF Individual - Passivo'),
  ('BPP_CON', 'DF Consolidado - Passivo'),
  ('DVA_IND', 'DF Individual - Demonstração de Valor Adicionado'),
  ('DVA_CON', 'DF Consolidado - Demonstração de Valor Adicionado'),
  ('DRE_IND', 'DF Individual - Demonstração do Resultado'),
  ('DRE_CON', 'DF Consolidado - Demonstração do Resultado');

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
