class Tipo_relatorio_auditor:
    _id_tipo_rel_auditor: int
    _descricao: str

    def __init__(self, _id_tipo_rel_auditor, _descricao):
        self._id_tipo_rel_auditor = _id_tipo_rel_auditor
        self._descricao = _descricao

    @property
    def id_tipo_rel_auditor(self):
        return self._id_tipo_rel_auditor

    @id_tipo_rel_auditor.setter
    def id_tipo_rel_auditor(self, value):
        self._id_tipo_rel_auditor = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_tipo_rel_auditor:", self._id_tipo_rel_auditor)
        print("descricao:", self._descricao)