from datetime import date


class Empresas:
    _categoria_doc: str
    _codigo_cvm: str
    _cnpj_companhia: str
    _descricao_atividade: str
    _especie_controle_acionario: str
    _identificador_documento: int
    _mes_encerramento_exercicio_social: int
    _nome_empresa: str
    _nome_anterior_empresa: str
    _pagina_web: str
    _pais_custodia_valores_mobiliarios: str
    _pais_origem: str
    _setor_atividade: str
    _situacao_emissor: str
    _situacao_registro_cvm: str
    _versao: int
    _data_registro_cvm: date
    _data_nome_empresarial: date
    _data_categoria_registro_cvm: date
    _data_situacao_registro_cvm: date
    _data_constituicao: date
    _data_especie_controle_acionario: date
    _data_referencia_documento: date
    _data_situacao_emissor: date
    _data_alteracao_exercicio_social: date
    _dia_encerramento_exercicio_social: int
    _data_doc: date
    _mes_doc: str
    _ano_doc: str

    def __init__(
        self,
        _categoria_doc,
        _codigo_cvm,
        _cnpj_companhia,
        _descricao_atividade,
        _especie_controle_acionario,
        _identificador_documento,
        _mes_encerramento_exercicio_social,
        _nome_empresa,
        _nome_anterior_empresa,
        _pagina_web,
        _pais_custodia_valores_mobiliarios,
        _pais_origem,
        _setor_atividade,
        _situacao_emissor,
        _situacao_registro_cvm,
        _versao,
        _data_registro_cvm,
        _data_nome_empresarial,
        _data_categoria_registro_cvm,
        _data_situacao_registro_cvm,
        _data_constituicao,
        _data_especie_controle_acionario,
        _data_referencia_documento,
        _data_situacao_emissor,
        _data_alteracao_exercicio_social,
        _dia_encerramento_exercicio_social,
        _data_doc,
        _mes_doc,
        _ano_doc,
    ):
        self._categoria_doc = _categoria_doc
        self._codigo_cvm = _codigo_cvm
        self._cnpj_companhia = _cnpj_companhia
        self._descricao_atividade = _descricao_atividade
        self._especie_controle_acionario = _especie_controle_acionario
        self._identificador_documento = _identificador_documento
        self._mes_encerramento_exercicio_social = _mes_encerramento_exercicio_social
        self._nome_empresa = _nome_empresa
        self._nome_anterior_empresa = _nome_anterior_empresa
        self._pagina_web = _pagina_web
        self._pais_custodia_valores_mobiliarios = _pais_custodia_valores_mobiliarios
        self._pais_origem = _pais_origem
        self._setor_atividade = _setor_atividade
        self._situacao_emissor = _situacao_emissor
        self._situacao_registro_cvm = _situacao_registro_cvm
        self._versao = _versao
        self._data_registro_cvm = _data_registro_cvm
        self._data_nome_empresarial = _data_nome_empresarial
        self._data_categoria_registro_cvm = _data_categoria_registro_cvm
        self._data_situacao_registro_cvm = _data_situacao_registro_cvm
        self._data_constituicao = _data_constituicao
        self._data_especie_controle_acionario = _data_especie_controle_acionario
        self._data_referencia_documento = _data_referencia_documento
        self._data_situacao_emissor = _data_situacao_emissor
        self._data_alteracao_exercicio_social = _data_alteracao_exercicio_social
        self._dia_encerramento_exercicio_social = _dia_encerramento_exercicio_social
        self._data_doc = _data_doc
        self._mes_doc = _mes_doc
        self._ano_doc = _ano_doc

    @property
    def categoria_doc(self):
        return self._categoria_doc

    @categoria_doc.setter
    def categoria_doc(self, value):
        self._categoria_doc = value

    @property
    def codigo_cvm(self):
        return self._codigo_cvm

    @codigo_cvm.setter
    def codigo_cvm(self, value):
        self._codigo_cvm = value

    @property
    def cnpj_companhia(self):
        return self._cnpj_companhia

    @cnpj_companhia.setter
    def cnpj_companhia(self, value):
        self._cnpj_companhia = value

    @property
    def descricao_atividade(self):
        return self._descricao_atividade

    @descricao_atividade.setter
    def descricao_atividade(self, value):
        self._descricao_atividade = value

    @property
    def especie_controle_acionario(self):
        return self._especie_controle_acionario

    @especie_controle_acionario.setter
    def especie_controle_acionario(self, value):
        self._especie_controle_acionario = value

    @property
    def identificador_documento(self):
        return self._identificador_documento

    @identificador_documento.setter
    def identificador_documento(self, value):
        self._identificador_documento = value

    @property
    def mes_encerramento_exercicio_social(self):
        return self._mes_encerramento_exercicio_social

    @mes_encerramento_exercicio_social.setter
    def mes_encerramento_exercicio_social(self, value):
        self._mes_encerramento_exercicio_social = value

    @property
    def nome_empresa(self):
        return self._nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, value):
        self._nome_empresa = value

    @property
    def nome_anterior_empresa(self):
        return self._nome_anterior_empresa

    @nome_anterior_empresa.setter
    def nome_anterior_empresa(self, value):
        self._nome_anterior_empresa = value

    @property
    def pagina_web(self):
        return self._pagina_web

    @pagina_web.setter
    def pagina_web(self, value):
        self._pagina_web = value

    @property
    def pais_custodia_valores_mobiliarios(self):
        return self._pais_custodia_valores_mobiliarios

    @pais_custodia_valores_mobiliarios.setter
    def pais_custodia_valores_mobiliarios(self, value):
        self._pais_custodia_valores_mobiliarios = value

    @property
    def pais_origem(self):
        return self._pais_origem

    @pais_origem.setter
    def pais_origem(self, value):
        self._pais_origem = value

    @property
    def setor_atividade(self):
        return self._setor_atividade

    @setor_atividade.setter
    def setor_atividade(self, value):
        self._setor_atividade = value

    @property
    def situacao_emissor(self):
        return self._situacao_emissor

    @situacao_emissor.setter
    def situacao_emissor(self, value):
        self._situacao_emissor = value

    @property
    def situacao_registro_cvm(self):
        return self._situacao_registro_cvm

    @situacao_registro_cvm.setter
    def situacao_registro_cvm(self, value):
        self._situacao_registro_cvm = value

    @property
    def versao(self):
        return self._versao

    @versao.setter
    def versao(self, value):
        self._versao = value

    @property
    def data_registro_cvm(self):
        return self._data_registro_cvm

    @data_registro_cvm.setter
    def data_registro_cvm(self, value):
        self._data_registro_cvm = value

    @property
    def data_nome_empresarial(self):
        return self._data_nome_empresarial

    @data_nome_empresarial.setter
    def data_nome_empresarial(self, value):
        self._data_nome_empresarial = value

    @property
    def data_categoria_registro_cvm(self):
        return self._data_categoria_registro_cvm

    @data_categoria_registro_cvm.setter
    def data_categoria_registro_cvm(self, value):
        self._data_categoria_registro_cvm = value

    @property
    def data_situacao_registro_cvm(self):
        return self._data_situacao_registro_cvm

    @data_situacao_registro_cvm.setter
    def data_situacao_registro_cvm(self, value):
        self._data_situacao_registro_cvm = value

    @property
    def data_constituicao(self):
        return self._data_constituicao

    @data_constituicao.setter
    def data_constituicao(self, value):
        self._data_constituicao = value

    @property
    def data_especie_controle_acionario(self):
        return self._data_especie_controle_acionario

    @data_especie_controle_acionario.setter
    def data_especie_controle_acionario(self, value):
        self._data_especie_controle_acionario = value

    @property
    def data_referencia_documento(self):
        return self._data_referencia_documento

    @data_referencia_documento.setter
    def data_referencia_documento(self, value):
        self._data_referencia_documento = value

    @property
    def data_situacao_emissor(self):
        return self._data_situacao_emissor

    @data_situacao_emissor.setter
    def data_situacao_emissor(self, value):
        self._data_situacao_emissor = value

    @property
    def data_alteracao_exercicio_social(self):
        return self._data_alteracao_exercicio_social

    @data_alteracao_exercicio_social.setter
    def data_alteracao_exercicio_social(self, value):
        self._data_alteracao_exercicio_social = value

    @property
    def dia_encerramento_exercicio_social(self):
        return self._dia_encerramento_exercicio_social

    @dia_encerramento_exercicio_social.setter
    def dia_encerramento_exercicio_social(self, value):
        self._dia_encerramento_exercicio_social = value

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
        print("self.categoria_doc: ", str(self.categoria_doc))
        print("self.codigo_cvm: ", str(self.codigo_cvm))
        print("self.cnpj_companhia: ", str(self.cnpj_companhia))
        print("self.descricao_atividade: ", str(self.descricao_atividade))
        print("self.especie_controle_acionario: ", str(self.especie_controle_acionario))
        print("self.identificador_documento: ", str(self.identificador_documento))
        print("self.mes_encerramento_exercicio_social: ", str(self.mes_encerramento_exercicio_social))
        print("self.nome_empresa: ", str(self.nome_empresa))
        print("self.nome_anterior_empresa: ", str(self.nome_anterior_empresa))
        print("self.pagina_web: ", str(self.pagina_web))
        print("self.pais_custodia_valores_mobiliarios: ", str(self.pais_custodia_valores_mobiliarios))
        print("self.pais_origem: ", str(self.pais_origem))
        print("self.setor_atividade: ", str(self.setor_atividade))
        print("self.situacao_emissor: ", str(self.situacao_emissor))
        print("self.situacao_registro_cvm: ", str(self.situacao_registro_cvm))
        print("self.versao: ", str(self.versao))
        print("self.data_registro_cvm: ", str(self.data_registro_cvm))
        print("self.data_nome_empresarial: ", str(self.data_nome_empresarial))
        print("self.data_categoria_registro_cvm: ", str(self.data_categoria_registro_cvm))
        print("self.data_situacao_registro_cvm: ", str(self.data_situacao_registro_cvm))
        print("self.data_constituicao: ", str(self.data_constituicao))
        print("self.data_especie_controle_acionario: ", str(self.data_especie_controle_acionario))
        print("self.data_referencia_documento: ", str(self.data_referencia_documento))
        print("self.data_situacao_emissor: ", str(self.data_situacao_emissor))
        print("self.data_alteracao_exercicio_social: ", str(self.data_alteracao_exercicio_social))
        print("self.dia_encerramento_exercicio_social: ", str(self.dia_encerramento_exercicio_social))
        print("self.data_doc: ", str(self.data_doc))
        print("self.mes_doc: ", str(self.mes_doc))
        print("self.ano_doc: ", str(self.ano_doc))
