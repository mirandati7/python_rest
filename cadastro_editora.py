from conexao import conecta_db


def inserir_editora_bd(conexao, nome):
    cursor = conexao.cursor()
    cursor.execute("insert into editora (nome)  values ('"+ nome +  "')")
    conexao.commit()
