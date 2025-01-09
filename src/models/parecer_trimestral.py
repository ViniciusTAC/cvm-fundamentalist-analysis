from datetime import date


class Parecer_trimestral:
    cnpj_companhia: str
    _num_linha_parecer_declaracao: int
    _tipo_parecer_declaracao: str
    _tipo_relatorio_especial: str
    _texto_parecer_declaracao: str
    _versao: int
    _data_referencia_doc: date
    _data_doc: date
    _mes_doc: str
    _ano_doc: str

    def __init__(
        self,
        _cnpj_companhia,
        _num_linha_parecer_declaracao,
        _tipo_parecer_declaracao,
        _tipo_relatorio_especial,
        _texto_parecer_declaracao,
        _versao,
        _data_referencia_doc,
        _data_doc,
        _mes_doc,
        _ano_doc,
    ):
        self._cnpj_companhia = _cnpj_companhia
        self._num_linha_parecer_declaracao = _num_linha_parecer_declaracao
        self._tipo_parecer_declaracao = _tipo_parecer_declaracao
        self._tipo_relatorio_especial = _tipo_relatorio_especial
        self._texto_parecer_declaracao = _texto_parecer_declaracao
        self._versao = _versao
        self._data_referencia_doc = _data_referencia_doc
        self._data_doc = _data_doc
        self._mes_doc = _mes_doc
        self._ano_doc = _ano_doc

    @property
    def cnpj_companhia(self):
        return self._cnpj_companhia

    @cnpj_companhia.setter
    def cnpj_companhia(self, value):
        self._cnpj_companhia = value

    @property
    def num_linha_parecer_declaracao(self):
        return self._num_linha_parecer_declaracao

    @num_linha_parecer_declaracao.setter
    def num_linha_parecer_declaracao(self, value):
        self._num_linha_parecer_declaracao = value

    @property
    def tipo_parecer_declaracao(self):
        return self._tipo_parecer_declaracao

    @tipo_parecer_declaracao.setter
    def tipo_parecer_declaracao(self, value):
        self._tipo_parecer_declaracao = value

    @property
    def tipo_relatorio_auditor(self):
        return self._tipo_relatorio_especial

    @tipo_relatorio_auditor.setter
    def tipo_relatorio_auditor(self, value):
        self._tipo_relatorio_especial = value

    @property
    def texto_parecer_declaracao(self):
        return self._texto_parecer_declaracao

    @texto_parecer_declaracao.setter
    def texto_parecer_declaracao(self, value):
        self._texto_parecer_declaracao = value

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
        print("self._cnpj_companhia: ", str(self._cnpj_companhia))
        print(
            "self._num_linha_parecer_declaracao: ",
            str(self._num_linha_parecer_declaracao),
        )
        print("self._tipo_parecer_declaracao: ", str(self._tipo_parecer_declaracao))
        print("self._tipo_relatorio_especial: ", str(self._tipo_relatorio_especial))
        print("self._texto_parecer_declaracao: ", str(self._texto_parecer_declaracao))
        print("self._versao: ", str(self._versao))
        print("self._data_referencia_doc: ", str(self._data_referencia_doc))
        print("self._data_doc: ", str(self._data_doc))
        print("self._mes_doc: ", str(self._mes_doc))
        print("self._ano_doc: ", str(self._ano_doc))