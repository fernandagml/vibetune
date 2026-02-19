from model.musica import recuperar_musicas as rm
from model.genero import recuperar_gerenos as rg
from flask import Flask as Fk, render_template as rt

app = Fk(__name__)

@app.route('/', methods=["GET"])
def index():

    musicas = rm()
    generos = rg()
    return rt("principal.html", musicas = musicas, generos = generos)

@app.route("/admin")
def p_admin():
    musicas = rm()
    generos = rg()
    return rt("administracao.html", musicas = musicas, generos = generos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)