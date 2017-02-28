#coding: utf-8
import pymysql


def ConectarBanco(valor):
    servidor, usuario, senha = '127.0.0.1', 'root', ''
    if valor == '0':
        servidor=input('Servidor:')
        usuario=input("Usuario:")
        senha=input("Senha:")
    elif valor == '1':
        servidor=input('Servidor:')
    elif valor == '2':
        usuario=input("Usuario:")
    elif valor == '3':
        senha=input("Senha:")

    if servidor=="":
        servidor='127.0.0.1'
    if usuario=="":
        usuario='root'
    return servidor,usuario,senha


def InicializarBanco():
    valor=input("Os valores padrões são:\n1-Servidor: 127.0.0.1\t2-Usuario: root\t\t3-Senha vazia.\n"
          "Aperte 'enter' para manter os valores padrões.\n"
          "Se deseja alterar apenas um valor digite seu número correspondente. Para mais de um digite 0.\n")
    servidor,usuario,senha = ConectarBanco(valor)
    try:
        db = pymysql.connect(servidor, usuario, senha, 'ClinicaMedica')
        cursor = db.cursor()
        return cursor, db,False
    except:
        db = pymysql.connect(servidor, usuario, senha, '')
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE ClinicaMedica DEFAULT CHARACTER SET utf8")

        db = pymysql.connect(servidor, usuario, senha, 'ClinicaMedica')
        cursor = db.cursor()
        return cursor, db,True
cursor,db,boolean = InicializarBanco()

def Executa_SQL(pSQL):
    try:
        cursor.execute(pSQL)
        db.commit()
        return True
    except:
        print("Error: Não foi possível executar o SQL")
        db.rollback()

def Busca_SQL(pSQL):
    try:
        cursor.execute(pSQL)
        results = cursor.fetchall()
        return results
    except:
        print("Error: Não foi possível buscar os dados")
        return False

def CriaTabelas():

    tabelaClinica = "CREATE TABLE IF NOT EXISTS CLINICA (CODCLI INT NOT NULL AUTO_INCREMENT, NOMECLI VARCHAR(45) NULL, LOCALCLI VARCHAR(45) NULL, PRIMARY KEY (CODCLI) ) ENGINE=InnoDB"
    Executa_SQL(tabelaClinica)

    tabelaEspecialidade = "CREATE TABLE IF NOT EXISTS ESPECIALIDADE (CODESPECI INT NOT NULL AUTO_INCREMENT, NOME VARCHAR(45) NULL, CODESPECIGENERICA INT NULL, PRIMARY KEY (CODESPECI), INDEX CODESPECIGENERICA_IDX (CODESPECIGENERICA ASC), CONSTRAINT CODESPECIGENERICA FOREIGN KEY (CODESPECIGENERICA) REFERENCES ESPECIALIDADE (CODESPECI) ON DELETE SET NULL ON UPDATE CASCADE) ENGINE=InnoDB"
    Executa_SQL(tabelaEspecialidade)

    tabelaMedico = "CREATE TABLE IF NOT EXISTS MEDICO (CODMED INT NOT NULL AUTO_INCREMENT, NOMEMED VARCHAR(45) NULL, CODESPECI INT NULL, PRIMARY KEY (CODMED), INDEX CODESPECI_IDX (CODESPECI ASC), CONSTRAINT CODESPECI FOREIGN KEY (CODESPECI) REFERENCES ESPECIALIDADE (CODESPECI) ON DELETE SET NULL ON UPDATE CASCADE) ENGINE=InnoDB"
    Executa_SQL(tabelaMedico)

    tabelaClinicaMedico = "CREATE TABLE IF NOT EXISTS CLINICAMEDICO (CODCLI INT NOT NULL, CODMED INT NOT NULL, PRIMARY KEY (CODCLI, CODMED), INDEX CODMED_IDX (CODMED ASC), CONSTRAINT CODCLI FOREIGN KEY (CODCLI) REFERENCES CLINICA (CODCLI) ON DELETE CASCADE ON UPDATE CASCADE, CONSTRAINT CODMED FOREIGN KEY (CODMED) REFERENCES MEDICO (CODMED) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB"
    Executa_SQL(tabelaClinicaMedico)

    tabelaAgendaConsulta = "CREATE TABLE IF NOT EXISTS AGENDACONSULTA (CODCLINICA INT NOT NULL, CODMEDICO INT NOT NULL, DATA DATE NOT NULL, HORA TIME NOT NULL, PRIMARY KEY (CODCLINICA, CODMEDICO, DATA, HORA), INDEX CODMEDICO_IDX (CODMEDICO ASC), CONSTRAINT CODCLINICA FOREIGN KEY (CODCLINICA) REFERENCES CLINICAMEDICO (CODCLI) ON DELETE CASCADE ON UPDATE CASCADE, CONSTRAINT CODMEDICO FOREIGN KEY (CODMEDICO) REFERENCES CLINICAMEDICO (CODMED) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB"
    Executa_SQL(tabelaAgendaConsulta)

