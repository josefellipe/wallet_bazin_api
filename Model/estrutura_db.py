import sqlite3

#Ação
#FII
#Investidor

####################################             Auxiliar           ####################################
'''Esta função transforma o array de tupla que vem do db em um array de array
Parâmetro: um array de tupla
Saída: um array de array'''
def transformar_tupla_para_array(tupla_acoes):
    array_acoes = []
    for acao in tupla_acoes:
        array_acao = []
        for item in acao:
            array_acao.append(item)
        array_acoes.append(array_acao)
    return array_acoes


####################################               Ação              ####################################
"""Estrutura e comandos para tabela acao"""


class Acao:
    'As colunas da tabela seguem a nomenclatura da classe'

    def __init__(self,  ticket, nome_empresa, cotacao, dividend_yield_ano, dividend_yield_ano_1, dividend_yield_ano_2, dividend_yield_ano_3, dividend_yield_ano_4, bazin='', id_acao=''):
        self.ticket = ticket
        self.nome_empresa = nome_empresa
        self.cotacao = cotacao
        self.dividend_yield_ano = dividend_yield_ano
        self.dividend_yield_ano_1 = dividend_yield_ano_1
        self.dividend_yield_ano_2 = dividend_yield_ano_2
        self.dividend_yield_ano_3 = dividend_yield_ano_3
        self.dividend_yield_ano_4 = dividend_yield_ano_4
        self.bazin = bazin
        self.id_acao = id_acao

    '''Esta função faz uma consulta no banco de dados.
    Retorno: array com os dados da tabela, cada linha e um array'''
    def consultar_acao():
        conexao = sqlite3.connect('app_bazin.db')
        cursor = conexao.cursor()
        comando = f'SELECT * FROM acao ORDER BY dividend_yield_ano DESC'
        cursor.execute(comando)
        historico = cursor.fetchall()
        cursor.close()
        conexao.close()
        acoes = transformar_tupla_para_array(historico)
        return acoes

    '''Esta função busca as informações de uma ação específica do db
    Parâmetros: o ticket da ação
    Saida: array com cada termo igual a classe Acao'''
    def consultar_acao_especifica(ticket):
        conexao = sqlite3.connect('app_bazin.db')
        cursor = conexao.cursor()
        comando = f'SELECT * FROM acao WHERE ticket = "{ticket}"'
        cursor.execute(comando)
        acao = cursor.fetchall()
        cursor.close()
        conexao.close()
        acao_array = transformar_tupla_para_array(acao)
        return acao_array

    '''Esta funcção adiciona 1 ou mais acoes ao banco de dados
    Parâmetro: array com termos sendo o objeto da classe Acao
    Retorno: OK'''
    def adicionar_acao(acoes):
        conexao = sqlite3.connect('app_bazin.db')
        cursor = conexao.cursor()
        values = ''
        for acao in acoes:
            value = f"""('{acao.ticket}', '{acao.nome_empresa}', '{acao.cotacao}', '{acao.dividend_yield_ano}', '{acao.dividend_yield_ano_1}', '{acao.dividend_yield_ano_2}', '{acao.dividend_yield_ano_3}', '{acao.dividend_yield_ano_4}', '0')"""
            if values == '':
                values = value
            else:
                values = values + ',' + value
        comando = f"""
                    INSERT INTO acao (ticket, nome_empresa, cotacao, dividend_yield_ano, dividend_yield_ano_1, dividend_yield_ano_2, dividend_yield_ano_3, dividend_yield_ano_4, bazin)
                    VALUES {values}
                    """
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
        return 'OK'




        

####################################             Investidor             ####################################             
'''Estrutura e comandos para tabela investidor'''


class Investidor:
    'As colunas da tabela seguem a nomenclatura da classe'

    def __init__(self, login, senha, nome, id_investidor=''):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.id_investidor = id_investidor


    '''Esta função retorna um investidor específico
    Parâmetro: id_investidor
    Retorno: json com as chaves iguais as caracteristicas do objeto dessa classe'''
    def consultar_investidor(usuario):
        conexao = sqlite3.connect('app_bazin.db')
        cursor = conexao.cursor()
        comando = f"SELECT * FROM investidor WHERE login = '{usuario['login']}' AND senha = '{usuario['senha']}'"
        cursor.execute(comando)
        investidor_db = cursor.fetchall()
        cursor.close()
        conexao.close()
        try:
            investidor = Investidor(
                investidor_db[0][1], investidor_db[0][2], investidor_db[0][3], investidor_db[0][0])
            return {
                'login': investidor.login,
                'senha': investidor.senha,
                'nome': investidor.nome
            }
        except:
            return 'Login ou senha Inválido'


    """Esta funcção adiciona um investidor ao banco de dados
    Parâmetros: um objeto dessa classe (login, senha, nome)
    Return: Mensagem dizendo que foi adicionado ou não"""
    def adicionar_investidor(investidor):
        conexao = sqlite3.connect('app_bazin.db')
        cursor = conexao.cursor()
        value = f"""('{investidor.login}', '{investidor.senha}', '{investidor.nome}')"""
        comando = f"""
                    INSERT INTO investidor (login, senha, nome)
                    VALUES {value}
                    """
        try:
            cursor.execute(comando)
            conexao.commit()
            mensagem = {'mensagem' : 'Usuário criado com sucesso'}
        except:
            mensagem = {'mensagem' : 'Usuário não foi criado'}
        cursor.close()
        conexao.close()
        return mensagem

    '''Esta função adiciona à carteira (tbl investidor_ativo) uma acao
    Parâmetros: é esperado um dic com as chaves: id_investidor, ticket, quantidade, valor_cota
    Return: mensagem de OK'''
    def adicionar_acao_carteira(dados):
        ticket = dados['ticket']
        quantidade = dados['quantidade']
        acao_detalhe = Acao.consultar_acao_especifica(ticket)
        conexao = sqlite3.connect('app_bazin.db')
        cursor = conexao.cursor()
        comando = f"""INSERT INTO investidor (login, senha, nome)
                    VALUES ()"""
        mensagem = 'ok'
        return {'mensagem': mensagem}


