class Situacao_emissor:
    id_situacao: int
    _descricao: str

    def __init__(self, id_situacao, _descricao):
        self.id_situacao = id_situacao
        self._descricao = _descricao

    @property
    def id_especie(self):
        return self.id_situacao

    @id_especie.setter
    def id_especie(self, value):
        self.id_situacao = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrarDados(self):
        return f"id_especie: {self.id_especie},descricao: {self.descricao}"
