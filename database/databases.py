import sqlite3
from sqlite3.dbapi2 import Connection

QUERY_SQL = "SELECT * from funcionarios"
ERROR_FIND =  {'Error': 'Funcionario não existe no banco de dados.'}

def CriarBancoDados():
    with sqlite3.connect("funcionarios.db") as Connection:
        c = Connection.cursor()
        c.execute("CREATE TABLE funcionarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER,cargo TEXT)")
        c.execute("INSERT INTO funcionarios VALUES('0','Felipe','26','Analista de sistema')")
        c.close()
    pass

def pesquisaBasica(campo,nome):
    conection = sqlite3.connect("database/funcionarios.db")
    cursor = conection.cursor()
    QUERY_SQL = "SELECT * from funcionarios WHERE {fieldID}='{nameID}'".format(fieldID=campo,nameID=nome)
    result = cursor.execute(QUERY_SQL)
    result = result.fetchall()
    conection.close()
    if result == []:
        return {'Error':'Funcionario não existe no banco de dados.'}
    else:
        return result

def todosRegistros():
    conection = sqlite3.connect("database/funcionarios.db")
    cursor = conection.cursor()
    QUERY_SQL = "SELECT * from funcionarios"
    result = cursor.execute(QUERY_SQL)
    result = result.fetchall()
    conection.close()
    return result

def adicionarFuncionario(id,name,age,ocupacion):
    connection = sqlite3.connect("database/funcionarios.db")
    cursor = connection.cursor()
    QUERY_SQL = "INSERT INTO funcionarios VALUES({idCod},'{nameArg}','{ageArg}','{ocupacionArg}')".format(nameArg=name,ageArg=age,ocupacionArg=ocupacion,idCod=id)
    cursor.execute(QUERY_SQL)
    connection.commit()
    connection.close()
    return "Dados Atualizdos com  sucesso!!"

def removerFuncionario(funcionario):
    connection = sqlite3.connect("database/funcionarios.db")
    cursor = connection.cursor()
    if pesquisaBasica("nome",funcionario) == ERROR_FIND:
        return "Funcionario não existe no banco de dados"
    else:
        QUERY_SQL = "DELETE  from funcionarios WHERE nome ='{n}'".format(n=funcionario)
        cursor.execute(QUERY_SQL)
        connection.commit()
        connection.close()
        return " Registros de {nameID} foram apagadas com sucesso!!".format(nameID=funcionario)

