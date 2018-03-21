import json
from flask import Flask, jsonify
app = Flask(__name__)

# Nossa base de dado
alunos = [{
  'nome': 'Ana Paula',
  'módulo': 1
},
{
  'nome': 'Carlos Souza',
  'módulo': 1
}]

@app.route('/')
def consultar_alunos():
    return jsonify(alunos)

if __name__ == '__main__':
    # Quando debug=True, o flask será atualizado a cada mudança no código
    # facilitando o desenvolvimento
    app.run(debug=True)