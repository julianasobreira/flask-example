##########################
# 
# DESAFIO
# E se a pessoa tentar cadastrar um aluno que já existe na lista?
# # Por exemplo, o usuário enviar um POST para /alunos com o seguinte json
# {
#   'nome': 'Ana Paula',
#   'módulo': 1
# }
# 
# Modifique o cadastrar_aluno para que o aluno não seja inserido no cadastro
# e retorne a mensagem "O aluno já existe no cadastro" junto com o status 400
# 
##########################

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

# Se você utilizar um método diferente de GET
# é necessário indicar aqui
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    # request.get_json é utilizado para pegar o JSON enviado para a API 
    # o silent=True indica que, caso não seja enviado nenhum JSON, novo_aluno será None
    novo_aluno = request.get_json(silent=True)

    # se os dados do aluno foram enviados, envia o status 400 indicando o problema
    if not novo_aluno:
      return 'É necessário enviar os dados do aluno', 400

    # caso contrário,
    # adiciona no cadastro e retorna para o usuário o status 201
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

if __name__ == '__main__':
    app.run(debug=True)
