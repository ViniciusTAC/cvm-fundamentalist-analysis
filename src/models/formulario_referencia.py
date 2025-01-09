from datetime import date


class Formulario_referencia:
    _cnpj_companhia: str
    _categoria_doc: str
    _denominacao_companhia: str
    _id_doc: int
    _link_doc: str
    _versao: int
    _data_recebimento_doc: date
    _data_referencia_doc: date
    _data_doc: date
    _mes_doc: str
    _ano_doc: str

    def __init__(
        self,
        _cnpj_companhia,
        _categoria_doc,
        _denominacao_companhia,
        _id_doc,
        _link_doc,
        _versao,
        _data_recebimento_doc,
        _data_referencia_doc,
        _data_doc,
        _mes_doc,
        _ano_doc,
    ):
        self._cnpj_companhia = _cnpj_companhia
        self._categoria_doc = _categoria_doc
        self._denominacao_companhia = _denominacao_companhia
        self._id_doc = _id_doc
        self._link_doc = _link_doc
        self._versao = _versao
        self._data_recebimento_doc = _data_recebimento_doc
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
    def categoria_doc(self):
        return self._categoria_doc

    @categoria_doc.setter
    def categoria_doc(self, value):
        self._categoria_doc = value

    @property
    def denominacao_companhia(self):
        return self._denominacao_companhia

    @denominacao_companhia.setter
    def denominacao_companhia(self, value):
        self._denominacao_companhia = value

    @property
    def id_doc(self):
        return self._id_doc

    @id_doc.setter
    def id_doc(self, value):
        self._id_doc = value

    @property
    def link_doc(self):
        return self._link_doc

    @link_doc.setter
    def link_doc(self, value):
        self._link_doc = value

    @property
    def versao(self):
        return self._versao

    @versao.setter
    def versao(self, value):
        self._versao = value

    @property
    def data_recebimento_doc(self):
        return self._data_recebimento_doc

    @data_recebimento_doc.setter
    def data_recebimento_doc(self, value):
        self._data_recebimento_doc = value

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
        print("self._categoria_doc: ", str(self._categoria_doc))
        print("self._denominacao_companhia: ", str(self._denominacao_companhia))
        print("self._id_doc: ", str(self._id_doc))
        print("self._link_doc: ", str(self._link_doc))
        print("self._versao: ", str(self._versao))
        print("self._data_recebimento_doc: ", str(self._data_recebimento_doc))
        print("self._data_referencia_doc: ", str(self._data_referencia_doc))
        print("self._data_doc: ", str(self._data_doc))
        print("self._mes_doc: ", str(self._mes_doc))
        print("self._ano_doc: ", str(self._ano_doc))
