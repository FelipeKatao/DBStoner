from sqlite3.dbapi2 import Connection, Cursor
from flask import Flask,g,jsonify
from flask.globals import request
import database.databases 

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World"

@app.route("/users", methods=['GET'])
def create_users():
    return jsonify(database.databases.todosRegistros())

@app.route("/users/find/<funcionario>", methods =['GET'])
def find_users(funcionario):
    return jsonify(database.databases.pesquisaBasica("nome",funcionario))

@app.route("/users/add" , methods = ['POST'])
def add_users():   
    return database.databases.adicionarFuncionario(request.args.get("id"),request.args.get("nome"),request.args.get("idade"),ocupacion = request.args.get("cargo"))

@app.route("/users/remove/<funcionario>", methods=['DELETE'])
def remove_users(funcionario):
    return database.databases.removerFuncionario(funcionario)

if __name__ == "__MAIN__":
    app.run()


