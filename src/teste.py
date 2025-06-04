import os

# # especies_controle
# from service.especie_controle_service import process_csv_files as process_especie_controle
# from repository.especie_controle_repository import ConexaoBanco as BancoEspecie_controle

# # especies_controle
# from service.situacao_emissor_service import process_csv_files as process_situacao_emissor
# from repository.situacao_emissor_repository import ConexaoBanco as BancoSituacao_emissor

# # setor_atividade
# from service.setor_atividade_service import process_csv_files as process_setor_atividade
# from repository.setor_atividade_repository import ConexaoBanco as BancoSetor_atividade

# # setor_atividade
# from service.categoria_documento_service import process_csv_files as process_categoria_documento
# from repository.categoria_documento_repository import ConexaoBanco as BancoCategoria_documento

# # empresas
# from service.empresas_service import process_csv_files as process_empresas
# from repository.empresas_repository import ConexaoBanco as BancoEmpresas

# # tipo_relatorio_auditor
# from service.tipo_relatorio_auditor_service import (
#     process_csv_files as process_tipo_relatorio_auditor,
# )
# from repository.tipo_relatorio_auditor_repository import (
#     ConexaoBanco as BancoTipo_relatorio_auditor,
# )

# # tipo_relatorio_especial
# from service.tipo_relatorio_especial_service import (
#     process_csv_files as process_tipo_relatorio_especial,
# )
# from repository.tipo_relatorio_especial_repository import (
#     ConexaoBanco as BancoTipo_relatorio_especial,
# )

# # assunto_prensa
# from service.assunto_prensa_service import (
#     process_csv_files as process_assunto_prensa,
# )
# from repository.assunto_prensa_repository import (
#     ConexaoBanco as BancoAssunto_prensa,
# )

# # especie_documento_eventual
# from service.especie_documento_eventual_service import (
#     process_csv_files as process_especie_documento_eventual,
# )
# from repository.especie_documento_eventual_repository import (
#     ConexaoBanco as BancoEspecie_documento_eventual,
# )

# # tipo_evento
# from service.tipo_evento_service import (
#     process_csv_files as process_tipo_evento,
# )
# from repository.tipo_evento_repository import (
#     ConexaoBanco as BancoTipo_evento,
# )

# # tipo_apresentacao_evento
# from service.tipo_apresentacao_evento_service import (
#     process_csv_files as process_tipo_apresentacao_evento,
# )
# from repository.tipo_apresentacao_evento_repository import (
#     ConexaoBanco as BancoTipo_apresentacao_evento,
# )


# tipo_parecer
from service.tipo_parecer_service import (
    process_csv_files as process_tipo_parecer,
)
from repository.tipo_parecer_repository import (
    ConexaoBanco as BancoTipo_parecer,
)

# escala_monetaria
from service.escala_monetaria_service import (
    process_csv_files as process_escala_monetaria,
)
from repository.escala_monetaria_repository import (
    ConexaoBanco as BancoEscala_monetaria,
)

# ordem_exercicio
from service.ordem_exercicio_service import (
    process_csv_files as process_ordem_exercicio,
)
from repository.ordem_exercicio_repository import (
    ConexaoBanco as BancoOrdem_exercicio,
)

# moeda
from service.moeda_service import (
    process_csv_files as process_moeda,
)
from repository.moeda_repository import (
    ConexaoBanco as BancoMoeda,
)

CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")


