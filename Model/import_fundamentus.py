from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import fundamentus
from Model.estrutura_db import Acao

'''Esta função busca no fundamentus os detalhes de cada papel listado
Parâmetro: não tem parâmetro de entrada
Saída: entrega um array de objetos da classe Acao'''
def pegar_acoes_fundamentus():
    list_papel = fundamentus.list_papel_all()
    acoes = []
    for papel in list_papel:
        try:
            acao_aux = fundamentus.get_detalhes_papel(f'{papel}')
            dividend = buscar_dividendos_por_ano(papel)
            div_0 = '0'
            div_1 = '0'
            div_2 = '0'
            div_3 = '0'
            div_4 = '0'
            cotacao = float(acao_aux['Cotacao'][0])
            fator = 100/cotacao
            for dividendo in dividend:
                dividendo['valor'] = dividendo['valor'].replace(',','.')
                if dividendo['ano'] == '2022':
                    div_0 = float(dividendo['valor'])*fator
                if dividendo['ano'] == '2021':
                    div_1 = float(dividendo['valor'])*fator
                if dividendo['ano'] == '2020':
                    div_2 = float(dividendo['valor'])*fator
                if dividendo['ano'] == '2019':
                    div_3 = float(dividendo['valor'])*fator
                if dividendo['ano'] == '2018':
                    div_4 = float(dividendo['valor'])*fator
            tick = acao_aux['Papel'][0]
            nome = acao_aux['Empresa'][0]   
            acao = Acao(tick, nome, cotacao, f'{div_0:.2f}', f'{div_1:.2f}', f'{div_2:.2f}', f'{div_3:.2f}', f'{div_4:.2f}')
            acoes.append(acao)
            print(acao.ticket)
        except:
            resposta = ''
    return acoes



'''Esta função busca no fundamentus os dividendos pagos por ação
Parâmetro: ticket
Return: array de dict do tipo {'ano': '1999', 'valor':'1,25'}'''
def buscar_dividendos_por_ano(papel):

    req = Request(
        url=f'https://www.fundamentus.com.br/proventos.php?papel={papel}&tipo=2',
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    page = urlopen(req).read()

    soup = BeautifulSoup(page, 'html5lib')

    tabela = soup.find("table", id="resultado-anual")

    aux = []
    for item in tabela:
        text_aux = item.text
        arr_aux = text_aux.split('\n')
        aux.append(arr_aux)

    n = 1
    while n != 0:
        n = 0
        for item in aux:
            for sub in item:
                if sub == '':
                    n +=1
                    item.remove('')
                if sub == ' ':
                    n +=1
                    item.remove(' ')
                if sub == '  ':
                    n +=1
                    item.remove('  ')

    table = []
    for item in aux:
        if item != []:
            table.append(item)

    dividendo = {
        'ano':'',
        'valor':''
    }
    aux = table[1]


    aux2 = []
    arr_dividendo = []
    n = 0
    while n < len(aux):
        try:
            dividendo['ano'] = aux[n]
            dividendo['valor'] = aux[n+1]
            aux2 = dividendo.copy()
            arr_dividendo.append(aux2)
            n += 2
        except:
            n = len(aux)
            arr_dividendo = ['Error']

    return arr_dividendo


