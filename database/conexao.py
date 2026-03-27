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

    return conec, cursor