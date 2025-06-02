class Ordem_exercicio:
    id_ordem: int
    _descricao: str

    def __init__(self, id_ordem, _descricao):
        self.id_ordem = id_ordem
        self._descricao = _descricao

    @property
    def id_especie(self):
        return self.id_ordem

    @id_especie.setter
    def id_especie(self, value):
        self.id_ordem = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrarDados(self):
        return f"id_especie: {self.id_especie},descricao: {self.descricao}"
