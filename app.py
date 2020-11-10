from sqlite3.dbapi2 import Connection, Cursor
from flask import Flask,g,jsonify
from flask.globals import request
from flask_cors import CORS
import database.databases 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def main():
    return "<h1>Desafio Stone</h1><p>Digite as seguintes rotas para consumir esta API:<p><ul><li><b>/Users: </b>Lista todos os usuarios no banco de dados</li><li><b>/users/find/<funcionario>: </b>Localiza um funcionario especifico digitando o seu nome</li><li><b>/users/add?id='<id>'&nome='<nome>'&idade='<idade>'&cargo='<cargo>': </b>Adiciona um novo registro ao banco de dados</li><li><b>/users/remove/<funcionario>: </b>Remove o funcionario do banco de dados.</li></ul>"

@app.route("/users", methods=['GET'])
def create_users():
    return jsonify(database.databases.todosRegistros())

@app.route("/users/find/<funcionario>", methods =['GET'])
def find_users(funcionario):
    return jsonify(database.databases.pesquisaBasica("nome",funcionario))

@app.route("/users/add" , methods = ['POST'])
def add_users():   
    return database.databases.adicionarFuncionario(request.args.get("nome"),request.args.get("idade"),ocupacion = request.args.get("cargo"))

@app.route("/users/remove/<funcionario>", methods=['DELETE'])
def remove_users(funcionario):
    return database.databases.removerFuncionario(funcionario)

if __name__ == "__MAIN__":
    app.run()


