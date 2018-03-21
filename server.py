import json
from flask import Flask, jsonify
app = Flask(__name__)

alunos = [{
  'nome': 'Ana Paula',
  'módulo': 1
},
{
  'nome': 'Carlos Souza',
  'módulo': 1
}]

@app.route('/alunos')
def consultar_alunos():
    return jsonify(alunos)

@app.route('/alunos/<string:nome>')
def consultar_aluno(nome):
    for aluno in alunos:
      if aluno['nome'] == nome:
        return jsonify(aluno)

    return 'Aluno não encontrado', 404

if __name__ == '__main__':
    app.run(debug=True)