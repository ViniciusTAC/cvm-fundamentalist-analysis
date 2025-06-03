class Tipo_evento:
    _id_tipo_evento: int
    _descricao: str

    def __init__(self, _id_tipo_evento, _descricao):
        self._id_tipo_evento = _id_tipo_evento
        self._descricao = _descricao

    @property
    def id_tipo_evento(self):
        return self._id_tipo_evento

    @id_tipo_evento.setter
    def id_tipo_evento(self, value):
        self._id_tipo_evento = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_tipo_evento:", self._id_tipo_evento)
        print("descricao:", self._descricao)