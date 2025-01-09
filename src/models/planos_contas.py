class Planos_contas:
    _codigo_conta: str
    _descricao_conta: str

    def __init__(self, _codigo_conta, _descricao_conta):
        self._codigo_conta = _codigo_conta
        self._descricao_conta = _descricao_conta

    @property
    def codigo_conta(self):
        return self._codigo_conta

    @codigo_conta.setter
    def codigo_conta(self, value):
        self._codigo_conta = value

    @property
    def descricao_conta(self):
        return self._descricao_conta

    @descricao_conta.setter
    def descricao_conta(self, value):
        self._descricao_conta = value

    def mostrarDados(self):
        print("self._codigo_conta: ", str(self._codigo_conta))
        print("self._descricao_conta: ", str(self._descricao_conta))
