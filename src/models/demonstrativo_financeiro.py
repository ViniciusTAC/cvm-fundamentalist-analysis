from datetime import date
from numpy import double


class Demonstrativo_financeiro:
    _id_demonstrativo: int
    _cnpj_companhia: str
    _id_plano_conta: int
    _id_escala: int
    _codigo_grupo_dfp: str
    _id_moeda: int
    _id_ordem: int
    _conta_fixa: str
    _versao: int
    _data_inicio_exercicio: date
    _data_fim_exercicio: date
    _data_referencia_doc: date
    _valor_conta: double
    _mes: int
    _ano: int

    def __init__(
        self,
        _cnpj_companhia,
        _id_plano_conta,
        _id_escala,
        _codigo_grupo_dfp,
        _id_moeda,
        _id_ordem,
        _conta_fixa,
        _versao,
        _data_inicio_exercicio,
        _data_fim_exercicio,
        _data_referencia_doc,
        _valor_conta,
        _mes,
        _ano,
    ):
        self._cnpj_companhia = _cnpj_companhia
        self._id_plano_conta = _id_plano_conta
        self._id_escala = _id_escala
        self._codigo_grupo_dfp = _codigo_grupo_dfp
        self._id_moeda = _id_moeda
        self._id_ordem = _id_ordem
        self._conta_fixa = _conta_fixa
        self._versao = _versao
        self._data_inicio_exercicio = _data_inicio_exercicio
        self._data_fim_exercicio = _data_fim_exercicio
        self._data_referencia_doc = _data_referencia_doc
        self._valor_conta = _valor_conta
        self._mes = _mes
        self._ano = _ano

    # Getters e setters
    @property
    def cnpj_companhia(self):
        return self._cnpj_companhia

    @cnpj_companhia.setter
    def cnpj_companhia(self, value):
        self._cnpj_companhia = value

    @property
    def id_plano_conta(self):
        return self._id_plano_conta

    @id_plano_conta.setter
    def id_plano_conta(self, value):
        self._id_plano_conta = value

    @property
    def id_escala(self):
        return self._id_escala

    @id_escala.setter
    def id_escala(self, value):
        self._id_escala = value

    @property
    def codigo_grupo_dfp(self):
        return self._codigo_grupo_dfp

    @codigo_grupo_dfp.setter
    def codigo_grupo_dfp(self, value):
        self._codigo_grupo_dfp = value

    @property
    def id_moeda(self):
        return self._id_moeda

    @id_moeda.setter
    def id_moeda(self, value):
        self._id_moeda = value

    @property
    def id_ordem(self):
        return self._id_ordem

    @id_ordem.setter
    def id_ordem(self, value):
        self._id_ordem = value

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

    def mostrar_dados(self):
        print("cnpj_companhia: ", self._cnpj_companhia)
        print("id_plano_conta: ", self._id_plano_conta)
        print("id_escala: ", self._id_escala)
        print("codigo_grupo_dfp: ", self._codigo_grupo_dfp)
        print("id_moeda: ", self._id_moeda)
        print("id_ordem: ", self._id_ordem)
        print("conta_fixa: ", self._conta_fixa)
        print("versao: ", self._versao)
        print("data_inicio_exercicio: ", self._data_inicio_exercicio)
        print("data_fim_exercicio: ", self._data_fim_exercicio)
        print("data_referencia_doc: ", self._data_referencia_doc)
        print("valor_conta: ", self._valor_conta)
        print("mes: ", self._mes)
        print("ano: ", self._ano)