if boolean == True: # Banco está sendo criado
    CriaTabelas()

#-------------------------------------------------------------------------------------------------------------------------------#

def InserirClinica(nome,local):
    busca = BuscarClinica(nome,local)
    if busca == False:
        insercao = Executa_SQL("INSERT INTO CLINICA(NOMECLI, LOCALCLI) VALUES ('"+nome+"', '"+local+"')")
        if insercao == True:
            return ("Clínica inserida com sucesso! \n Atualize para visualizar.")
        else:
            return ("Não foi possível inserir a clínica.")
    else:
        return ("Clínica já existe.")


def BuscarClinica(nome,local):
    #busca o objeto
    resultado = Busca_SQL("SELECT * FROM CLINICA WHERE NOMECLI = '"+nome+"' AND LOCALCLI = '"+local+"'")
    if len(resultado)==0:
        return False
    return True

def BuscarNomeClinica(nome):
    #busca clínica pelo nome
    codCli, nomeCli,localCli = [],[],[]
    resultado = Busca_SQL("SELECT * FROM CLINICA WHERE NOMECLI LIKE '%"+nome+"%'")
    if (resultado)==0:
        return None,False,"Clínica não encontrada. \n Atualize para voltar."

    for row in resultado:
        codCli.append(str(row[0]))
        nomeCli.append(row[1])
        localCli.append(row[2])
    clinicas = [codCli,nomeCli,localCli]

    return clinicas,True,None

def BuscarLocalClinica(localCli):
    #busca clínica pelo local
    cod,nome,local = [],[],[]
    resultado = Busca_SQL("SELECT * FROM CLINICA WHERE LOCALCLI LIKE '%" + localCli + "%'")
    if (resultado)==0:
        return None,False,"Clínica não encontrada. \n Atualize para voltar."

    for row in resultado:
        cod.append(str(row[0]))
        nome.append(row[1])
        local.append(row[2])
    clinicas = [cod,nome,local]

    return clinicas,True,None

def BuscarCodClinica(nome,local):
    #busca o código da clínica
    resultado = Busca_SQL("SELECT CODCLI FROM CLINICA WHERE NOMECLI = '"+nome+"' AND LOCALCLI = '"+local+"'")
    if len(resultado)==0:
        return False
    else:
        return(resultado[-1][0])

def BuscarClinicaCod(codCli):
    #busca a clínica pelo código
    cod,nome,local = [],[],[]
    codCli = str(codCli)
    resultado = Busca_SQL("SELECT * FROM CLINICA WHERE CODCLI = "+codCli+"")
    if len(resultado)==0:
        return None,False,"Clínica não encontrada. \n Atualize para voltar."

    for row in resultado:
        cod.append(str(row[0]))
        nome.append(row[1])
        local.append(row[2])
    clinicas = [cod,nome,local]

    return clinicas,True,None

def ApagarClinica(codCli):
    ## Se apagar um ID que não seja o último vai ficar o buraco e as próximas clínicas serão criadas de acordo com o último id
    lista,busca,menssagem = BuscarClinicaCod(codCli)
    if busca == True:
        codCli = str(codCli)
        delete = Executa_SQL("DELETE FROM CLINICA WHERE CODCLI = "+codCli+"")
        if delete == True:
            return ("Clínica removida com sucesso! \n Atualize para visualizar.")
        else:
            return ("Não foi possível remover a clínica.")
    else:
        return ("Clínica não existe.")

