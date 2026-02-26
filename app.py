from model.musica import recuperar_musicas as rm, salvar_musica as sm
from model.genero import recuperar_gerenos as rg
from flask import Flask as Fk, render_template as rt, request, redirect

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

@app.route("/music/post", methods=["POST"])
def api_inserir_musica():
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    titulo = request.form.get("titulo")
    imagem = request.form.get("imagem")
    categoria = request.form.get("categoria")
    print(categoria)
    if sm(cantor, duracao, titulo, imagem, categoria):
        return redirect("/admin")
    else:
        return "ERRO! Não foi possível adicionar a música"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)