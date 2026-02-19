from database.conexao import conectar

def recuperar_musicas():
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo_musica, cantor, duracao, titulo, imagem, categoria FROM musica;") #Executando a consulta
    musicas = cursor.fetchall() #Recuperando os dados
    conexao.close()
    return musicas