def AlterarClinica(codCli,nome,local):
    lista,codClinica,menssagem = BuscarClinicaCod(codCli)
    if codClinica != False:
        codCli = str(codCli)
        resultado = Executa_SQL("UPDATE CLINICA SET NOMECLI = '"+nome+"', LOCALCLI = '"+local+"' WHERE CODCLI = "+codCli+"")
        if resultado == True:
            return ("Clínica alterada com sucesso.\nAtualize para visualizar.")
        else:
            return ("Não foi possível alterar a clínica.")
    else:
        return ("CLínica não existe.")
    
def ListarClinicas():
    codCli,nomeCli,localCli=[],[],[]
    resultado = Busca_SQL("SELECT * FROM CLINICA")
    if len(resultado)!=0:
        for row in resultado:
            codCli.append(str(row[0]))
            nomeCli.append(row[1])
            localCli.append(row[2])
        clinicas = [codCli,nomeCli,localCli]
        return clinicas
    else:
        return None

def QuantidadeClinicas():
    resultado = Busca_SQL("SELECT COUNT(*) FROM CLINICA")
    return resultado[0][-1]

#---------------------------------------------------------------------------------------------------------------------------------------#         
                            
def InserirEspecialidade(nome,especGenerica='null'):
    busca = BuscarEspecialidade(nome,especGenerica)
    if busca == False:
        if type(especGenerica) is int:
            lista,boolean,menssagem = BuscarCodEspecialidade(especGenerica)
            if boolean==True:
                especGenerica = str(especGenerica)
                insercao = Executa_SQL("INSERT INTO ESPECIALIDADE(NOME, CODESPECIGENERICA) VALUES ('"+nome+"', "+especGenerica+")")
            else:
                return "Especialidade genérica não existe."
        else:
            insercao = Executa_SQL("INSERT INTO ESPECIALIDADE(NOME, CODESPECIGENERICA) VALUES ('" + nome + "', " + especGenerica + ")")

        if insercao == True:
            return ("Especialidade inserida com sucesso! \n Atualize para visualizar.")
        else:
            return ("Não foi possível inserir a especialidade.")
    else:
        return ("Especialidade já existe.")

def BuscarEspecialidade(nome,especGenerica='null'):
    #busca o objeto
    if type(especGenerica) is int:
        especGenerica = str(especGenerica)
        resultado = Busca_SQL("SELECT * FROM ESPECIALIDADE WHERE NOME = '"+nome+"' AND CODESPECIGENERICA = "+especGenerica+"")
    else:
        resultado = Busca_SQL("SELECT * FROM ESPECIALIDADE WHERE NOME = '"+nome+"' AND CODESPECIGENERICA IS NULL")
    if len(resultado)==0:
        return False
    return True       

'''def BuscarCodEspecialidade(nome):
    #busca o código da especialidade
    resultado = Busca_SQL("SELECT * FROM ESPECIALIDADE WHERE NOME = '"+nome+"'")
    if (resultado)==0:
        return False
    else:
        return(resultado[-1][0])    
'''
def BuscarNomeEspecialidade(nomeEspec):
    #busca especialidade pelo nome
    codEspec,nome,codEspecG = [],[],[]
    resultado = Busca_SQL("SELECT * FROM ESPECIALIDADE WHERE NOME LIKE '%"+nomeEspec+"%'")
    if len(resultado)==0:
        return None,False,"Especialidade não encontrada. \n Atualize para voltar."

    for row in resultado:
        codEspec.append(str(row[0]))
        nome.append(row[1])

        if row[2]==None:
            codEspecG.append("")
        else:
            codEspecG.append(str(row[2]))
    especialidades = [codEspec,nome,codEspecG]

    return especialidades,True,None


