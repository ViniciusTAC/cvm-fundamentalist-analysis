from datetime import date


class Periodicos_eventuais:
    _cnpj_companhia: str
    _codigo_cvm: str
    _assunto: str
    _categoria_doc: str
    _especie: str
    _link_doc: str
    _nome_companhia: str
    _protocolo_entrega: str
    _tipo: str
    _tipo_apresentacao: str
    _versao: int
    _data_entrega_doc: date
    _data_referencia_doc: date
    _data_doc: date
    _mes_doc: str
    _ano_doc: str

    def __init__(
        self,
        _cnpj_companhia,
        _codigo_cvm,
        _assunto,
        _categoria_doc,
        _especie,
        _link_doc,
        _nome_companhia,
        _protocolo_entrega,
        _tipo,
        _tipo_apresentacao,
        _versao,
        _data_entrega_doc,
        _data_referencia_doc,
        _data_doc,
        _mes_doc,
        _ano_doc,
    ):
        self._cnpj_companhia = _cnpj_companhia
        self._codigo_cvm = _codigo_cvm
        self._assunto = _assunto
        self._categoria_doc = _categoria_doc
        self._especie = _especie
        self._link_doc = _link_doc
        self._nome_companhia = _nome_companhia
        self._protocolo_entrega = _protocolo_entrega
        self._tipo = _tipo
        self._tipo_apresentacao = _tipo_apresentacao
        self._versao = _versao
        self._data_entrega_doc = _data_entrega_doc
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
    def codigo_cvm(self):
        return self._codigo_cvm

    @codigo_cvm.setter
    def codigo_cvm(self, value):
        self._codigo_cvm = value

    @property
    def assunto(self):
        return self._assunto

    @assunto.setter
    def assunto(self, value):
        self._assunto = value

    @property
    def categoria_doc(self):
        return self._categoria_doc

    @categoria_doc.setter
    def categoria_doc(self, value):
        self._categoria_doc = value

    @property
    def especie(self):
        return self._especie

    @especie.setter
    def especie(self, value):
        self._especie = value

    @property
    def link_doc(self):
        return self._link_doc

    @link_doc.setter
    def link_doc(self, value):
        self._link_doc = value

    @property
    def nome_companhia(self):
        return self._nome_companhia

    @nome_companhia.setter
    def nome_companhia(self, value):
        self._nome_companhia = value

    @property
    def protocolo_entrega(self):
        return self._protocolo_entrega

    @protocolo_entrega.setter
    def protocolo_entrega(self, value):
        self._protocolo_entrega = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def tipo_apresentacao(self):
        return self._tipo_apresentacao

    @tipo_apresentacao.setter
    def tipo_apresentacao(self, value):
        self._tipo_apresentacao = value

    @property
    def versao(self):
        return self._versao

    @versao.setter
    def versao(self, value):
        self._versao = value

    @property
    def data_entrega_doc(self):
        return self._data_entrega_doc

    @data_entrega_doc.setter
    def data_entrega_doc(self, value):
        self._data_entrega_doc = value

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
        print("self._codigo_cvm: ", str(self._codigo_cvm))
        print("self._assunto: ", str(self._assunto))
        print("self._categoria_doc: ", str(self._categoria_doc))
        print("self._especie: ", str(self._especie))
        print("self._link_doc: ", str(self._link_doc))
        print("self._nome_companhia: ", str(self._nome_companhia))
        print("self._protocolo_entrega: ", str(self._protocolo_entrega))
        print("self._tipo: ", str(self._tipo))
        print("self._tipo_apresentacao: ", str(self._tipo_apresentacao))
        print("self._versao: ", str(self._versao))
        print("self._data_entrega_doc: ", str(self._data_entrega_doc))
        print("self._data_referencia_doc: ", str(self._data_referencia_doc))
        print("self._data_doc: ", str(self._data_doc))
        print("self._mes_doc: ", str(self._mes_doc))
        print("self._ano_doc: ", str(self._ano_doc))
