class CategoriaTipoTransacaoParent:
    def __init__(self, nId,sDescricao,dDtCadastro,bPublicado,bAtivo):
        self.nId = nId
        self.sDescricao = sDescricao
        self.dDtCadastro = dDtCadastro
        self.bPublicado = bPublicado
        self.bAtivo = bAtivo
        
    def getId(self):
        return self.nId

    def setId(self, nId):
        self.Id = nId

    def getDescricao(self):
        return self.sDescricao

    def setDescricao(self, sDescricao):
        self.Descricao = sDescricao

    def getDtCadastro(self):
        return self.dDtCadastro

    def setDtCadastro(self, dDtCadastro):
        self.DtCadastro = dDtCadastro

    def getPublicado(self):
        return self.bPublicado

    def setPublicado(self, bPublicado):
        self.Publicado = bPublicado

    def getAtivo(self):
        return self.bAtivo

    def setAtivo(self, bAtivo):
        self.Ativo = bAtivo

    
