import mysql.connector as sql

def conectar():
    #Conectando no banco de dados
    conec = sql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="vibetune"
    )

    #Criando o cursor
    cursor = conec.cursor(dictionary=True)

    return conec, cursor