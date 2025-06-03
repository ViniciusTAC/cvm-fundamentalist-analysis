class Assunto_prensa:
    _id_assunto: int
    _descricao: str

    def __init__(self, _id_assunto, _descricao):
        self._id_assunto = _id_assunto
        self._descricao = _descricao

    @property
    def id_assunto(self):
        return self._id_assunto

    @id_assunto.setter
    def id_assunto(self, value):
        self._id_assunto = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def mostrar_dados(self):
        print("id_assunto:", self._id_assunto)
        print("descricao:", self._descricao)