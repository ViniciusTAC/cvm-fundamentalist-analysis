class Escala_monetaria:
    _id_escala: int
    _descricao: str

    def __init__(self, _id_escala, _descricao):
        self._id_escala = _id_escala
        self._descricao = _descricao

    @property
    def id_escala(self):
        return self._id_escala

    @id_escala.setter
    def id_escala(self, value):
        self._id_escala = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_escala:", self._id_escala)
        print("descricao:", self._descricao)