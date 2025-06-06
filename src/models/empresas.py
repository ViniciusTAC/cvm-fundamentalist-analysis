from datetime import date


class Empresas:
    _id_categoria_doc: int
    _codigo_cvm: str
    _cnpj_companhia: str
    _descricao_atividade: str
    _id_especie: int
    _identificador_documento: int
    _mes_encerramento_exercicio_social: int
    _nome_empresa: str
    _nome_anterior_empresa: str
    _pagina_web: str
    _pais_custodia_valores_mobiliarios: str
    _pais_origem: str
    _id_setor: int
    _id_situacao: int
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
    _mes_doc: str
    _ano_doc: str

    def __init__(
        self,
        _id_categoria_doc,
        _codigo_cvm,
        _cnpj_companhia,
        _descricao_atividade,
        _id_especie,
        _identificador_documento,
        _mes_encerramento_exercicio_social,
        _nome_empresa,
        _nome_anterior_empresa,
        _pagina_web,
        _pais_custodia_valores_mobiliarios,
        _pais_origem,
        _id_setor,
        _id_situacao,
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
        _mes_doc,
        _ano_doc,
    ):
        self._id_categoria_doc = _id_categoria_doc
        self._codigo_cvm = _codigo_cvm
        self._cnpj_companhia = _cnpj_companhia
        self._descricao_atividade = _descricao_atividade
        self._id_especie = _id_especie
        self._identificador_documento = _identificador_documento
        self._mes_encerramento_exercicio_social = _mes_encerramento_exercicio_social
        self._nome_empresa = _nome_empresa
        self._nome_anterior_empresa = _nome_anterior_empresa
        self._pagina_web = _pagina_web
        self._pais_custodia_valores_mobiliarios = _pais_custodia_valores_mobiliarios
        self._pais_origem = _pais_origem
        self._id_setor = _id_setor
        self._id_situacao = _id_situacao
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
        self._mes_doc = _mes_doc
        self._ano_doc = _ano_doc

    @property
    def id_categoria_doc(self):
        return self._id_categoria_doc

    @id_categoria_doc.setter
    def id_categoria_doc(self, value):
        self._id_categoria_doc = value

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
    def id_especie(self):
        return self._id_especie

    @id_especie.setter
    def id_especie(self, value):
        self._id_especie = value

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
    def id_setor(self):
        return self._id_setor

    @id_setor.setter
    def id_setor(self, value):
        self._id_setor = value

    @property
    def id_situacao(self):
        return self._id_situacao

    @id_situacao.setter
    def id_situacao(self, value):
        self._id_situacao = value

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
        return (
            f"id_categoria_doc: {self.id_categoria_doc}, "
            f"codigo_cvm: {self.codigo_cvm}, "
            f"cnpj_companhia: {self.cnpj_companhia}, "
            f"descricao_atividade: {self.descricao_atividade}, "
            f"id_especie: {self.id_especie}, "
            f"identificador_documento: {self.identificador_documento}, "
            f"mes_encerramento_exercicio_social: {self.mes_encerramento_exercicio_social}, "
            f"nome_empresa: {self.nome_empresa}, "
            f"nome_anterior_empresa: {self.nome_anterior_empresa}, "
            f"pagina_web: {self.pagina_web}, "
            f"pais_custodia_valores_mobiliarios: {self.pais_custodia_valores_mobiliarios}, "
            f"pais_origem: {self.pais_origem}, "
            f"id_setor: {self.id_setor}, "
            f"id_situacao: {self.id_situacao}, "
            f"situacao_registro_cvm: {self.situacao_registro_cvm}, "
            f"versao: {self.versao}, "
            f"data_registro_cvm: {self.data_registro_cvm}, "
            f"data_nome_empresarial: {self.data_nome_empresarial}, "
            f"data_categoria_registro_cvm: {self.data_categoria_registro_cvm}, "
            f"data_situacao_registro_cvm: {self.data_situacao_registro_cvm}, "
            f"data_constituicao: {self.data_constituicao}, "
            f"data_especie_controle_acionario: {self.data_especie_controle_acionario}, "
            f"data_referencia_documento: {self.data_referencia_documento}, "
            f"data_situacao_emissor: {self.data_situacao_emissor}, "
            f"data_alteracao_exercicio_social: {self.data_alteracao_exercicio_social}, "
            f"dia_encerramento_exercicio_social: {self.dia_encerramento_exercicio_social}, "
            f"mes_doc: {self.mes_doc}, "
            f"ano_doc: {self.ano_doc}"
        )
