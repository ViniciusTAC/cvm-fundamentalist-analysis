-- LPA - DFP

WITH dados_base AS (
  SELECT
      dfp.cnpj_companhia,
      dfp.id_plano_conta,
      dfp.valor_conta,
      dfp.mes,
      dfp.ano,
      num_acoes.qtd_total_acoes_capital_integralizado,
      num_acoes.qtd_total_acoes_tesouro,
      (num_acoes.qtd_total_acoes_capital_integralizado - num_acoes.qtd_total_acoes_tesouro) AS acoes_em_circulacao
  FROM demonstrativo_financeiro AS dfp
  LEFT JOIN numeros_acoes AS num_acoes 
    ON num_acoes.cnpj_companhia = dfp.cnpj_companhia 
   AND num_acoes.mes = dfp.mes 
   AND num_acoes.ano = dfp.ano
  WHERE dfp.id_plano_conta = '3.13'
)
SELECT
    cnpj_companhia,
    id_plano_conta,
    valor_conta,
    mes,
    ano,
    acoes_em_circulacao,
    valor_conta / acoes_em_circulacao AS lpa
FROM dados_base
WHERE	lpa is not null
ORDER BY ano, mes;




-- ---------------------------------------------------------------------------------------------
-- LPA - ITR

WITH dados_base AS (
  SELECT
      itr.cnpj_companhia,
      itr.id_plano_conta,
      itr.valor_conta,
      itr.mes,
      itr.ano,
      num_acoes.qtd_total_acoes_capital_integralizado,
      num_acoes.qtd_total_acoes_tesouro,
      (num_acoes.qtd_total_acoes_capital_integralizado - num_acoes.qtd_total_acoes_tesouro) AS acoes_em_circulacao
  FROM informacao_trimestral AS itr
  LEFT JOIN numeros_acoes AS num_acoes 
    ON num_acoes.cnpj_companhia = itr.cnpj_companhia 
   AND num_acoes.mes = itr.mes 
   AND num_acoes.ano = itr.ano
  WHERE itr.id_plano_conta = '3.13'
)
SELECT
    cnpj_companhia,
    id_plano_conta,
    valor_conta,
    mes,
    ano,
    acoes_em_circulacao,
    valor_conta / acoes_em_circulacao AS lpa
FROM dados_base
WHERE	lpa is not null
ORDER BY ano, mes;

-- ---------------------------------------------------------------------------------------------
-- ITR

WITH dados_trimestrais AS (
  SELECT
    itr.cnpj_companhia,
    itr.mes,
    itr.ano,
    (na.qtd_total_acoes_capital_integralizado - na.qtd_total_acoes_tesouro) AS acoes_em_circulacao,
    MAX(CASE WHEN itr.id_plano_conta = '3.13'       THEN itr.valor_conta END) AS lucro_liquido,
    MAX(CASE WHEN itr.id_plano_conta = 'Dividendos' THEN itr.valor_conta END) AS dividendos,
    MAX(CASE WHEN itr.id_plano_conta = '1.01'       THEN itr.valor_conta END) AS ativo_circulante,
    MAX(CASE WHEN itr.id_plano_conta = '2.01'       THEN itr.valor_conta END) AS passivo_circulante,
    MAX(CASE WHEN itr.id_plano_conta = '2.02'       THEN itr.valor_conta END) AS passivo_nao_circulante,
    MAX(CASE WHEN itr.id_plano_conta = '1.01.01'    THEN itr.valor_conta END) AS disponibilidades
  FROM informacao_trimestral itr
  LEFT JOIN numeros_acoes na
    ON na.cnpj_companhia = itr.cnpj_companhia
   AND na.mes           = itr.mes
   AND na.ano           = itr.ano
  WHERE itr.id_plano_conta IN (
    '3.13','Dividendos','1.01','1.01.01','2.01','2.02'
  )
  GROUP BY
    itr.cnpj_companhia,
    itr.mes,
    itr.ano,
    na.qtd_total_acoes_capital_integralizado,
    na.qtd_total_acoes_tesouro
)
SELECT
  d.cnpj_companhia,
  d.ano,
  d.mes,
  d.acoes_em_circulacao,

  -- 1) LPA
  d.lucro_liquido   / NULLIF(d.acoes_em_circulacao,0)             AS lpa,

  -- 2) Liquidez Corrente
  d.ativo_circulante / NULLIF(d.passivo_circulante,0)            AS lc,

  -- 3) Dívida Bruta
  (d.passivo_circulante + d.passivo_nao_circulante)              AS db,

  -- 4) Dívida Líquida
  (d.passivo_circulante + d.passivo_nao_circulante)
    - d.disponibilidades                                         AS dl


FROM dados_trimestrais d

WHERE d.lucro_liquido IS NOT NULL

ORDER BY d.ano, d.mes;


-------------------------- 
-- DFP
WITH dados_trimestrais AS (
  SELECT
    dfp.cnpj_companhia,
    dfp.mes,
    dfp.ano,
    (na.qtd_total_acoes_capital_integralizado - na.qtd_total_acoes_tesouro) AS acoes_em_circulacao,
    MAX(CASE WHEN dfp.id_plano_conta = '3.13'       THEN dfp.valor_conta END) AS lucro_liquido,
    MAX(CASE WHEN dfp.id_plano_conta = 'Dividendos' THEN dfp.valor_conta END) AS dividendos,
    MAX(CASE WHEN dfp.id_plano_conta = '1.01'       THEN dfp.valor_conta END) AS ativo_circulante,
    MAX(CASE WHEN dfp.id_plano_conta = '2.01'       THEN dfp.valor_conta END) AS passivo_circulante,
    MAX(CASE WHEN dfp.id_plano_conta = '2.02'       THEN dfp.valor_conta END) AS passivo_nao_circulante,
    MAX(CASE WHEN dfp.id_plano_conta = '1.01.01'    THEN dfp.valor_conta END) AS disponibilidades
  FROM demonstrativo_financeiro dfp
  LEFT JOIN numeros_acoes na
    ON na.cnpj_companhia = dfp.cnpj_companhia
   AND na.mes           = dfp.mes
   AND na.ano           = dfp.ano
  WHERE dfp.id_plano_conta IN (
    '3.13','Dividendos','1.01','1.01.01','2.01','2.02'
  )
  GROUP BY
    dfp.cnpj_companhia,
    dfp.mes,
    dfp.ano,
    na.qtd_total_acoes_capital_integralizado,
    na.qtd_total_acoes_tesouro
)
SELECT
  d.cnpj_companhia,
  d.ano,
  d.mes,
  d.acoes_em_circulacao,

  -- 1) LPA
  d.lucro_liquido   / NULLIF(d.acoes_em_circulacao,0)             AS lpa,

  -- 2) Liquidez Corrente
  d.ativo_circulante / NULLIF(d.passivo_circulante,0)            AS lc,

  -- 3) Dívida Bruta
  (d.passivo_circulante + d.passivo_nao_circulante)              AS db,

  -- 4) Dívida Líquida
  (d.passivo_circulante + d.passivo_nao_circulante)
    - d.disponibilidades                                         AS dl


FROM dados_trimestrais d

WHERE d.lucro_liquido IS NOT NULL

ORDER BY d.ano, d.mes;
