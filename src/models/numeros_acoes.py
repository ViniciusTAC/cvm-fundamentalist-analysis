from datetime import date


class Numeros_Acoes:
    _fonte_dados: str
    _cnpj_companhia: str
    _qtd_acoes_ordinarias_capital_integralizado: int
    _qtd_acoes_preferenciais_capital_integralizado: int
    _qtd_total_acoes_capital_integralizado: int
    _qtd_acoes_ordinarias_tesouro: int
    _qtd_acoes_preferenciais_tesouro: int
    _qtd_total_acoes_tesouro: int
    _versao: int
    _data_referencia: date
    _mes: int
    _ano: int

    def __init__(
        self,
        _fonte_dados,
        _cnpj_companhia,
        _qtd_acoes_ordinarias_capital_integralizado,
        _qtd_acoes_preferenciais_capital_integralizado,
        _qtd_total_acoes_capital_integralizado,
        _qtd_acoes_ordinarias_tesouro,
        _qtd_acoes_preferenciais_tesouro,
        _qtd_total_acoes_tesouro,
        _versao,
        _data_referencia,
        _mes,
        _ano,
    ):
        self._fonte_dados = _fonte_dados
        self._cnpj_companhia = _cnpj_companhia
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
        self._data_referencia = _data_referencia
        self._mes = _mes
        self._ano = _ano

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
    def data_referencia(self):
        return self._data_referencia

    @data_referencia.setter
    def data_referencia(self, value):
        self._data_referencia = value

    @property
    def mes(self):
        return self._mes

    @mes.setter
    def mes(self, value):
        self._mes = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value

    def mostrarDados(self):
        print("cnpj_companhia: ", str(self.cnpj_companhia))
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
        print("data_referencia: ", str(self.data_referencia))
        print("mes: ", str(self.mes))
        print("ano: ", str(self.ano))
