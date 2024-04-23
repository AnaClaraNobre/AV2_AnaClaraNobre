import psycopg2
from psycopg2 import Error

conectar = lambda: psycopg2.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="AV2_Funcional"
)
conn = conectar()

executar_consulta = lambda conexao, consulta, parametros=None: (lambda cursor: (cursor.execute(consulta, parametros), conexao.commit(), print("Operação bem-sucedida.")))(conn.cursor())

inserir_usuario = lambda conexao, nome, país, id_console: executar_consulta(conexao, "INSERT INTO USERS (name, country, id_console) VALUES (%s, %s, %s)", (nome, país, id_console))
excluir_usuario = lambda conexao, id_usuario: executar_consulta(conexao, "DELETE FROM USERS WHERE id = %s", (id_usuario,))
selecionar_todos_usuarios = lambda conexao: (lambda cursor: (cursor.execute("SELECT * FROM USERS"), print("Consulta de todos os usuários:"), [print(linha) for linha in cursor.fetchall()]))(conexao.cursor())

inserir_video_game = lambda conexao, nome, id_empresa, data_lançamento: executar_consulta(conexao, "INSERT INTO VIDEOGAMES (name, id_company, release_date) VALUES (%s, %s, %s)", (nome, id_empresa, data_lançamento))
excluir_video_game = lambda conexao, id_video_game: executar_consulta(conexao, "DELETE FROM VIDEOGAMES WHERE id_console = %s", (id_video_game,))
selecionar_todos_video_games = lambda conexao: (lambda cursor: (cursor.execute("SELECT * FROM VIDEOGAMES"), print("Consulta de todos os videogames:"), [print(linha) for linha in cursor.fetchall()]))(conexao.cursor())

inserir_jogo = lambda conexao, título, gênero, data_lançamento, id_console: executar_consulta(conexao, "INSERT INTO GAMES (title, genre, release_date, id_console) VALUES (%s, %s, %s, %s)", (título, gênero, data_lançamento, id_console))
excluir_jogo = lambda conexao, id_jogo: executar_consulta(conexao, "DELETE FROM GAMES WHERE id_game = %s", (id_jogo,))
selecionar_todos_jogos = lambda conexao: (lambda cursor: (cursor.execute("SELECT * FROM GAMES"), print("Consulta de todos os jogos:"), [print(linha) for linha in cursor.fetchall()]))(conexao.cursor())

inserir_empresa = lambda conexao, nome, país: executar_consulta(conexao, "INSERT INTO COMPANY (name, country) VALUES (%s, %s)", (nome, país))
excluir_empresa = lambda conexao, id_empresa: executar_consulta(conexao, "DELETE FROM COMPANY WHERE id_company = %s", (id_empresa,))
selecionar_todas_empresas = lambda conexao: (lambda cursor: (cursor.execute("SELECT * FROM COMPANY"), print("Consulta de todas as empresas:"), [print(linha) for linha in cursor.fetchall()]))(conexao.cursor())

conn.close()