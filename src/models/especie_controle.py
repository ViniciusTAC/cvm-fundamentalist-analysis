class Especie_controle:
    _id_especie: int
    _descricao: str

    def __init__(self, _id_especie, _descricao):
        self._id_especie = _id_especie
        self._descricao = _descricao

    @property
    def id_especie(self):
        return self._id_especie

    @id_especie.setter
    def id_especie(self, value):
        self._id_especie = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrarDados(self):
        return f"id_especie: {self.id_especie},descricao: {self.descricao}"
