class ErrosMysqlParent:
    def __init__(self, nId,sErro,nIdUsuario,sIp,dDtCadastro,bPublicado,bAtivo):
        self.nId = nId
        self.sErro = sErro
        self.nIdUsuario = nIdUsuario
        self.sIp = sIp
        self.dDtCadastro = dDtCadastro
        self.bPublicado = bPublicado
        self.bAtivo = bAtivo
        
    def getId(self):
        return self.nId

    def setId(self, nId):
        self.Id = nId

    def getErro(self):
        return self.sErro

    def setErro(self, sErro):
        self.Erro = sErro

    def getIdUsuario(self):
        return self.nIdUsuario

    def setIdUsuario(self, nIdUsuario):
        self.IdUsuario = nIdUsuario

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

    
