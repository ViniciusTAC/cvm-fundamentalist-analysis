class Especie_documento_eventual:
    _id_especie_eventual: int
    _descricao: str

    def __init__(self, _id_especie_eventual, _descricao):
        self._id_especie_eventual = _id_especie_eventual
        self._descricao = _descricao

    @property
    def id_especie_eventual(self):
        return self._id_especie_eventual

    @id_especie_eventual.setter
    def id_especie_eventual(self, value):
        self._id_especie_eventual = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_especie_eventual:", self._id_especie_eventual)
        print("descricao:", self._descricao)