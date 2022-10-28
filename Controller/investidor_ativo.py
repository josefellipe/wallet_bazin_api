from flask import Blueprint, request, jsonify
from Model.estrutura_db import InvestidorAtivo


investidor_ativo_blueprint = Blueprint('investidor_ativo_bluprint', __name__)

@investidor_ativo_blueprint.route('/adicionar_ativo', methods=['POST'])
def adicionar_ativo_carteira():
    #É esperado um json do tipo: {"id_investidor":"4", "ticket":"hglg11", "ativo_quantidade":"3", "valor_cota": "10"}
    operacao_ativo = request.json
    resposta = InvestidorAtivo.adicionar_acao_carteira(operacao_ativo)
    return jsonify(resposta)

@investidor_ativo_blueprint.route('/consultar_ativos_carteira', methods=['POST'])
def consultar_ativos_carteira():
    usuario = request.json
    ativos = InvestidorAtivo.consultar_ativos_carteira(usuario['id_investidor'])
    return jsonify(ativos)