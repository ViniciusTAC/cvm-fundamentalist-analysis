from datetime import date


class Periodicos_eventuais:
    _cnpj_companhia: str
    _id_assunto: int
    _id_categoria_doc: int
    _id_especie_eventual: int
    _link_doc: str
    _protocolo_entrega: str
    _id_tipo_evento: int
    _id_tipo_apres: int
    _versao: int
    _data_entrega: date
    _data_referencia: date
    _data_doc: date
    _mes: int
    _ano: int

    def __init__(
        self,
        _cnpj_companhia,
        _id_assunto,
        _id_categoria_doc,
        _id_especie_eventual,
        _link_doc,
        _protocolo_entrega,
        _id_tipo_evento,
        _id_tipo_apres,
        _versao,
        _data_entrega,
        _data_referencia,
        _data_doc,
        _mes,
        _ano,
    ):
        self._cnpj_companhia = _cnpj_companhia
        self._id_assunto = _id_assunto
        self._id_categoria_doc = _id_categoria_doc
        self._id_especie_eventual = _id_especie_eventual
        self._protocolo_entrega = _protocolo_entrega
        self._link_doc = _link_doc
        self._id_tipo_evento = _id_tipo_evento
        self._id_tipo_apres = _id_tipo_apres
        self._versao = _versao
        self._data_entrega = _data_entrega
        self._data_referencia = _data_referencia
        self._data_doc = _data_doc
        self._mes = _mes
        self._ano = _ano

    @property
    def cnpj_companhia(self):
        return self._cnpj_companhia

    @cnpj_companhia.setter
    def cnpj_companhia(self, value):
        self._cnpj_companhia = value

    @property
    def id_assunto(self):
        return self._id_assunto

    @id_assunto.setter
    def id_assunto(self, value):
        self._id_assunto = value

    @property
    def id_categoria_doc(self):
        return self._id_categoria_doc

    @id_categoria_doc.setter
    def id_categoria_doc(self, value):
        self._id_categoria_doc = value

    @property
    def id_especie_eventual(self):
        return self._id_especie_eventual

    @id_especie_eventual.setter
    def id_especie_eventual(self, value):
        self._id_especie_eventual = value

    @property
    def link_doc(self):
        return self._link_doc

    @link_doc.setter
    def link_doc(self, value):
        self._link_doc = value

    @property
    def protocolo_entrega(self):
        return self._protocolo_entrega

    @protocolo_entrega.setter
    def protocolo_entrega(self, value):
        self._protocolo_entrega = value

    @property
    def id_tipo_evento(self):
        return self._id_tipo_evento

    @id_tipo_evento.setter
    def id_tipo_evento(self, value):
        self._id_tipo_evento = value

    @property
    def id_tipo_apres(self):
        return self._id_tipo_apres

    @id_tipo_apres.setter
    def id_tipo_apres(self, value):
        self._id_tipo_apres = value

    @property
    def versao(self):
        return self._versao

    @versao.setter
    def versao(self, value):
        self._versao = value

    @property
    def data_entrega(self):
        return self._data_entrega

    @data_entrega.setter
    def data_entrega(self, value):
        self._data_entrega = value

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
        print("cnpj_companhia: ", str(self._cnpj_companhia))
        print("id_assunto: ", str(self._id_assunto))
        print("id_categoria_doc: ", str(self._id_categoria_doc))
        print("id_especie_eventual: ", str(self._id_especie_eventual))
        print("protocolo_entrega: ", str(self._protocolo_entrega))
        print("link_doc: ", str(self._link_doc))
        print("id_tipo_evento: ", str(self._id_tipo_evento))
        print("id_tipo_apres: ", str(self._id_tipo_apres))
        print("versao: ", str(self._versao))
        print("data_entrega: ", str(self._data_entrega))
        print("data_referencia: ", str(self._data_referencia))
        print("data_doc: ", str(self._data_doc))
        print("mes: ", str(self._mes))
        print("ano: ", str(self._ano))
