from flask import Flask as Fk, render_template as rt
import mysql.connector as sql

app = Fk(__name__)

@app.route('/', methods=["GET"])
def index():

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

    #Executando a consulta
    cursor.execute("SELECT codigo_musica, cantor, duracao, titulo, imagem, categoria FROM musica;")

    #Recuperando os dados
    musicas = cursor.fetchall()

    #Fechando a conexão
    conec.close()

    return rt("principal.html", musicas = musicas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)