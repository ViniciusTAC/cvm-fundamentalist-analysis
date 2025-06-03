import os
# especies_controle
from service.especie_controle_service import process_csv_files as process_especie_controle
from repository.especie_controle_repository import ConexaoBanco as BancoEspecie_controle

# especies_controle
from service.situacao_emissor_service import process_csv_files as process_situacao_emissor
from repository.situacao_emissor_repository import ConexaoBanco as BancoSituacao_emissor

# setor_atividade
from service.setor_atividade_service import process_csv_files as process_setor_atividade
from repository.setor_atividade_repository import ConexaoBanco as BancoSetor_atividade

# setor_atividade
from service.categoria_documento_service import process_csv_files as process_categoria_documento
from repository.categoria_documento_repository import ConexaoBanco as BancoCategoria_documento

# empresas
from service.empresas_service import process_csv_files as process_empresas
from repository.empresas_repository import ConexaoBanco as BancoEmpresas

CAMINHO_BANCO = os.path.join("sqlite-projeto", "cvm-dados.db")


def main():
    # especies_controle
    base_path = "data_extraido/FCA/sucesso"
    especies_controle = process_especie_controle(base_path)
    repo = BancoEspecie_controle(db_path=CAMINHO_BANCO)
    repo.conectar()
    for especie in especies_controle:
        repo.inserir_ou_ignorar_especie_controle(especie)
    repo.desconectar()

    # situacao_emissor
    base_path = "data_extraido/FCA/sucesso"
    situacao_emissor = process_situacao_emissor(base_path)
    repo = BancoSituacao_emissor(db_path=CAMINHO_BANCO)
    repo.conectar()
    for situacao in situacao_emissor:
        repo.inserir_ou_ignorar_situacao_emissor(situacao)
    repo.desconectar()

    # setor_atividade
    base_path = "data_extraido/FCA/sucesso"
    setor_atividade = process_setor_atividade(base_path)
    repo = BancoSetor_atividade(db_path=CAMINHO_BANCO)
    repo.conectar()
    for setor in setor_atividade:
        repo.inserir_ou_ignorar_setor_atividade(setor)
    repo.desconectar()

    # categoria_documento
    base_path = "data_extraido/FCA/sucesso"
    dados = process_categoria_documento(base_path)
    repo = BancoCategoria_documento(db_path=CAMINHO_BANCO)
    repo.conectar()
    for dado in dados:
        repo.inserir_ou_ignorar_categoria_documento(dado)
    repo.desconectar()

    # empresas
    base_path = "data_extraido/FCA/sucesso"
    dados = process_empresas(base_path, db_path=CAMINHO_BANCO)
    repo = BancoEmpresas(db_path=CAMINHO_BANCO)
    repo.conectar()
    for dado in dados:
        repo.inserir_ou_atualizar_empresa(dado)
    repo.desconectar()


if __name__ == "__main__":
    main()
