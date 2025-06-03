class Tipo_parecer:
    _id_tipo_parecer: int
    _descricao: str

    def __init__(self, _id_tipo_parecer, _descricao):
        self._id_tipo_parecer = _id_tipo_parecer
        self._descricao = _descricao

    @property
    def id_tipo_parecer(self):
        return self._id_tipo_parecer

    @id_tipo_parecer.setter
    def id_tipo_parecer(self, value):
        self._id_tipo_parecer = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_tipo_parecer:", self._id_tipo_parecer)
        print("descricao:", self._descricao)