def BuscarCodEspecialidadeGenerica(codEspecG):
    #busca especialidade genérica pelo código generico
    codEspec,nome,codEspecGen = [],[],[]
    codEspecG = str(codEspecG)
    if codEspecG!="":
        resultado = Busca_SQL("SELECT * FROM ESPECIALIDADE WHERE CODESPECIGENERICA = "+codEspecG+"")
    else:
        resultado = Busca_SQL("SELECT * FROM ESPECIALIDADE WHERE CODESPECIGENERICA IS NULL")
    if len(resultado)==0:
        return None,False,"Especialidade não encontrada. \n Atualize para voltar."

    for row in resultado:
        codEspec.append(str(row[0]))
        nome.append(row[1])
        if row[2] == None:
            codEspecGen.append("")
        else:
            codEspecGen.append(str(row[2]))
    especialidades = [codEspec,nome,codEspecGen]

    return especialidades,True,None


def BuscarCodEspecialidade(codEspeci):
    # busca especialidade pelo código
    codEspec, nome, codEspecGen = [], [], []
    codEspeci = str(codEspeci)
    resultado = Busca_SQL("SELECT * FROM ESPECIALIDADE WHERE CODESPECI = " + codEspeci + "")
    if len(resultado) == 0:
        return None, False, "Especialidade não encontrada. \n Atualize para voltar."

    for row in resultado:
        codEspec.append(str(row[0]))
        nome.append(row[1])
        if row[2] == None:
            codEspecGen.append("")
        else:
            codEspecGen.append(str(row[2]))
    especialidades = [codEspec, nome, codEspecGen]

    return especialidades, True, None


def ApagarEspecialidade(codEspeci):
    ## Se apagar um ID que não seja o último vai ficar o buraco e as próximas clínicas serão criadas de acordo com o último id
    lista,busca,menssagem = BuscarCodEspecialidade(codEspeci)
    if busca == True:
        codEspeci = str(codEspeci)
        delete = Executa_SQL("DELETE FROM ESPECIALIDADE WHERE CODESPECI = "+codEspeci+"")
        if delete == True:
            return ("Especialidade removida com sucesso! \n Atualize para visualizar.")
        else:
            return ("Não foi possível remover a especialidade.")
    else:
        return ("Especialidade não existe")
          
def AlterarEspecialidade(codEspeci,nome,especGenerica='null'):
    lista,codEspec,menssagem = BuscarCodEspecialidade(codEspeci)
    if codEspec != False:
        codEspeci = str(codEspeci)
        if especGenerica == 'null':
            resultado = Executa_SQL("UPDATE ESPECIALIDADE SET NOME = '"+nome+"', CODESPECIGENERICA = null WHERE CODESPECI = "+codEspeci+"")
        else:
            lista,codEspecGen,menssagem = BuscarCodEspecialidade(especGenerica)
            if codEspecGen!=False:
                especGenerica = str(especGenerica)
                resultado = Executa_SQL("UPDATE ESPECIALIDADE SET NOME = '"+nome+"', CODESPECIGENERICA = "+especGenerica+" WHERE CODESPECI = "+codEspeci+"")
            else:
                return "Especialidade genérica não existe."

        if resultado == True:
            return ("Especialidade alterada com sucesso.\nAtualize para visualizar.")
        else:
            return ("Não foi possível alterar a especialidade.")
    else:
        return ("Especialidade não existe.")

def ListarEspecialidades():
    codEspec, nomeEspec, codEspecGen = [],[],[]
    resultado = Busca_SQL("SELECT * FROM ESPECIALIDADE")
    if len(resultado)!=0:
        for row in resultado:
            codEspec.append(str(row[0]))
            nomeEspec.append(row[1])
            if row[2]==None:
                codEspecGen.append("")
            else:
                codEspecGen.append(str(row[2]))
        especialidades = [codEspec, nomeEspec, codEspecGen]
        return especialidades
    else:
        return None


def QuantidadeEspecialidades():
    resultado = Busca_SQL("SELECT COUNT(*) FROM ESPECIALIDADE")
    return resultado[0][-1]

#--------------------------------------------------------------------------------------------------------------------------------#

