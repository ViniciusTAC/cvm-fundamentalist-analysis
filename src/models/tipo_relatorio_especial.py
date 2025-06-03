class Tipo_relatorio_especial:
    _id_tipo_rel_especial: int
    _descricao: str

    def __init__(self, _id_tipo_rel_especial, _descricao):
        self._id_tipo_rel_especial = _id_tipo_rel_especial
        self._descricao = _descricao

    @property
    def id_tipo_rel_especial(self):
        return self._id_tipo_rel_especial

    @id_tipo_rel_especial.setter
    def id_tipo_rel_especial(self, value):
        self._id_tipo_rel_especial = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_tipo_rel_especial:", self._id_tipo_rel_especial)
        print("descricao:", self._descricao)