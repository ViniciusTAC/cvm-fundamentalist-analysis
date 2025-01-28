from datetime import date


class Numeros_Acoes:
    _fonte_dados: str
    _cnpj_companhia: str
    _denominacao_companhia: str
    _qtd_acoes_ordinarias_capital_integralizado: int
    _qtd_acoes_preferenciais_capital_integralizado: int
    _qtd_total_acoes_capital_integralizado: int
    _qtd_acoes_ordinarias_tesouro: int
    _qtd_acoes_preferenciais_tesouro: int
    _qtd_total_acoes_tesouro: int
    _versao: int
    _data_referencia_doc: date
    _data_doc: date
    _mes_doc: str
    _ano_doc: str

    def __init__(
        self,
        _fonte_dados,
        _cnpj_companhia,
        _denominacao_companhia,
        _qtd_acoes_ordinarias_capital_integralizado,
        _qtd_acoes_preferenciais_capital_integralizado,
        _qtd_total_acoes_capital_integralizado,
        _qtd_acoes_ordinarias_tesouro,
        _qtd_acoes_preferenciais_tesouro,
        _qtd_total_acoes_tesouro,
        _versao,
        _data_referencia_doc,
        _data_doc,
        _mes_doc,
        _ano_doc,
    ):
        self._fonte_dados = _fonte_dados
        self._cnpj_companhia = _cnpj_companhia
        self._denominacao_companhia = _denominacao_companhia
        self._qtd_acoes_ordinarias_capital_integralizado = (
            _qtd_acoes_ordinarias_capital_integralizado
        )
        self._qtd_acoes_preferenciais_capital_integralizado = (
            _qtd_acoes_preferenciais_capital_integralizado
        )
        self._qtd_total_acoes_capital_integralizado = (
            _qtd_total_acoes_capital_integralizado
        )
        self._qtd_acoes_ordinarias_tesouro = _qtd_acoes_ordinarias_tesouro
        self._qtd_acoes_preferenciais_tesouro = _qtd_acoes_preferenciais_tesouro
        self._qtd_total_acoes_tesouro = _qtd_total_acoes_tesouro
        self._versao = _versao
        self._data_referencia_doc = _data_referencia_doc
        self._data_doc = _data_doc
        self._mes_doc = _mes_doc
        self._ano_doc = _ano_doc

    @property
    def fonte_dados(self):
        return self._fonte_dados

    @fonte_dados.setter
    def fonte_dados(self, value):
        self._fonte_dados = value

    @property
    def cnpj_companhia(self):
        return self._cnpj_companhia

    @cnpj_companhia.setter
    def cnpj_companhia(self, value):
        self._cnpj_companhia = value

    @property
    def denominacao_companhia(self):
        return self._denominacao_companhia

    @denominacao_companhia.setter
    def denominacao_companhia(self, value):
        self._denominacao_companhia = value

    @property
    def qtd_acoes_ordinarias_capital_integralizado(self):
        return self._qtd_acoes_ordinarias_capital_integralizado

    @qtd_acoes_ordinarias_capital_integralizado.setter
    def qtd_acoes_ordinarias_capital_integralizado(self, value):
        self._qtd_acoes_ordinarias_capital_integralizado = value

    @property
    def qtd_acoes_preferenciais_capital_integralizado(self):
        return self._qtd_acoes_preferenciais_capital_integralizado

    @qtd_acoes_preferenciais_capital_integralizado.setter
    def qtd_acoes_preferenciais_capital_integralizado(self, value):
        self._qtd_acoes_preferenciais_capital_integralizado = value

    @property
    def qtd_total_acoes_capital_integralizado(self):
        return self._qtd_total_acoes_capital_integralizado

    @qtd_total_acoes_capital_integralizado.setter
    def qtd_total_acoes_capital_integralizado(self, value):
        self._qtd_total_acoes_capital_integralizado = value

    @property
    def qtd_acoes_ordinarias_tesouro(self):
        return self._qtd_acoes_ordinarias_tesouro

    @qtd_acoes_ordinarias_tesouro.setter
    def qtd_acoes_ordinarias_tesouro(self, value):
        self._qtd_acoes_ordinarias_tesouro = value

    @property
    def qtd_acoes_preferenciais_tesouro(self):
        return self._qtd_acoes_preferenciais_tesouro

    @qtd_acoes_preferenciais_tesouro.setter
    def qtd_acoes_preferenciais_tesouro(self, value):
        self._qtd_acoes_preferenciais_tesouro = value

    @property
    def qtd_total_acoes_tesouro(self):
        return self._qtd_total_acoes_tesouro

    @qtd_total_acoes_tesouro.setter
    def qtd_total_acoes_tesouro(self, value):
        self._qtd_total_acoes_tesouro = value

    @property
    def versao(self):
        return self._versao

    @versao.setter
    def versao(self, value):
        self._versao = value

    @property
    def data_referencia_doc(self):
        return self._data_referencia_doc

    @data_referencia_doc.setter
    def data_referencia_doc(self, value):
        self._data_referencia_doc = value

    @property
    def data_doc(self):
        return self._data_doc

    @data_doc.setter
    def data_doc(self, value):
        self._data_doc = value

    @property
    def mes_doc(self):
        return self._mes_doc

    @mes_doc.setter
    def mes_doc(self, value):
        self._mes_doc = value

    @property
    def ano_doc(self):
        return self._ano_doc

    @ano_doc.setter
    def ano_doc(self, value):
        self._ano_doc = value

    def mostrarDados(self):
        print("cnpj_companhia: ", str(self.cnpj_companhia))
        print("denominacao_companhia: ", str(self.denominacao_companhia))
        print(
            "qtd_acoes_ordinarias_capital_integralizado: ",
            str(self.qtd_acoes_ordinarias_capital_integralizado),
        )
        print(
            "qtd_acoes_preferenciais_capital_integralizado: ",
            str(self.qtd_acoes_preferenciais_capital_integralizado),
        )
        print(
            "qtd_total_acoes_capital_integralizado: ",
            str(self.qtd_total_acoes_capital_integralizado),
        )
        print("qtd_acoes_ordinarias_tesouro: ", str(self.qtd_acoes_ordinarias_tesouro))
        print(
            "qtd_acoes_preferenciais_tesouro: ",
            str(self.qtd_acoes_preferenciais_tesouro),
        )
        print("qtd_total_acoes_tesouro: ", str(self.qtd_total_acoes_tesouro))
        print("versao: ", str(self.versao))
        print("data_referencia_doc: ", str(self.data_referencia_doc))
        print("data_doc: ", str(self.data_doc))
        print("mes_doc: ", str(self.mes_doc))
        print("ano_doc: ", str(self.ano_doc))
