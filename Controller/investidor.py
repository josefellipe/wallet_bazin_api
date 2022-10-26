from flask import Blueprint, request, jsonify
from Model.estrutura_db import Investidor


investidor_blueprint = Blueprint('investidor_bluprint', __name__)

@investidor_blueprint.route('/login', methods=['POST'])
def login():
    #É esperado um json do tipo: {"login":"fulano", "senha":"9999"}
    usuario = request.json
    mensagem = Investidor.consultar_investidor(usuario)
    return jsonify(mensagem)

@investidor_blueprint.route('/registrar_novo_investidor', methods=['POST'])
def registrar():
    #É esperado um json do tipo: {"nome": "José", "user_name": "zezinho", "senha": "9999"}
    novo_registro = request.json
    investidor = Investidor(novo_registro['user_name'],novo_registro['senha'],novo_registro['nome'])
    mensagem = Investidor.adicionar_investidor(investidor)
    print(novo_registro)
    return jsonify(mensagem)