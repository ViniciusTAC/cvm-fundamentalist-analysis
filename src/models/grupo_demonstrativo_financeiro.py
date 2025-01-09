class Grupo_demonstrativo_financeiro:
    _codigo_grupo_dfp: int
    _grupo_dpf: str

    def __init__(self, _codigo_grupo_dfp, _grupo_dpf):
        self._codigo_grupo_dfp = _codigo_grupo_dfp
        self._grupo_dpf = _grupo_dpf

    @property
    def codigo_grupo_dfp(self):
        return self._codigo_grupo_dfp

    @codigo_grupo_dfp.setter
    def codigo_grupo_dfp(self, value):
        self._codigo_grupo_dfp = value

    @property
    def grupo_dpf(self):
        return self._grupo_dpf

    @grupo_dpf.setter
    def grupo_dpf(self, value):
        self._grupo_dpf = value

    def mostrarDados(self):
        print("self.codigo_grupo_dfp: ", str(self.codigo_grupo_dfp))
        print("self.grupo_dpf: ", str(self.grupo_dpf))
