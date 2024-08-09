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



def inserir_autor_bd(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute("insert into autor (nome)  values ('"+ nome +  "')")
    conexao.commit()

def alterar_autor_bd(conexao, id, nome):
    cursor = conexao.cursor()
    sql_update = "update autor set nome = %s where id = %s"
    dados   = (nome, id)
    cursor.execute(sql_update,dados)
    conexao.commit()

def deletar_autor_bd(conexao, id):
    cursor = conexao.cursor()
    sql_delete = "delete from  autor where id =  %s"
    cursor.execute(sql_delete,[id])
    conexao.commit()

def consultar_autor_por_id_bd(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from autor where id = %s",[id])
    registro = cursor.fetchone()
    item = {
        "id": registro[0],
        "nome": registro[1]
    }
    return item