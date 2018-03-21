import json
from flask import Flask, jsonify, request
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

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    novo_aluno = request.get_json(silent=True)

    if not novo_aluno:
      return 'É necessário enviar os dados do aluno', 400

    for aluno in alunos:
      if aluno['nome'] == novo_aluno['nome']:
        return '"O aluno já existe no cadastro', 400

    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

@app.route('/alunos/<string:nome>', methods=['DELETE'])
def remover_aluno(nome):
    for index, aluno in enumerate(alunos):
      if aluno['nome'] == nome:
        del alunos[index]
        return 'O aluno foi removido cadastro', 201
    
    return 'Aluno não encontrado', 409

if __name__ == '__main__':
    app.run(debug=True)
