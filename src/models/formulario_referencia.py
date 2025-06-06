from datetime import date


class Formulario_referencia:
    # _cnpj_companhia: str
    _codigo_cvm: int
    _id_categoria_doc: int
    # _denominacao_companhia: str
    _id_doc: int
    _link_doc: str
    _versao: int
    _data_recebimento: date
    _data_referencia: date
    _data_doc: date
    _mes: str
    _ano: str

    def __init__(
        self,
        _codigo_cvm,
        _id_categoria_doc,
        _id_doc,
        _link_doc,
        _versao,
        _data_recebimento,
        _data_referencia,
        _data_doc,
        _mes,
        _ano,
    ):
        self._codigo_cvm = _codigo_cvm
        self._id_categoria_doc = _id_categoria_doc
        self._id_doc = _id_doc
        self._link_doc = _link_doc
        self._versao = _versao
        self._data_recebimento = _data_recebimento
        self._data_referencia = _data_referencia
        self._data_doc = _data_doc
        self._mes = _mes
        self._ano = _ano


    @property
    def codigo_cvm(self):
        return self._codigo_cvm

    @codigo_cvm.setter
    def codigo_cvm(self, value):
        self._codigo_cvm = value

    @property
    def id_categoria_doc(self):
        return self._id_categoria_doc

    @id_categoria_doc.setter
    def id_categoria_doc(self, value):
        self._id_categoria_doc = value

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
    def data_recebimento(self):
        return self._data_recebimento

    @data_recebimento.setter
    def data_recebimento(self, value):
        self._data_recebimento = value

    @property
    def data_referencia(self):
        return self._data_referencia

    @data_referencia.setter
    def data_referencia(self, value):
        self._data_referencia = value


    @property
    def data_doc(self):
        return self._data_doc

    @data_doc.setter
    def data_doc(self, value):
        self._data_doc = value

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
        # print("cnpj_companhia: ", str(self._cnpj_companhia))
        print("id_categoria_doc: ", str(self._id_categoria_doc))
        # print("denominacao_companhia: ", str(self._denominacao_companhia))
        print("id_doc: ", str(self._id_doc))
        print("link_doc: ", str(self._link_doc))
        print("versao: ", str(self._versao))
        print("data_recebimento: ", str(self._data_recebimento))
        print("_data_referencia: ", str(self._data_referencia))
        print("data_doc: ", str(self._data_doc))
        print("mes: ", str(self._mes))
        print("ano: ", str(self._ano))
