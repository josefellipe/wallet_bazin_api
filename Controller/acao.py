from flask import Blueprint, request, jsonify
from Model.main import atualizar_acoes_db
from Model.estrutura_db import Acao


acao_blueprint = Blueprint('acao_bluprint', __name__)

@acao_blueprint.route('/atualizar_acoes_db', methods=['GET'])
def adicionar_acao():
    mensagem = atualizar_acoes_db()
    return jsonify(mensagem)

@acao_blueprint.route('/consultar', methods=['GET'])
def consultar_acoes():
    acoes = Acao.consultar_acao()
    return jsonify(acoes)