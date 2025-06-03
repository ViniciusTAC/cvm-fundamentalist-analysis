class Tipo_apresentacao_evento:
    _id_tipo_apres: int
    _descricao: str

    def __init__(self, _id_tipo_apres, _descricao):
        self._id_tipo_apres = _id_tipo_apres
        self._descricao = _descricao

    @property
    def id_tipo_apres(self):
        return self._id_tipo_apres

    @id_tipo_apres.setter
    def id_tipo_apres(self, value):
        self._id_tipo_apres = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_tipo_apres:", self._id_tipo_apres)
        print("descricao:", self._descricao)