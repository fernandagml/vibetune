<<<<<<< HEAD
import mysql.connector as sql

def conectar():
    tipo_conexao = 'NUVEM'
    #Conectando no banco de dados
    if tipo_conexao == 'LOCAL':
        conec = sql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="vibetune"
        )
    else:
        conec = sql.connect(
            host="servidor-vibetune-fernanda-web-server-fernanda-vibetune.a.aivencloud.com",
            port=16941,
            user="avnadmin",
            password="AVNS_RZ_rsqrnYIWX1aFuu9I",
            database="vibetune"
        )

    #Criando o cursor
    cursor = conec.cursor(dictionary=True)

=======
import mysql.connector as sql

def conectar():
    tipo_conexao = 'NUVEM'
    #Conectando no banco de dados
    if tipo_conexao == 'LOCAL':
        conec = sql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="vibetune"
        )
    else:
        conec = sql.connect(
            host="servidor-vibetune-fernanda-web-server-fernanda-vibetune.a.aivencloud.com",
            port=16941,
            user="avnadmin",
            password="AVNS_RZ_rsqrnYIWX1aFuu9I",
            database="vibetune"
        )

    #Criando o cursor
    cursor = conec.cursor(dictionary=True)

>>>>>>> 52335547b8e3503c4d09e6ea11bf082c120335f6
    return conec, cursor