from flask import Flask, jsonify, request
from flask_restx import Api, Resource

from cadastro_autor import (alterar_autor_bd, consultar_autor_por_id_bd,
                            deletar_autor_bd, inserir_autor_bd, listar_autores)
from cadastro_livro import (alterar, consultar, consultar_por_id, deletar,
                            inserir)
from cadastro_usuario import (alterar_usuario_bd, consultar_usuario_por_id_bd,
                              deletar_usuario_bd, inserir_usuario_bd,
                              listar_usuarios, verificar_login)
from conexao import conecta_db

app = Flask(__name__)
api = Api(app, doc='/swagger/')

@app.route("/livros/<int:id>", methods=["GET"])
def get_livro(id):
   conexao = conecta_db()
   livros = consultar_por_id(conexao,id)
   return jsonify(livros)

@app.route("/livros", methods=["POST"])
def inserir_livro():
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    inserir(conexao,nome)
    return jsonify(data)

@app.route("/livros/<int:id>", methods=["PUT"])
def alterar_livro(id):
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    alterar(conexao,int(id),nome)
    return jsonify(data)


@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    conexao = conecta_db()
    deletar(conexao,id)
    return jsonify({"message": "Livro deletado com sucesso" })


@app.route("/livros", methods=["GET"])
def listar_todos():
    conexao = conecta_db()
    livros = consultar(conexao)
    return jsonify(livros)

@app.route("/autores", methods=["GET"])
def listar_todos_autores():
    conexao = conecta_db()
    autores = listar_autores(conexao)
    return jsonify(autores)


@app.route("/autores", methods=["POST"])
def inserir_autor():
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    inserir_autor_bd(conexao,nome)
    return jsonify(data)

@app.route("/autores/<int:id>", methods=["PUT"])
def update_autor(id):
    conexao = conecta_db()
    data = request.get_json()
    nome = data["nome"]
    alterar_autor_bd(conexao,int(id),nome)
    return jsonify(data)


@app.route("/autores/<int:id>", methods=["DELETE"])
def excluir_autor(id):
    conexao = conecta_db()
    deletar_autor_bd(conexao,id)
    return jsonify({"message": "Autor deletado com sucesso" })


@app.route("/autores/<int:id>", methods=["GET"])
def consultar_autor_por_id(id):
    conexao = conecta_db()
    autor = consultar_autor_por_id_bd(conexao,id)
    return jsonify(autor)


@app.route("/usuarios", methods=["GET"])
def listar_todos_usuarios():
    conexao = conecta_db()
    usuarios = listar_usuarios(conexao)
    return jsonify(usuarios)


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    inserir_usuario_bd(conexao,login,senha)
    return jsonify(data)

@app.route("/usuarios/<int:id>", methods=["PUT"])
def update_usuario(id):
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    alterar_usuario_bd(conexao,int(id),login,senha)
    return jsonify(data)


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):
    conexao = conecta_db()
    deletar_usuario_bd(conexao,id)
    return jsonify({"message": "Usuário deletado com sucesso" })


@app.route("/usuarios/<int:id>", methods=["GET"])
def consultar_usuario_por_id(id):
    conexao = conecta_db()
    autor = consultar_usuario_por_id_bd(conexao,id)
    return jsonify(autor)


@app.route("/autenticar", methods=["POST"])
def autenticar():
    conexao = conecta_db()
    data = request.get_json()
    login = data["login"]
    senha = data["senha"]
    resultado = verificar_login(conexao,login,senha)
    return jsonify(resultado)





if __name__ == "__main__":
    app.run(debug=True)