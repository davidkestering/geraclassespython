class TipoTransacaoParent:
    def __init__(self, nId,nIdCategoriaTipoTransacao,sTransacao,dDtCadastro,bPublicado,bAtivo):
        self.nId = nId
        self.nIdCategoriaTipoTransacao = nIdCategoriaTipoTransacao
        self.sTransacao = sTransacao
        self.dDtCadastro = dDtCadastro
        self.bPublicado = bPublicado
        self.bAtivo = bAtivo
        
    def getId(self):
        return self.nId

    def setId(self, nId):
        self.Id = nId

    def getIdCategoriaTipoTransacao(self):
        return self.nIdCategoriaTipoTransacao

    def setIdCategoriaTipoTransacao(self, nIdCategoriaTipoTransacao):
        self.IdCategoriaTipoTransacao = nIdCategoriaTipoTransacao

    def getTransacao(self):
        return self.sTransacao

    def setTransacao(self, sTransacao):
        self.Transacao = sTransacao

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

    
