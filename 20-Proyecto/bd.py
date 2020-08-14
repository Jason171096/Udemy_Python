import mysql.connector
import hashlib

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="notas"
)

mycursor = mydb.cursor(buffered=True)

def insertUser(Name, Last_Name, Email, Pass):
    #Cifrar contraseña
    cifrado = haslib.sha256()
    cifrado.update(Pass.encode('utf8'))
    sql = """INSERT INTO usuario VALUES
    (null, %s, %s, %s, %s) 
    """
    values = (Name, Last_Name, Email, cifrado.hexdigest())
    mycursor.execute(sql, values)
    mydb.commit()
    if(mycursor.rowcount == 1):
        return True
    else:
        return False

def checkUser(Email, Pass):
    sql = """SELECT COUNT(1) FROM usuario 
    where Correo = %s and Password = %s"""
    values = (Email, Pass)
    mycursor.execute(sql, values)
    myresult = mycursor.fetchone()
    for result in myresult:
        if result == 1:
            return True
        else:
            return False

def returnName(Email):
    sql = "SELECT IDUsuario, Nombre FROM usuario where Correo = %s"
    values = (Email,)
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    return myresult
        
def insertNota(IDUsuario ,TituloNota, ContentNota):
    sql = """INSERT INTO nota VALUES
        (null, %s, %s, %s)
    """
    values = (IDUsuario, TituloNota, ContentNota)
    mycursor.execute(sql, values)
    mydb.commit()
    if(mycursor.rowcount == 1):
        return True
    else:
        return False

def showNotas(IDUsuario):
    sql = """SELECT * FROM nota where IDUsuario = %s"""
    values = (IDUsuario,)
    mycursor.execute(sql, values)
    myresult = mycursor.fetchall()
    return myresult

def deleteNota(IDUsuario, IDNota):
    sql = """DELETE FROM nota where IDUsuario = %s and IDNota = %s """
    values = (IDUsuario, IDNota)
    mycursor.execute(sql, values)
    mydb.commit()
    myresult = mycursor.rowcount
    if myresult == 1:
        return True
    else:
        return False