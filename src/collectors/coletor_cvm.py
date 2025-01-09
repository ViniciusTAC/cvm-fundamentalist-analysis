class Coletor_cvm:
    # Links principais para os dados da CVM
    links_cvm = [
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FCA/DADOS/",
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/",
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/",
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FRE/DADOS/",
        "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/IPE/DADOS/",
    ]

    # Modelo para organizar as informações
    class relacao_cvm_model:
        def __init__(self, descricao, link, arquivos, tabela):
            """
            :param descricao: Nome da descricao associada.
            :param link: URL base para os dados.
            :param arquivos: Lista de arquivos (ZIPs ou específicos).
            :param tabela: Diretório de tabela.
            """
            self.descricao = descricao
            self.link = link
            self.arquivos = arquivos  # Pode conter ZIPs ou arquivos específicos
            self.tabela = tabela

        def __repr__(self):
            return (
                f"relacao_cvm_model(descricao={self.descricao}, link={self.link}, "
                f"arquivos={self.arquivos}, tabela={self.tabela})"
            )

    # Lista de relações entre dados e arquivos
    lista_relacao = [
        relacao_cvm_model(
            descricao="Informações das empresas na CIA ABERTA",
            link=links_cvm[0],
            arquivos=["fca_cia_aberta_geral_ANO.csv"],
            tabela="empresas",
        ),
        relacao_cvm_model(
            descricao="Demonstrações Financeiras",
            link=links_cvm[1],
            arquivos=[
                "dfp_cia_aberta_DVA_ind_ANO.csv",
                "dfp_cia_aberta_DVA_con_ANO.csv",
                "dfp_cia_aberta_DRE_ind_ANO.csv",
                "dfp_cia_aberta_DRE_con_ANO.csv",
                "dfp_cia_aberta_DRA_ind_ANO.csv",
                "dfp_cia_aberta_DRA_con_ANO.csv",
                "dfp_cia_aberta_DMPL_ind_ANO.csv",
                "dfp_cia_aberta_DMPL_con_ANO.csv",
                "dfp_cia_aberta_DFC_MI_ind_ANO.csv",
                "dfp_cia_aberta_DFC_MI_con_ANO.csv",
                "dfp_cia_aberta_DFC_MD_ind_ANO.csv",
                "dfp_cia_aberta_DFC_MD_con_ANO.csv",
                "dfp_cia_aberta_BPP_ind_ANO.csv",
                "dfp_cia_aberta_BPP_con_ANO.csv",
                "dfp_cia_aberta_BPA_ind_ANO.csv",
                "dfp_cia_aberta_BPA_con_ANO.csv",
                "dfp_cia_aberta_ANO.zip",
            ],
            tabela="demonstrativo_financeiro",
        ),
        relacao_cvm_model(
            descricao="Pareceres das Demonstrações Financeiras",
            link=links_cvm[1],
            arquivos=["dfp_cia_aberta_parecer_ANO.csv", "dfp_cia_aberta_ANO.zip"],
            tabela="parecer_demonstrativo",
        ),
        relacao_cvm_model(
            descricao="Informações Trimestrais",
            link=links_cvm[2],
            arquivos=[
                "itr_cia_aberta_DVA_ind_ANO.csv",
                "itr_cia_aberta_DVA_con_ANO.csv",
                "itr_cia_aberta_DRE_ind_ANO.csv",
                "itr_cia_aberta_DRE_con_ANO.csv",
                "itr_cia_aberta_DRA_ind_ANO.csv",
                "itr_cia_aberta_DRA_con_ANO.csv",
                "itr_cia_aberta_DMPL_ind_ANO.csv",
                "itr_cia_aberta_DMPL_con_ANO.csv",
                "itr_cia_aberta_DFC_MI_ind_ANO.csv",
                "itr_cia_aberta_DFC_MI_con_ANO.csv",
                "itr_cia_aberta_DFC_MD_ind_ANO.csv",
                "itr_cia_aberta_DFC_MD_con_ANO.csv",
                "itr_cia_aberta_BPP_ind_ANO.csv",
                "itr_cia_aberta_BPP_con_ANO.csv",
                "itr_cia_aberta_BPA_ind_ANO.csv",
                "itr_cia_aberta_BPA_con_ANO.csv",
                "itr_cia_aberta_ANO.zip",
            ],
            tabela="informacao_trimestral",
        ),
        relacao_cvm_model(
            descricao="Pareceres das Informações Trimestrais",
            link=links_cvm[2],
            arquivos=["itr_cia_aberta_parecer_ANO.csv", "itr_cia_aberta_ANO.zip"],
            tabela="parecer_trimestral",
        ),
        relacao_cvm_model(
            descricao="Periódicos e Eventuais",
            link=links_cvm[4],
            arquivos=["ipe_cia_aberta_ANO.csv", "ipe_cia_aberta_ANO.zip"],
            tabela="periodicos_eventuais",
        ),
        relacao_cvm_model(
            descricao="Formulário de Referência",
            link=links_cvm[3],
            arquivos=["fre_cia_aberta_ANO.csv", "fre_cia_aberta_ANO.zip"],
            tabela="formulario_referencia",
        ),
        relacao_cvm_model(
            descricao="Grupos de Demonstrações Financeiras",
            link=[links_cvm[1], links_cvm[2]],
            arquivos=[
                "dfp_cia_aberta_DVA_ind_ANO.csv",
                "dfp_cia_aberta_DVA_con_ANO.csv",
                "dfp_cia_aberta_DRE_ind_ANO.csv",
                "dfp_cia_aberta_DRE_con_ANO.csv",
                "dfp_cia_aberta_DRA_ind_ANO.csv",
                "dfp_cia_aberta_DRA_con_ANO.csv",
                "dfp_cia_aberta_DMPL_ind_ANO.csv",
                "dfp_cia_aberta_DMPL_con_ANO.csv",
                "dfp_cia_aberta_DFC_MI_ind_ANO.csv",
                "dfp_cia_aberta_DFC_MI_con_ANO.csv",
                "dfp_cia_aberta_DFC_MD_ind_ANO.csv",
                "dfp_cia_aberta_DFC_MD_con_ANO.csv",
                "dfp_cia_aberta_BPP_ind_ANO.csv",
                "dfp_cia_aberta_BPP_con_ANO.csv",
                "dfp_cia_aberta_BPA_ind_ANO.csv",
                "dfp_cia_aberta_BPA_con_ANO.csv",
                "dfp_cia_aberta_ANO.zip",
                "itr_cia_aberta_DVA_ind_ANO.csv",
                "itr_cia_aberta_DVA_con_ANO.csv",
                "itr_cia_aberta_DRE_ind_ANO.csv",
                "itr_cia_aberta_DRE_con_ANO.csv",
                "itr_cia_aberta_DRA_ind_ANO.csv",
                "itr_cia_aberta_DRA_con_ANO.csv",
                "itr_cia_aberta_DMPL_ind_ANO.csv",
                "itr_cia_aberta_DMPL_con_ANO.csv",
                "itr_cia_aberta_DFC_MI_ind_ANO.csv",
                "itr_cia_aberta_DFC_MI_con_ANO.csv",
                "itr_cia_aberta_DFC_MD_ind_ANO.csv",
                "itr_cia_aberta_DFC_MD_con_ANO.csv",
                "itr_cia_aberta_BPP_ind_ANO.csv",
                "itr_cia_aberta_BPP_con_ANO.csv",
                "itr_cia_aberta_BPA_ind_ANO.csv",
                "itr_cia_aberta_BPA_con_ANO.csv",
                "itr_cia_aberta_ANO.zip",
            ],
            tabela="grupo_demonstrativo_financeiro",
        ),
        relacao_cvm_model(
            descricao="Planos de Contas",
            link=[links_cvm[1], links_cvm[2]],
            arquivos=[
                "dfp_cia_aberta_DVA_ind_ANO.csv",
                "dfp_cia_aberta_DVA_con_ANO.csv",
                "dfp_cia_aberta_DRE_ind_ANO.csv",
                "dfp_cia_aberta_DRE_con_ANO.csv",
                "dfp_cia_aberta_DRA_ind_ANO.csv",
                "dfp_cia_aberta_DRA_con_ANO.csv",
                "dfp_cia_aberta_DMPL_ind_ANO.csv",
                "dfp_cia_aberta_DMPL_con_ANO.csv",
                "dfp_cia_aberta_DFC_MI_ind_ANO.csv",
                "dfp_cia_aberta_DFC_MI_con_ANO.csv",
                "dfp_cia_aberta_DFC_MD_ind_ANO.csv",
                "dfp_cia_aberta_DFC_MD_con_ANO.csv",
                "dfp_cia_aberta_BPP_ind_ANO.csv",
                "dfp_cia_aberta_BPP_con_ANO.csv",
                "dfp_cia_aberta_BPA_ind_ANO.csv",
                "dfp_cia_aberta_BPA_con_ANO.csv",
                "dfp_cia_aberta_ANO.zip",
                "itr_cia_aberta_DVA_ind_ANO.csv",
                "itr_cia_aberta_DVA_con_ANO.csv",
                "itr_cia_aberta_DRE_ind_ANO.csv",
                "itr_cia_aberta_DRE_con_ANO.csv",
                "itr_cia_aberta_DRA_ind_ANO.csv",
                "itr_cia_aberta_DRA_con_ANO.csv",
                "itr_cia_aberta_DMPL_ind_ANO.csv",
                "itr_cia_aberta_DMPL_con_ANO.csv",
                "itr_cia_aberta_DFC_MI_ind_ANO.csv",
                "itr_cia_aberta_DFC_MI_con_ANO.csv",
                "itr_cia_aberta_DFC_MD_ind_ANO.csv",
                "itr_cia_aberta_DFC_MD_con_ANO.csv",
                "itr_cia_aberta_BPP_ind_ANO.csv",
                "itr_cia_aberta_BPP_con_ANO.csv",
                "itr_cia_aberta_BPA_ind_ANO.csv",
                "itr_cia_aberta_BPA_con_ANO.csv",
                "itr_cia_aberta_ANO.zip",
            ],
            tabela="planos_contas",
        ),
    ]

    def mostrarDados(self):
        for relacao in self.lista_relacao:
            print("\n", relacao)
