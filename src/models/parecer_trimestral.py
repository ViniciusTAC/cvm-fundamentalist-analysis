from datetime import date


class Parecer_trimestral:
    cnpj_companhia: str
    _num_linha_parecer_declaracao: int
    _id_tipo_parecer: int
    _id_tipo_rel_especial: int
    _texto_parecer_declaracao: str
    _versao: int
    _data_referencia_doc: date
    _mes: str
    _ano: str

    def __init__(
        self,
        _cnpj_companhia,
        _num_linha_parecer_declaracao,
        _id_tipo_parecer,
        _id_tipo_rel_especial,
        _texto_parecer_declaracao,
        _versao,
        _data_referencia_doc,
        _mes,
        _ano,
    ):
        self._cnpj_companhia = _cnpj_companhia
        self._num_linha_parecer_declaracao = _num_linha_parecer_declaracao
        self._id_tipo_parecer = _id_tipo_parecer
        self._id_tipo_rel_especial = _id_tipo_rel_especial
        self._texto_parecer_declaracao = _texto_parecer_declaracao
        self._versao = _versao
        self._data_referencia_doc = _data_referencia_doc
        self._mes = _mes
        self._ano = _ano

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
    def id_tipo_parecer(self):
        return self._id_tipo_parecer

    @id_tipo_parecer.setter
    def id_tipo_parecer(self, value):
        self._id_tipo_parecer = value

    @property
    def id_tipo_rel_especial(self):
        return self._id_tipo_rel_especial

    @id_tipo_rel_especial.setter
    def id_tipo_rel_especial(self, value):
        self._id_tipo_rel_especial = value

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
        print("self._cnpj_companhia: ", str(self._cnpj_companhia))
        print(
            "self._num_linha_parecer_declaracao: ",
            str(self._num_linha_parecer_declaracao),
        )
        print("id_tipo_parecer: ", str(self._id_tipo_parecer))
        print("id_tipo_rel_especial: ", str(self._id_tipo_rel_especial))
        print("texto_parecer_declaracao: ", str(self._texto_parecer_declaracao))
        print("versao: ", str(self._versao))
        print("data_referencia_doc: ", str(self._data_referencia_doc))
        print("data_doc: ", str(self._data_doc))
        print("mes: ", str(self._mes))
        print("ano: ", str(self._ano))
