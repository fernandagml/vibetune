from model.musica import recuperar_musicas as rm, salvar_musica as sm, deletar as dm, status as sm
from model.genero import recuperar_gerenos as rg
from model.cadastro import cadastrar as cd
from model.login import verificar_login as vl
from flask import Flask as Fk, render_template as rt, request, redirect, session

app = Fk(__name__)

app.secret_key = "vibetune_secret_key"

@app.route('/', methods=["GET"])
def index():
    musicas = rm(True, None)
    generos = rg()
    return rt("principal.html", musicas = musicas, generos = generos)

@app.route("/admin")
def p_admin():
    if "usuario_logado" not in session:
        return redirect("/login")
    
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

@app.route("/cadastro")
def pagina_cadastro():
    return rt("cadastro.html")

@app.route("/login")
def login():
    return rt("login.html")

@app.route("/cadastro/post", methods=["POST"])
def inserir_cadastro():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    cd(usuario, senha)
    return redirect("/login")

@app.route("/login/post", methods=["POST"])
def logar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    usuario = vl(usuario, senha)
    if usuario:
        session["usuario_logado"] = usuario
        return redirect("/admin")
    else:
        return redirect("/login")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)