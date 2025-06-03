class Moeda:
    _id_moeda: int
    _sigla: str
    _descricao: str

    def __init__(self, _id_moeda, _sigla, _descricao):
        self._id_moeda = _id_moeda
        self._sigla = _sigla
        self._descricao = _descricao

    @property
    def id_moeda(self):
        return self._id_moeda

    @id_moeda.setter
    def id_moeda(self, value):
        self._id_moeda = value

    @property
    def sigla(self):
        return self._sigla

    @sigla.setter
    def sigla(self, value):
        self._sigla = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_moeda:", self._id_moeda)
        print("sigla:", self._sigla)
        print("descricao:", self._descricao)