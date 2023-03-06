import pyodbc


class Conexao:
    def __init__(self, sServidor='BANCO'):
        self.pConexao = None
        self.pConsulta = None
        self.pBanco = None
        self.sErro = None
        self.sSqlError = None
        self.nQtdTabelas = None
        self.nQtdCampos = None
        self.sServidor = sServidor
        self.setServidor(sServidor)
        if sServidor == 'LOCAL':
            self.conectaBD('WINDOWS_SERVER\MSSQLSERVER01', 'sa', 'sa', 'dbteste')
        elif sServidor == 'BANCO':
            self.conectaBD('localhost', '', '', '')
        else:
            raise Exception(f'Não foi possível conectar ao servidor: {sServidor}')

    def setServidor(self, sServidor):
        self.sServidor = sServidor

    def getServidor(self):
        return self.sServidor

    def conectaBD(self, sHost, sUser, sSenha, sBanco):
        self.pConexao = pyodbc.connect(f"Driver={{SQL Server}};Server={sHost};Database={sBanco};uid={sUser};pwd={sSenha}")

    def execute(self, sSql):
        self.pConsulta = self.pConexao.cursor()
        try:
            self.pConsulta.execute(sSql)
            #self.pConsulta.commit()
        except pyodbc.Error as e:
            self.sSqlError = str(e)
            self.sErro = f'Ocorreu o seguinte erro na consulta: {self.sSqlError} <br> Query: {sSql}'
            self.insereErroSql(sSql)
            return self.getErro()

    def insereErroSql(self, sSql):
        try:
            with self.pConexao.cursor() as cursor:
                sSqlErroExecucao = f"INSERT INTO seg_erros_mysql (erro,ip,publicado) VALUES ('{self.escapeString(self.getErro())}','{IP_SERVIDOR}',1)"
                cursor.execute(sSqlErroExecucao)
                self.pConexao.commit()
        except pyodbc.Error as e:
            self.sSqlError = str(e)
            self.sErro = f'Ocorreu o seguinte erro na inserção do erro na tabela seg_erros_mysql: {self.sSqlError} <br> Query: {sSql}'

    #def recordCount(self):
    #    return self.pConsulta.rowcount()

    def fetchObject(self):
        return self.pConsulta.fetchone()

    def close(self):
        self.pConexao.close()

    def getErroSql(self):
        return self.sSqlError

    def setConexao(self,sBanco):
        self.pConexao = Conexao(sServidor=sBanco)

    def getConexao(self):
        return self.pConexao

    def getConsulta(self):
        return self.pConsulta

    def getErro(self):
        return self.sErro

    def escapeString(self, sAtributo):
        return sAtributo.replace("'", "''")

    def unescapeString(self, sEscapedString):
        sEscapedString = sEscapedString.replace("'", "")
        sEscapedString = sEscapedString.replace("\"", "")
        return sEscapedString

    def getLastId(self):
        return self.pConsulta.lastrowid

    def setQtdTabelas(self,nQtdTabelas):
        self.nQtdTabelas = nQtdTabelas

    def getQtdTabelas(self):
        return self.nQtdTabelas

    def setQtdCampos(self,nQtdCampos):
        self.nQtdCampos = nQtdCampos

    def getQtdCampos(self):
        return self.nQtdCampos

    def carregaQtdTabelas(self):
        self.pConsulta = self.pConexao.cursor()
        sSql = "SELECT count(0) as qtd FROM INFORMATION_SCHEMA.TABLES"
        self.pConsulta.execute(sSql)
        oReg = self.pConsulta.fetchone()
        if oReg:
            self.setQtdTabelas(oReg.qtd)
        return self.getQtdTabelas()

    def pegaTabelas(self):
        self.pConsulta = self.pConexao.cursor()
        sSql = "SELECT * FROM INFORMATION_SCHEMA.TABLES"
        self.pConsulta.execute(sSql)
        voObjeto = []
        while True:
            oReg = self.pConsulta.fetchone()
            if not oReg:
                break
            voObjeto.append(oReg)
            del oReg
        return voObjeto

    def carregaQtdCampos(self,sNomeBanco,sNomeTabela):
        self.pConsulta = self.pConexao.cursor()
        sSql = f"select count(COLUMN_NAME) as qtd from information_schema.columns where TABLE_CATALOG = '{sNomeBanco}' and table_name = '{sNomeTabela}'"
        self.pConsulta.execute(sSql)
        oReg = self.pConsulta.fetchone()
        if oReg:
            self.setQtdTabelas(oReg.qtd)
        return self.getQtdTabelas()

    def pegaCampos(self,sNomeBanco,sNomeTabela):
        self.pConsulta = self.pConexao.cursor()
        sSql = f"""select T.TABLE_CATALOG, T.TABLE_SCHEMA, T.TABLE_NAME, C.COLUMN_NAME, C.DATA_TYPE, SUBSTRING(CCU.CONSTRAINT_NAME,1,2) as PRI from INFORMATION_SCHEMA.TABLES T
                    join INFORMATION_SCHEMA.COLUMNS C
                        on C.TABLE_CATALOG = T.TABLE_CATALOG
                        and C.TABLE_NAME = T.TABLE_NAME
                        and C.TABLE_SCHEMA = T.TABLE_SCHEMA
                    left join INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE CCU
                        on CCU.TABLE_CATALOG = C.TABLE_CATALOG
                        and CCU.TABLE_NAME = C.TABLE_NAME
                        and CCU.TABLE_SCHEMA = C.TABLE_SCHEMA
                        and CCU.COLUMN_NAME = C.COLUMN_NAME
                        and SUBSTRING(CCU.CONSTRAINT_NAME,1,2) = 'PK'
                    where T.TABLE_CATALOG = '{sNomeBanco}' and T.TABLE_NAME = '{sNomeTabela}' order by C.ORDINAL_POSITION"""
        self.pConsulta.execute(sSql)
        voObjeto = []
        while True:
            oReg = self.pConsulta.fetchone()
            if not oReg:
                break
            voObjeto.append(oReg)
            del oReg
        return voObjeto