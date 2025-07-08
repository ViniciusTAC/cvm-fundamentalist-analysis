CREATE TABLE IF NOT EXISTS analise_itr (
  cnpj_companhia TEXT NOT NULL,
  ano INTEGER NOT NULL,
  mes INTEGER NOT NULL,
  acoes_em_circulacao REAL,
  lpa REAL,
  lc REAL,
  db REAL,
  dl REAL,
  data_hora_insercao DATETIME NOT NULL,
  data_hora_atualizacao DATETIME,
  PRIMARY KEY (cnpj_companhia, ano, mes)
);


CREATE TABLE IF NOT EXISTS analise_dfp (
  cnpj_companhia TEXT NOT NULL,
  ano INTEGER NOT NULL,
  mes INTEGER NOT NULL,
  acoes_em_circulacao REAL,
  lpa REAL,
  lc REAL,
  db REAL,
  dl REAL,
  data_hora_insercao DATETIME NOT NULL,
  data_hora_atualizacao DATETIME,
  PRIMARY KEY (cnpj_companhia, ano, mes)
);


-- ---------------------------------------------------------------------------------------------
-- ITR
WITH escala_fatores AS (
  SELECT 
    id_escala,
    CASE descricao
      WHEN 'MIL' THEN 1e3
      WHEN 'UNIDADE' THEN 1e0
      ELSE 1
    END AS fator
  FROM escala_monetaria
),
dados_trimestrais AS (
  SELECT
    itr.cnpj_companhia,
    itr.mes,
    itr.ano,
    (na.qtd_total_acoes_capital_integralizado - na.qtd_total_acoes_tesouro) AS acoes_em_circulacao,

    MAX(CASE WHEN pc.codigo_conta = '3.13'       THEN itr.valor_conta * COALESCE(ef.fator, 1) END) AS lucro_liquido,
    MAX(CASE WHEN pc.codigo_conta = 'Dividendos' THEN itr.valor_conta * COALESCE(ef.fator, 1) END) AS dividendos,
    MAX(CASE WHEN pc.codigo_conta = '1.01'       THEN itr.valor_conta * COALESCE(ef.fator, 1) END) AS ativo_circulante,
    MAX(CASE WHEN pc.codigo_conta = '2.01'       THEN itr.valor_conta * COALESCE(ef.fator, 1) END) AS passivo_circulante,
    MAX(CASE WHEN pc.codigo_conta = '2.02'       THEN itr.valor_conta * COALESCE(ef.fator, 1) END) AS passivo_nao_circulante,
    MAX(CASE WHEN pc.codigo_conta = '1.01.01'    THEN itr.valor_conta * COALESCE(ef.fator, 1) END) AS disponibilidades

  FROM informacao_trimestral itr
  LEFT JOIN planos_contas pc ON pc.codigo_conta = itr.id_plano_conta
  LEFT JOIN escala_fatores ef ON ef.id_escala = itr.id_escala
  LEFT JOIN numeros_acoes na 
    ON na.cnpj_companhia = itr.cnpj_companhia 
   AND na.mes = itr.mes 
   AND na.ano = itr.ano

  WHERE pc.codigo_conta IN ('3.13','Dividendos','1.01','2.01','2.02','1.01.01')

  GROUP BY itr.cnpj_companhia, itr.mes, itr.ano,
           na.qtd_total_acoes_capital_integralizado,
           na.qtd_total_acoes_tesouro
)

SELECT
  d.cnpj_companhia,
  d.ano,
  d.mes,
  d.acoes_em_circulacao,

  -- 1) LPA
  d.lucro_liquido / NULLIF(d.acoes_em_circulacao, 0)               AS lpa,

  -- 2) Liquidez Corrente
  d.ativo_circulante / NULLIF(d.passivo_circulante, 0)            AS lc,

  -- 3) Dívida Bruta
  (d.passivo_circulante + d.passivo_nao_circulante)              AS db,

  -- 4) Dívida Líquida
  (d.passivo_circulante + d.passivo_nao_circulante)
    - d.disponibilidades                                         AS dl

FROM dados_trimestrais d
WHERE d.lucro_liquido IS NOT NULL
ORDER BY d.ano, d.mes;










-- ---------------------------------------------------------------------------------------------
-- DFP
WITH escala_fatores AS (
  SELECT 
    id_escala,
    CASE descricao
      WHEN 'MIL' THEN 1e3
      WHEN 'UNIDADE' THEN 1e0
      ELSE 1
    END AS fator
  FROM escala_monetaria
),
dados_anuais AS (
  SELECT
    dfp.cnpj_companhia,
    dfp.mes,
    dfp.ano,
    (na.qtd_total_acoes_capital_integralizado - na.qtd_total_acoes_tesouro) AS acoes_em_circulacao,

    MAX(CASE WHEN pc.codigo_conta = '3.13'       THEN dfp.valor_conta * COALESCE(ef.fator, 1) END) AS lucro_liquido,
    MAX(CASE WHEN pc.codigo_conta = 'Dividendos' THEN dfp.valor_conta * COALESCE(ef.fator, 1) END) AS dividendos,
    MAX(CASE WHEN pc.codigo_conta = '1.01'       THEN dfp.valor_conta * COALESCE(ef.fator, 1) END) AS ativo_circulante,
    MAX(CASE WHEN pc.codigo_conta = '2.01'       THEN dfp.valor_conta * COALESCE(ef.fator, 1) END) AS passivo_circulante,
    MAX(CASE WHEN pc.codigo_conta = '2.02'       THEN dfp.valor_conta * COALESCE(ef.fator, 1) END) AS passivo_nao_circulante,
    MAX(CASE WHEN pc.codigo_conta = '1.01.01'    THEN dfp.valor_conta * COALESCE(ef.fator, 1) END) AS disponibilidades

  FROM demonstrativo_financeiro dfp
  LEFT JOIN planos_contas pc ON pc.codigo_conta = dfp.id_plano_conta
  LEFT JOIN escala_fatores ef ON ef.id_escala = dfp.id_escala
  LEFT JOIN numeros_acoes na 
    ON na.cnpj_companhia = dfp.cnpj_companhia 
   AND na.mes = dfp.mes 
   AND na.ano = dfp.ano

  WHERE pc.codigo_conta IN ('3.13','Dividendos','1.01','2.01','2.02','1.01.01')

  GROUP BY dfp.cnpj_companhia, dfp.mes, dfp.ano,
           na.qtd_total_acoes_capital_integralizado,
           na.qtd_total_acoes_tesouro
)

SELECT
  d.cnpj_companhia,
  d.ano,
  d.mes,
  d.acoes_em_circulacao,

  -- 1) LPA
  d.lucro_liquido / NULLIF(d.acoes_em_circulacao, 0)               AS lpa,

  -- 2) Liquidez Corrente
  d.ativo_circulante / NULLIF(d.passivo_circulante, 0)            AS lc,

  -- 3) Dívida Bruta
  (d.passivo_circulante + d.passivo_nao_circulante)              AS db,

  -- 4) Dívida Líquida
  (d.passivo_circulante + d.passivo_nao_circulante)
    - d.disponibilidades                                         AS dl

FROM dados_anuais d
WHERE d.lucro_liquido IS NOT NULL
ORDER BY d.ano, d.mes;