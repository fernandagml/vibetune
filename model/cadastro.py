from database.conexao import conectar

def cadastrar(usuario:str, senha:str) -> bool:
    """Função que cadastra um usuário"""
    try:
        conexao, cursor = conectar()
        cursor.execute("INSERT INTO cadastros (usuario, senha) VALUES (%s, %s)", (usuario, senha)) #Executando a consulta
        conexao.commit()
        conexao.close()
        return True
    
    except Exception as erro:
        print(erro)
        return False