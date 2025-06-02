class Moeda:
    id_moeda: int
    _descricao: str

    def __init__(self, id_moeda, _descricao):
        self.id_moeda = id_moeda
        self._descricao = _descricao

    @property
    def id_especie(self):
        return self.id_moeda

    @id_especie.setter
    def id_especie(self, value):
        self.id_moeda = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrarDados(self):
        return f"id_especie: {self.id_especie},descricao: {self.descricao}"