def InserirMedico(nomeMed,codEspeci='null'):
    busca = BuscarMedico(nomeMed,codEspeci)
    if busca == False:
        if type(codEspeci) is int:
            lista,boolean,menssagem = BuscarCodEspecialidade(codEspeci)
            if boolean == True:
                codEspeci = str(codEspeci)
                insercao = Executa_SQL("INSERT INTO MEDICO(NOMEMED, CODESPECI) VALUES ('"+nomeMed+"', "+codEspeci+")")
            else:
                return ("Especialidade não existe.")
        else:
            insercao = Executa_SQL("INSERT INTO MEDICO(NOMEMED) VALUES ('"+nomeMed+"')")

        if insercao == True:
            return ("Médico inserido com sucesso! \n Atualize para visualizar.")
        else:
            return ("Não foi possível inserir o médico.")
    else:
        return ("Médico já cadastrado.")

def BuscarMedico(nomeMed,codEspeci='null'):
    #busca o objeto
    if type(codEspeci) is int:
        codEspeci = str(codEspeci)
        resultado = Busca_SQL("SELECT * FROM MEDICO WHERE NOMEMED = '"+nomeMed+"' AND CODESPECI = "+codEspeci+"")
    else:
        resultado = Busca_SQL("SELECT * FROM MEDICO WHERE NOMEMED = '"+nomeMed+"' AND CODESPECI IS NULL")
    if len(resultado)==0:
        return False
    return True      

def BuscarMedicoCod(codMed):
    #busca médico pelo código
    codMedico,nome,codEspeci = [],[],[]
    codMed = str(codMed)
    resultado = Busca_SQL("SELECT * FROM MEDICO WHERE CODMED = "+codMed+"")
    if len(resultado)==0:
        return None,False,"Médico não encontrado.\n Atualize para retornar."
    for row in resultado:
        codMedico.append(str(row[0]))
        nome.append(row[1])
        if row[2]!= None:
            codEspeci.append(str(row[2]))
        else:
            codEspeci.append("")
    medicos = [codMedico,nome,codEspeci]

    return medicos,True,None

def BuscarCodMedico(nomeMed):
    #busca código do médico
    resultado = Busca_SQL("SELECT * FROM MEDICO WHERE NOMEMED = '"+nomeMed+"'")
    if (resultado)==0:
        return False
    else:
        return(resultado[-1][0])
    
def BuscarNomeMedico(nomeMed):
    # busca o médico pelo nome
    codMed,nome,codEspeci=[],[],[]
    resultado = Busca_SQL("SELECT * FROM MEDICO WHERE NOMEMED LIKE '%"+nomeMed+"%'")
    if len(resultado)==0:
        return None,False,"Médico não encontrado.\n Atualize para retornar."
    for row in resultado:
        codMed.append(str(row[0]))
        nome.append(row[1])
        if row[2]==None:
            codEspeci.append("")
        else:
            codEspeci.append(str(row[2]))
    medicos = [codMed,nome,codEspeci]
    return medicos,True,None

def BuscarEspecialidadeMedico(codEspeci):
    #busca o médico pela especialidade
    codMed,nome,codE = [],[],[]
    codEspeci = str(codEspeci)
    if codEspeci!="":
        resultado = Busca_SQL("SELECT * FROM MEDICO WHERE CODESPECI = "+codEspeci+"")
    else:
        resultado = Busca_SQL("SELECT * FROM MEDICO WHERE CODESPECI IS NULL")
    if len(resultado)==0:
        return None,False,"Médico não encontrado. \n Atualize para voltar."
    for row in resultado:
        codMed.append(str(row[0]))
        nome.append(row[1])
        if row[2]==None:
            codE.append("")
        else:
            codE.append(str(row[2]))
    medicos = [codMed,nome,codE]

    return medicos,True,None

def ApagarMedico(codMed):
    # Se apagar um ID que não seja o último vai ficar o buraco e as próximas clínicas serão criadas de acordo com o último id
    lista,busca,menssagem = BuscarMedicoCod(codMed)
    if busca == True:
        codMed = str(codMed)
        delete = Executa_SQL("DELETE FROM MEDICO WHERE CODMED = "+codMed+"")
        if delete == True:
            return "Médico removido com sucesso! \n Atualize para visualizar."
        else:
            return "Não foi possível remover o médico."
    else:
        return "Médico não existe."

