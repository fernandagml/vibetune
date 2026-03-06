from database.conexao import conectar

def verificar_login(usuario:str, senha:str) -> list:
    """Função que verifica se o usuário está cadastrado"""

    conexao, cursor = conectar()
    cursor.execute("SELECT usuario, senha FROM cadastros WHERE usuario = %s AND senha = %s;", (usuario, senha)) #Executando a consulta
    login = cursor.fetchone()
    conexao.close()
    return login