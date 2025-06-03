class Ordem_exercicio:
    _id_ordem: int
    _descricao: str

    def __init__(self, _id_ordem, _descricao):
        self._id_ordem = _id_ordem
        self._descricao = _descricao

    @property
    def id_ordem(self):
        return self._id_ordem

    @id_ordem.setter
    def id_ordem(self, value):
        self._id_ordem = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_ordem:", self._id_ordem)
        print("descricao:", self._descricao)