def AlterarMedico(codMedi,nomeMed,codEspeci='null'):
    resultado,codMed,menssagem = BuscarMedicoCod(codMedi)
    if codMed != False:
        codMedi = str(codMedi)
        if codEspeci == 'null':
            resultado = Executa_SQL("UPDATE MEDICO SET NOMEMED = '"+nomeMed+"', CODESPECI = null WHERE CODMED = "+codMedi+"")
        else:
            resultado, codEspec, menssagem = BuscarCodEspecialidade(codEspeci)
            if codEspec!= False:
                codEspeci = str(codEspeci)
                resultado = Executa_SQL("UPDATE MEDICO SET NOMEMED = '"+nomeMed+"', CODESPECI = "+codEspeci+" WHERE CODMED = "+codMedi+"")
            else:
                return "Especialidade não existe"
        if resultado == True:
            return ("Médico alterado com sucesso. \n Atualize para visualizar.")
        else:
            return("Não foi possível alterar o médico.")
    else:
        return ("Médico não existe.")

def ListarMedicos():
    codMed,nomeMed,codEspeciMed = [],[],[]
    resultado = Busca_SQL("SELECT * FROM MEDICO")
    if len(resultado)==0:
        return None
    else:
        for row in resultado:
            codMed.append(str(row[0]))
            nomeMed.append(row[1])
            if row[2]==None:
                codEspeciMed.append("")
            else:
                codEspeciMed.append(str(row[2]))
        medicos = [codMed,nomeMed,codEspeciMed]
        return medicos

def QuantidadeMedicos():
    resultado = Busca_SQL("SELECT COUNT(*) FROM MEDICO")
    return resultado[0][-1]

#--------------------------------------------------------------------------------------------------------------------------------#

def InserirClinicaMedico(codCli,codMed):
    lista,clinica,menssagem = BuscarClinicaCod(codCli)
    lista,medico,menssagem = BuscarMedicoCod(codMed)
    if clinica==False or medico == False:
        return "Clínica ou Médico não existe(m)!"
    busca = BuscarClinicaMedico(codCli,codMed)
    if busca == False:
        codMed = str(codMed)
        codCli = str(codCli)
        insercao = Executa_SQL("INSERT INTO CLINICAMEDICO(CODCLI, CODMED) VALUES ("+codCli+", "+codMed+")")
        if insercao == True:
            return ("Clínica+Médico inseridos com sucesso!\n Atualize para visualizar.")
        else:
            return ("Não foi possível inserir clínica+médico.")
    else:
        return ("CLínica+Médico já cadastrado.")

def BuscarClinicaMedico(codCli,codMed):
    #busca o objeto
    codCli = str(codCli)
    codMed = str(codMed)
    resultado = Busca_SQL("SELECT * FROM CLINICAMEDICO WHERE CODCLI = "+codCli+" AND CODMED = "+codMed+"")
    if len(resultado)==0:
        return False
    return True   

def BuscarCodMed(codCli):
    #busca código médico pelo código da clínica
    codClinica,codMedico = [],[]
    codCli = str(codCli)
    resultado = Busca_SQL("SELECT * FROM CLINICAMEDICO WHERE CODCLI = "+codCli+"")
    if (resultado)==0:
        return None,False,"Clínica+Médico não encontrada. \n Atualize para voltar."

    for row in resultado:
        codClinica.append(str(row[0]))
        codMedico.append(str(row[1]))
    clinicaMedicos = [codClinica,codMedico]
    #resultado[-1][1]
    return clinicaMedicos,True,None

def BuscarCodCli(codMed):
    #busca código da clínica pelo código do médico
    codClinica,codMedico = [],[]
    codMed = str(codMed)
    resultado = Busca_SQL("SELECT * FROM CLINICAMEDICO WHERE CODMED = "+codMed+"")
    if (resultado)==0:
        return None,False,"Clínica+Médico não encontrada. \n Atualize para voltar."

    for row in resultado:
        codClinica.append(str(row[0]))
        codMedico.append(str(row[1]))
    clinicaMedicos = [codClinica,codMedico]
    return clinicaMedicos,True,None

