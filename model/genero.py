from database.conexao import conectar

def recuperar_gerenos():
    conexao, cursor = conectar()
    cursor.execute("SELECT categoria, icone, cor FROM genero;") #Executando a consulta
    generos = cursor.fetchall() #Recuperando os dados
    conexao.close()
    return generos