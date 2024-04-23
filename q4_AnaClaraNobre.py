import psycopg2
from psycopg2 import Error

conectar = lambda: psycopg2.connect(
    user="postgres",
    password="admin",
    host="localhost",
    port="5432",
    database="AV2_Funcional"
)

def executar_consulta(consulta_sql):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()
        if resultados:
            print("Resultados da consulta:")
            for resultado in resultados:
                print(resultado)
        else:
            print("Nenhum resultado encontrado.")
        conexao.commit()
        print("Operação bem-sucedida.")
        return resultados
    except Error as e:
        print(f"Erro ao executar consulta: {e}")
    finally:
        cursor.close()
        conexao.close()

gerar_inner_join = lambda: "INNER JOIN VIDEOGAMES ON GAMES.id_console = VIDEOGAMES.id_console INNER JOIN COMPANY ON VIDEOGAMES.id_company = COMPANY.id_company"

gerar_select_query = lambda campos: f"SELECT {', '.join(campos)} FROM GAMES {gerar_inner_join()}"


# campos = ["GAMES.title", "VIDEOGAMES.name AS console_name", "COMPANY.name AS company_name"]
# consulta_sql = gerar_select_query(campos)
# resultados = executar_consulta(consulta_sql)
