from database.conexao import conectar

def login(usuario, senha):

    conexao, cursor = conectar()
    cursor.execute("SELECT usuario, senha FROM cadastros WHERE usuario = %s AND senha = %s;", (usuario, senha)) #Executando a consulta
    login = cursor.fetchone()
    conexao.close()
    return login