def main():
    # # especies_controle
    # base_path = "data_extraido/FCA/sucesso"
    # especies_controle = process_especie_controle(base_path)
    # repo = BancoEspecie_controle(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for especie in especies_controle:
    #     repo.inserir_ou_ignorar_especie_controle(especie)
    # repo.desconectar()

    # # situacao_emissor
    # base_path = "data_extraido/FCA/sucesso"
    # situacao_emissor = process_situacao_emissor(base_path)
    # repo = BancoSituacao_emissor(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for situacao in situacao_emissor:
    #     repo.inserir_ou_ignorar_situacao_emissor(situacao)
    # repo.desconectar()

    # # setor_atividade
    # base_path = "data_extraido/FCA/sucesso"
    # setor_atividade = process_setor_atividade(base_path)
    # repo = BancoSetor_atividade(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for setor in setor_atividade:
    #     repo.inserir_ou_ignorar_setor_atividade(setor)
    # repo.desconectar()

    # # categoria_documento
    # base_path = "data_extraido/FCA/sucesso"
    # dados = process_categoria_documento(base_path)
    # repo = BancoCategoria_documento(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for dado in dados:
    #     repo.inserir_ou_ignorar_categoria_documento(dado)
    # repo.desconectar()

    # # empresas
    # base_path = "data_extraido/FCA/sucesso"
    # dados = process_empresas(base_path, db_path=CAMINHO_BANCO)
    # repo = BancoEmpresas(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for dado in dados:
    #     repo.inserir_ou_atualizar_empresa(dado)
    # repo.desconectar()

    # # tipo_relatorio_auditor
    # base_path = "data_extraido/DFP/sucesso"
    # dados = process_tipo_relatorio_auditor(base_path)
    # repo = BancoTipo_relatorio_auditor(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for dado in dados:
    #     repo.inserir_ou_ignorar_tipo_relatorio_auditor(dado)
    # repo.desconectar()

    # # tipo_relatorio_especial
    # base_path = "data_extraido/ITR/sucesso"
    # dados = process_tipo_relatorio_especial(base_path)
    # repo = BancoTipo_relatorio_especial(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for dado in dados:
    #     repo.inserir_ou_ignorar_tipo_relatorio_especial(dado)
    # repo.desconectar()



# -----------------
    # # assunto_prensa
    # base_path = "data_extraido/IPE/sucesso"
    # dados = process_assunto_prensa(base_path)
    # repo = BancoAssunto_prensa(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for dado in dados:
    #     repo.inserir_ou_ignorar_assunto_prensa(dado)
    # repo.desconectar()

    # # especie_documento_eventual
    # base_path = "data_extraido/IPE/sucesso"
    # dados = process_especie_documento_eventual(base_path)
    # repo = BancoEspecie_documento_eventual(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for dado in dados:
    #     repo.inserir_ou_ignorar_especie_documento_eventual(dado)
    # repo.desconectar()

    # # tipo_evento
    # base_path = "data_extraido/IPE/sucesso"
    # dados = process_tipo_evento(base_path)
    # repo = BancoTipo_evento(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for dado in dados:
    #     repo.inserir_ou_ignorar_tipo_evento(dado)
    # repo.desconectar()

    # # tipo_apresentacao_evento
    # base_path = "data_extraido/IPE/sucesso"
    # dados = process_tipo_apresentacao_evento(base_path)
    # repo = BancoTipo_apresentacao_evento(db_path=CAMINHO_BANCO)
    # repo.conectar()
    # for dado in dados:
    #     repo.inserir_ou_ignorar_tipo_apresentacao_evento(dado)
    # repo.desconectar()

    
# -----------------

    # tipo_parecer
    base_path = "data_extraido/DFP/sucesso"
    dados = process_tipo_parecer(base_path)
    repo = BancoTipo_parecer(db_path=CAMINHO_BANCO)
    repo.conectar()
    for dado in dados:
        repo.inserir_ou_ignorar_tipo_parecer(dado)
    repo.desconectar()

    # escala_monetaria
    base_path = "data_extraido/DFP/sucesso"
    dados = process_escala_monetaria(base_path)
    repo = BancoEscala_monetaria(db_path=CAMINHO_BANCO)
    repo.conectar()
    for dado in dados:
        repo.inserir_ou_ignorar_escala_monetaria(dado)
    repo.desconectar()

    # ordem_exercicio
    base_path = "data_extraido/DFP/sucesso"
    dados = process_ordem_exercicio(base_path)
    repo = BancoOrdem_exercicio(db_path=CAMINHO_BANCO)
    repo.conectar()
    for dado in dados:
        repo.inserir_ou_ignorar_ordem_exercicio(dado)
    repo.desconectar()

    # moeda
    base_path = "data_extraido/DFP/sucesso"
    dados = process_moeda(base_path)
    repo = BancoMoeda(db_path=CAMINHO_BANCO)
    repo.conectar()
    for dado in dados:
        repo.inserir_ou_ignorar_moeda(dado)
    repo.desconectar()



if __name__ == "__main__":
    main()
