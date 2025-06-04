class Assunto_prensa:
    _descricao: str

    def __init__(self, _descricao):
        self._descricao = _descricao


    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("descricao:", self._descricao)