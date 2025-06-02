class Setor_atividade:
    id_setor: int
    _descricao: str

    def __init__(self, id_setor, _descricao):
        self.id_setor = id_setor
        self._descricao = _descricao

    @property
    def id_especie(self):
        return self.id_setor

    @id_especie.setter
    def id_especie(self, value):
        self.id_setor = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrarDados(self):
        return f"id_especie: {self.id_especie},descricao: {self.descricao}"
