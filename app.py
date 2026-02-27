from model.musica import recuperar_musicas as rm, salvar_musica as sm, deletar as dm, status as sm
from model.genero import recuperar_gerenos as rg
from flask import Flask as Fk, render_template as rt, request, redirect

app = Fk(__name__)

@app.route('/', methods=["GET"])
def index():
    musicas = rm(True, None)
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

@app.route("/music/delete/<codigo>")
def deletar_musica(codigo):
    dm(codigo)
    return redirect("/admin")

@app.route("/music/status/<codigo>/<status>")
def ativar_musica(codigo, status):
    sm(codigo, status)
    return redirect("/admin")

@app.route("/music/<genero>")
def filtrar_genero(genero):
    musicas = rm(1, genero)
    generos = rg()
    return rt("principal.html", musicas = musicas, generos = generos)

@app.route("cadastro")
def cadastrar():
    return rt("cadastro.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)