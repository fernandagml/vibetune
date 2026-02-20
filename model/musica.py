from database.conexao import conectar

def recuperar_musicas():
    """Função criada para buscar as músicas salvas no banco de dados."""
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo_musica, cantor, duracao, titulo, imagem, categoria FROM musica;") #Executando a consulta
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