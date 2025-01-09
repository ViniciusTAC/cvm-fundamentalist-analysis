from datetime import date
from numpy import double


class Informacao_trimestral:
    _codigo_conta: str
    _cnpj_companhia: str
    _codigo_cvm: str
    _escala_monetaria: str
    _grupo_dfp: int
    _moeda: int
    _ordem_exercicio: str
    _conta_fixa: str
    _versao: int
    _data_inicio_exercicio: date
    _data_fim_exercicio: date
    _data_referencia_doc: date
    _valor_conta: double
    _data_doc: date
    _mes_doc: str
    _ano_doc: str

    def __init__(
        self,
        _codigo_conta,
        _cnpj_companhia,
        _codigo_cvm,
        _escala_monetaria,
        _grupo_dfp,
        _moeda,
        _ordem_exercicio,
        _conta_fixa,
        _versao,
        _data_inicio_exercicio,
        _data_fim_exercicio,
        _data_referencia_doc,
        _valor_conta,
        _data_doc,
        _mes_doc,
        _ano_doc,
    ):
        self._codigo_conta = _codigo_conta
        self._cnpj_companhia = _cnpj_companhia
        self._codigo_cvm = _codigo_cvm
        self._escala_monetaria = _escala_monetaria
        self._grupo_dfp = _grupo_dfp
        self._moeda = _moeda
        self._ordem_exercicio = _ordem_exercicio
        self._conta_fixa = _conta_fixa
        self._versao = _versao
        self._data_inicio_exercicio = _data_inicio_exercicio
        self._data_fim_exercicio = _data_fim_exercicio
        self._data_referencia_doc = _data_referencia_doc
        self._valor_conta = _valor_conta
        self._data_doc = _data_doc
        self._mes_doc = _mes_doc
        self._ano_doc = _ano_doc

    @property
    def codigo_conta(self):
        return self._codigo_conta

    @codigo_conta.setter
    def codigo_conta(self, value):
        self._codigo_conta = value

    @property
    def cnpj_companhia(self):
        return self._cnpj_companhia

    @cnpj_companhia.setter
    def cnpj_companhia(self, value):
        self._cnpj_companhia = value

    @property
    def codigo_cvm(self):
        return self._codigo_cvm

    @codigo_cvm.setter
    def codigo_cvm(self, value):
        self._codigo_cvm = value

    @property
    def escala_monetaria(self):
        return self._escala_monetaria

    @escala_monetaria.setter
    def escala_monetaria(self, value):
        self._escala_monetaria = value

    @property
    def grupo_dfp(self):
        return self._grupo_dfp

    @grupo_dfp.setter
    def grupo_dfp(self, value):
        self._grupo_dfp = value

    @property
    def moeda(self):
        return self._moeda

    @moeda.setter
    def moeda(self, value):
        self._moeda = value

    @property
    def ordem_exercicio(self):
        return self._ordem_exercicio

    @ordem_exercicio.setter
    def ordem_exercicio(self, value):
        self._ordem_exercicio = value

    @property
    def conta_fixa(self):
        return self._conta_fixa

    @conta_fixa.setter
    def conta_fixa(self, value):
        self._conta_fixa = value

    @property
    def versao(self):
        return self._versao

    @versao.setter
    def versao(self, value):
        self._versao = value

    @property
    def data_inicio_exercicio(self):
        return self._data_inicio_exercicio

    @data_inicio_exercicio.setter
    def data_inicio_exercicio(self, value):
        self._data_inicio_exercicio = value

    @property
    def data_fim_exercicio(self):
        return self._data_fim_exercicio

    @data_fim_exercicio.setter
    def data_fim_exercicio(self, value):
        self._data_fim_exercicio = value

    @property
    def data_referencia_doc(self):
        return self._data_referencia_doc

    @data_referencia_doc.setter
    def data_referencia_doc(self, value):
        self._data_referencia_doc = value

    @property
    def valor_conta(self):
        return self._valor_conta

    @valor_conta.setter
    def valor_conta(self, value):
        self._valor_conta = value

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
        print("self._codigo_conta: ", str(self._codigo_conta))
        print("self._cnpj_companhia: ", str(self._cnpj_companhia))
        print("self._codigo_cvm: ", str(self._codigo_cvm))
        print("self._escala_monetaria: ", str(self._escala_monetaria))
        print("self._grupo_dfp: ", str(self._grupo_dfp))
        print("self._moeda: ", str(self._moeda))
        print("self._ordem_exercicio: ", str(self._ordem_exercicio))
        print("self._conta_fixa: ", str(self._conta_fixa))
        print("self._versao: ", str(self._versao))
        print("self._data_inicio_exercicio: ", str(self._data_inicio_exercicio))
        print("self._data_fim_exercicio: ", str(self._data_fim_exercicio))
        print("self._data_referencia_doc: ", str(self._data_referencia_doc))
        print("self._valor_conta: ", str(self._valor_conta))
        print("self._data_doc: ", str(self._data_doc))
        print("self._mes_doc: ", str(self._mes_doc))
        print("self._ano_doc: ", str(self._ano_doc))
