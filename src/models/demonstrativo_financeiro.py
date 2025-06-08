from datetime import date
from numpy import double


class Demonstrativo_financeiro:
    _id_demonstrativo: int
    _codigo_cvm: str
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
    _data_doc: date
    _mes: int
    _ano: int

    def __init__(
        self,
        codigo_cvm,
        id_plano_conta,
        id_escala,
        codigo_grupo_dfp,
        id_moeda,
        id_ordem,
        conta_fixa,
        versao,
        data_inicio_exercicio,
        data_fim_exercicio,
        data_referencia_doc,
        valor_conta,
        data_doc,
        mes,
        ano
    ):
        self._codigo_cvm = codigo_cvm
        self._id_plano_conta = id_plano_conta
        self._id_escala = id_escala
        self._codigo_grupo_dfp = codigo_grupo_dfp
        self._id_moeda = id_moeda
        self._id_ordem = id_ordem
        self._conta_fixa = conta_fixa
        self._versao = versao
        self._data_inicio_exercicio = data_inicio_exercicio
        self._data_fim_exercicio = data_fim_exercicio
        self._data_referencia_doc = data_referencia_doc
        self._valor_conta = valor_conta
        self._data_doc = data_doc
        self._mes = mes
        self._ano = ano

    # Getters e setters
    @property
    def codigo_cvm(self):
        return self._codigo_cvm

    @codigo_cvm.setter
    def codigo_cvm(self, value):
        self._codigo_cvm = value

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

    def mostrar_dados(self):
        print("codigo_cvm: ", self._codigo_cvm)
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
        print("data_doc: ", self._data_doc)
        print("mes: ", self._mes)
        print("ano: ", self._ano)
