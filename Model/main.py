import sqlite3
from Model.estrutura_db import Acao
from Model.import_fundamentus import pegar_acoes_fundamentus


'''Esta função atualiza as ações e dividendos do db
Parâmetros: Não tem parâmetros de entrada, ela busca os tickets na api do fundamentos e os dividendos por Web Scraping (bs4)
Saída: mensagem de ok'''
#Falta criar uma tabela auxiliar para apagar a tabela antiga e deixar apenas a mais atual
def atualizar_acoes_db():
    acoes = pegar_acoes_fundamentus()
    mensagem = Acao.adicionar_acao(acoes)
    return {'mensagem': f'{mensagem}'}