def ApagarClinicaMedico(codCli,codMed):
    busca = BuscarClinicaMedico(codCli, codMed)
    if busca == True:
        codCli = str(codCli)
        codMed = str(codMed)
        delete = Executa_SQL("DELETE FROM CLINICAMEDICO WHERE CODCLI = "+codCli+" AND CODMED = "+codMed+"")
        if delete == True:
            return ("Clínica+Médico removido com sucesso! \n Atualize para visualizar.")
        else:
            return ("Não foi possível remover a clínica+médico.")
    else:
        return ("Clínica+Médico não existem.")
            
def ListarClinicaMedicos():
    codCli,codMed = [],[]
    resultado = Busca_SQL("SELECT * FROM CLINICAMEDICO")
    if len(resultado)!=0:
        for row in resultado:
            codCli.append(str(row[0]))
            codMed.append(str(row[1]))
        clinicaMedicos = [codCli,codMed]
        return clinicaMedicos
    else:
        return None

def QuantidadeClinicaMedicos():
    resultado = Busca_SQL("SELECT COUNT(*) FROM CLINICAMEDICO")
    return resultado[0][-1]

#--------------------------------------------------------------------------------------------------------------------------------#

def BuscarConsulta(codClinica,codMedico,dia,hora):
    #busca o objeto
    dia = dia.split("/")[::-1]
    date = dia[0]+"-"+dia[1]+"-"+dia[2]
    codClinica = str(codClinica)
    codMedico = str(codMedico)
    resultado = Busca_SQL("SELECT * FROM AGENDACONSULTA WHERE CODCLINICA = "+codClinica+" AND CODMEDICO = "+codMedico+" AND DATA = '"+date+"' AND HORA = '"+hora+"'")
    if len(resultado)==0:
        return False
    return True

def AgendarConsulta(codClinica,codMedico,dia,hora):
    lista,buscaCodCli,aviso = BuscarClinicaCod(codClinica)
    lista,buscaCodMed,aviso = BuscarMedicoCod(codMedico)
    if buscaCodCli == False or buscaCodMed == False:
        return "Clínica ou Médico não existe(m)!"
    busca = BuscarConsulta(codClinica,codMedico,dia,hora)
    dia = dia.split("/")[::-1]
    date = dia[0]+"-"+dia[1]+"-"+dia[2]
    codClinica = str(codClinica)
    codMedico = str(codMedico)    
    if busca == False:
        insercao = Executa_SQL("INSERT INTO AGENDACONSULTA(CODCLINICA, CODMEDICO, DATA, HORA) VALUES ("+codClinica+", "+codMedico+", '"+date+"', '"+hora+"')")
        if insercao == True:
            return ("Consulta inserida com sucesso!\n Atualize para visualizar.")
        else:
            return ("Não foi possível agendar a consulta.")
    else:
        return ("Consulta já existe.")

def BuscarConsultaCodClinica(codClinica):
    #busca consulta pelo código da clínica
    codCli,codMed,data,hora = [],[],[],[]
    codClinica = str(codClinica)
    resultado = Busca_SQL("SELECT CODCLINICA, CODMEDICO, DATE_FORMAT(DATA, '%d/%m/%Y'), HORA FROM AGENDACONSULTA WHERE CODCLINICA = "+codClinica+"")
    if (resultado)==0:
        return None,False,"Não há consultas nessa clínica.\n Atualize para voltar."

    for row in resultado:
        codCli.append(str(row[0]))
        codMed.append(str(row[1]))
        data.append(row[2])
        hora.append(str(row[3]))
    consultas = [codCli,codMed,data,hora]

    return consultas,True,None

def BuscarConsultaCodMedico(codMedico):
    #busca consulta pelo código do médico
    codCli,codMed,data,hora = [],[],[],[]
    codMedico = str(codMedico)
    resultado = Busca_SQL("SELECT CODCLINICA, CODMEDICO, DATE_FORMAT(DATA, '%d/%m/%Y'), HORA FROM AGENDACONSULTA WHERE CODMEDICO = "+codMedico+"")
    if (resultado) == 0:
        return None,False,"Não há consultas com esse médico.\n Atualize para voltar."

    for row in resultado:
        codCli.append(str(row[0]))
        codMed.append(str(row[1]))
        data.append(row[2])
        hora.append(str(row[3]))
    consultas = [codCli,codMed,data,hora]

    return consultas,True,None

