# from datetime import datetime
from collectors.coletor_cvm import Coletor_cvm
# from models.demonstrativo_financeiro import Demonstrativo_financeiro
# from models.empresas import Empresas
# from models.grupo_demonstrativo_financeiro import Grupo_demonstrativo_financeiro
# from models.informacao_trimestral import Informacao_trimestral
# from models.planos_contas import Planos_contas


def main():
    # empresa = Empresas(
    #     "dogmatic",
    #     "47184",
    #     "63.765.372/0001-53",
    #     "unleash B2C e-tailers",
    #     "systematized",
    #     217544,
    #     9,
    #     "Silva Ltda.",
    #     "Oliveira S.A.",
    #     "http://www.lee.com",
    #     "Portugal",
    #     "Argentina",
    #     "generate synergistic solutions",
    #     "Suspenso",
    #     "Registrado",
    #     "9",
    #     "2015-06-15",
    #     "2001-10-21",
    #     "2020-04-28",
    #     "2019-02-13",
    #     "2005-12-01",
    #     "2012-09-04",
    #     "2016-03-19",
    #     "2021-11-25",
    #     "2009-05-11",
    #     15,
    #     "2024-02-28",
    #     "December",
    #     "2016",
    # )
    # empresa.mostrarDados()

    # print("\n\nDados DPF\n---------")

    # demotracao = Demonstrativo_financeiro(
    #     "12.345.678-9",
    #     "63.765.372/0001-53",
    #     "47184",
    #     "BRL",
    #     3,
    #     986,
    #     "2023",
    #     "115",
    #     2,
    #     datetime(2023, 1, 1).date(),
    #     datetime(2023, 12, 31).date(),
    #     datetime(2023, 12, 31).date(),
    #     159.75,
    #     datetime(2023, 12, 31).date(),
    #     "December",
    #     "2023",
    # )
    # demotracao.mostrarDados()

    # print("\n\nDados Planos de Contas\n---------")
    # plano = Planos_contas("32541", "Conta teste")
    # plano.mostrarDados()

    # print("\n\nDados Grupo DPF\n---------")
    # dfp = Grupo_demonstrativo_financeiro(2, "Balanço patrimonial ativo")
    # dfp.mostrarDados()

    # print("\n\nDados ITR\n---------")
    # itr = Informacao_trimestral(
    #     "12.345.678-9",
    #     "63.765.372/0001-53",
    #     "47184",
    #     "BRL",
    #     3,
    #     986,
    #     "2023",
    #     "115",
    #     2,
    #     datetime(2023, 1, 1).date(),
    #     datetime(2023, 12, 31).date(),
    #     datetime(2023, 12, 31).date(),
    #     159.75,
    #     datetime(2023, 12, 31).date(),
    #     "December",
    #     "2023",
    # )
    # itr.mostrarDados()

    coletor = Coletor_cvm()
    coletor.mostrarDados()


if __name__ == "__main__":
    main()
