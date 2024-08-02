from conexao import conecta_db


def listar_autores(conexao):
    autores = []
    cursor = conexao.cursor()
    cursor.execute("select id,nome from autor")
    registros = cursor.fetchall()
 
    for registro in registros:
        item = {
            "id": registro[0],
            "nome": registro[1]
        }
        autores.append(item)
    return autores