def BuscarConsultaData(dataCons):
    #busca consulta pela data
    codCli,codMed,data,hora =[],[],[],[]
    dataCons = dataCons.split("/")[::-1]
    date = dataCons[0] + "-" + dataCons[1] + "-" + dataCons[2]
    resultado = Busca_SQL("SELECT CODCLINICA, CODMEDICO, DATE_FORMAT(DATA, '%d/%m/%Y'), HORA FROM AGENDACONSULTA WHERE DATA = '"+date+"'")
    if (resultado) == 0:
        return None,False,"Não há consultas nessa data.\n Atualize para voltar."
    for row in resultado:
        codCli.append(str(row[0]))
        codMed.append(str(row[1]))
        data.append(row[2])
        hora.append(str(row[3]))
    consultas = [codCli,codMed,data,hora]

    return consultas,True,None

def BuscarConsultaHora(horaCons):
    #busca consulta pela hora
    codCli,codMed,data,hora = [],[],[],[]
    resultado = Busca_SQL("SELECT CODCLINICA, CODMEDICO, DATE_FORMAT(DATA, '%d/%m/%Y'), HORA FROM AGENDACONSULTA WHERE HORA = '" + horaCons + "'")
    if (resultado) == 0:
        return None,False,"Não há consultas nesse horário. \n Atualize para voltar."

    for row in resultado:
        codCli.append(str(row[0]))
        codMed.append((str(row[1])))
        data.append(row[2])
        hora.append(str(row[3]))
    consultas = [codCli,codMed,data,hora]

    return consultas,True,None

def AlterarConsulta(codClinica, codMedico, data,novaData, hora,novaHora):
    busca = BuscarConsulta(codClinica, codMedico, data, hora)
    dia = novaData.split("/")[::-1]
    date = dia[0]+"-"+dia[1]+"-"+dia[2]
    dataAnt = data.split("/")[::-1]
    data = dataAnt[0]+"-"+dataAnt[1]+"-"+dataAnt[2]
    if busca == True:
        codClinica = str(codClinica)
        codMedico = str(codMedico)
        resultado = Executa_SQL("UPDATE AGENDACONSULTA SET DATA = '" + date +"', HORA = '" + novaHora + "' WHERE CODCLINICA = "+codClinica+" AND CODMEDICO = "+codMedico+" AND DATA = '"+data+"' AND HORA = '"+hora+"'")
        if resultado == True:
            return "Consulta alterada com sucesso.\nAtualize para visualizar."
        else:
            return "Não foi possível alterar a consulta."
    else:
        return "Consulta não existe."
        
def DesmarcarConsulta(codClinica,codMedico,dia,hora):
    busca = BuscarConsulta(codClinica, codMedico, dia, hora)
    dia = dia.split("/")[::-1]
    date = dia[0]+"-"+dia[1]+"-"+dia[2]
    if busca == True:
        codClinica = str(codClinica)
        codMedico = str(codMedico)
        delete = Executa_SQL("DELETE FROM AGENDACONSULTA WHERE CODCLINICA = "+codClinica+" AND CODMEDICO = "+codMedico+" AND DATA = '"+date+"' AND HORA = '"+hora+"'")
        if delete == True:
            return ("Consulta desmarcada com sucesso! \n Atualize para visualizar.")
        else:
            return ("Não foi possível desmarcar a consulta.")
    else:
        return ("Consulta não existe.")

def ListarConsultas():
    codClinica,codMedico,data,hora = [],[],[],[]
    resultado = Busca_SQL("SELECT CODCLINICA, CODMEDICO, DATE_FORMAT(DATA, '%d/%m/%Y'), HORA FROM AGENDACONSULTA")
    if len(resultado)!=0:
        for row in resultado:
            codClinica.append(str(row[0]))
            codMedico.append(str(row[1]))
            data.append(row[2])
            hora.append(str(row[3]))
        consultas = [codClinica,codMedico,data,hora]
        return consultas
    else:
        return None


def QuantidadeConsultas():
    resultado = Busca_SQL("SELECT COUNT(*) FROM AGENDACONSULTA")
    return resultado[0][-1]
#--------------------------------------------------------------------------------------------------------------------------------#
