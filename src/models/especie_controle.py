class Especie_controle:
    _descricao: str

    def __init__(self, _descricao: str):
        self._descricao = _descricao

    @property
    def descricao(self):
        return self._descricao

    def mostrar_dados(self):
        return f"descricao: {self.descricao}"
