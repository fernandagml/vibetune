from database.conexao import conectar

def recuperar_musicas():
    """Função criada para buscar as músicas salvas no banco de dados."""
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo_musica, cantor, duracao, titulo, imagem, categoria, status_musica FROM musica;") #Executando a consulta
    musicas = cursor.fetchall() #Recuperando os dados
    conexao.close()
    return musicas

def salvar_musica(cantor:str, duracao:str, titulo:str, imagem:str, categoria:str) -> bool:
    """Função criada para adicionar uma música no banco de dados."""

    try:
        conexao, cursor = conectar()
        cursor.execute("INSERT INTO musica (cantor, duracao, titulo, imagem, categoria) VALUES (%s, %s, %s, %s, %s);", (cantor, duracao, titulo, imagem, categoria))
        conexao.commit()
        conexao.close()
        return True
    
    except Exception as erro:
        print(erro)
        return False
    
def deletar(codigo:int) -> bool:
    """Função criada para deletar uma música no banco de dados."""

    try:
        conexao, cursor = conectar()
        cursor.execute("DELETE FROM musica WHERE codigo_musica = %s;", (codigo,))
        conexao.commit()
        conexao.close()
        return True
    
    except Exception as erro:
        print(erro)
        return False
    
def status(codigo:int, status:bool):

    status = int(status)
    if status == 1:
        status = 0
    else:
        status = 1
        
    try:
        conexao, cursor = conectar()
        cursor.execute("UPDATE musica SET status_musica = %s WHERE codigo_musica = %s;", (status, codigo))
        conexao.commit()
        conexao.close()
        return True
    
    except Exception as erro:
        print(erro)
        return False