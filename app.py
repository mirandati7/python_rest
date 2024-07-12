from flask import Flask, jsonify, request

app = Flask(__name__)

livros = []

@app.route("/livros/<int:id>", methods=["GET"])
def get_livro(id):
    print(" ID Livro > " + str(id))
    return jsonify("{ 'nome':  'Livro Python 21 dias' }")

@app.route("/livros", methods=["POST"])
def create_livro():
    data = request.get_json()
    print(data)
    livros.append(data)
    return jsonify(data)

@app.route("/livros/<int:id>", methods=["PUT"])
def alterar_livro(id):
    data = request.get_json()
    print("ID " + str(id))
    print(data)
    return jsonify(data)


@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    print ("ID " + str(id))
    return jsonify({"message": "Livro deletado com sucesso" })


@app.route("/livros", methods=["GET"])
def listar_todos():
    return jsonify(livros)


if __name__ == "__main__":
    app.run(debug=True)