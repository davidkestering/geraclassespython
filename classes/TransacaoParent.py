class TransacaoParent:
    def __init__(self, nId,nIdTipoTransacao,nIdUsuario,sObjeto,sIp,dDtCadastro,bPublicado,bAtivo):
        self.nId = nId
        self.nIdTipoTransacao = nIdTipoTransacao
        self.nIdUsuario = nIdUsuario
        self.sObjeto = sObjeto
        self.sIp = sIp
        self.dDtCadastro = dDtCadastro
        self.bPublicado = bPublicado
        self.bAtivo = bAtivo
        
    def getId(self):
        return self.nId

    def setId(self, nId):
        self.Id = nId

    def getIdTipoTransacao(self):
        return self.nIdTipoTransacao

    def setIdTipoTransacao(self, nIdTipoTransacao):
        self.IdTipoTransacao = nIdTipoTransacao

    def getIdUsuario(self):
        return self.nIdUsuario

    def setIdUsuario(self, nIdUsuario):
        self.IdUsuario = nIdUsuario

    def getObjeto(self):
        return self.sObjeto

    def setObjeto(self, sObjeto):
        self.Objeto = sObjeto

    def getIp(self):
        return self.sIp

    def setIp(self, sIp):
        self.Ip = sIp

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

    
