class Escala_monetaria:
    id_escala: int
    _descricao: str

    def __init__(self, id_escala, _descricao):
        self.id_escala = id_escala
        self._descricao = _descricao

    @property
    def id_especie(self):
        return self.id_escala

    @id_especie.setter
    def id_especie(self, value):
        self.id_escala = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrarDados(self):
        return f"id_especie: {self.id_especie},descricao: {self.descricao}"
