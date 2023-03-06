class GrupoUsuarioParent:
    def __init__(self, nId,sNmGrupoUsuario,dDtCadastro,bPublicado,bAtivo):
        self.nId = nId
        self.sNmGrupoUsuario = sNmGrupoUsuario
        self.dDtCadastro = dDtCadastro
        self.bPublicado = bPublicado
        self.bAtivo = bAtivo
        
    def getId(self):
        return self.nId

    def setId(self, nId):
        self.Id = nId

    def getNmGrupoUsuario(self):
        return self.sNmGrupoUsuario

    def setNmGrupoUsuario(self, sNmGrupoUsuario):
        self.NmGrupoUsuario = sNmGrupoUsuario

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

    
