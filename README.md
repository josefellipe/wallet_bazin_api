# Wallet Bazin

Bem vindo a Wallet Bazin!

*Se desejar, você pode interagir com essa aplicação através do link: [Wallet Bazin](https://wallet-bazin-view.herokuapp.com/index.html)

Neste repositorio está a api que alimenta a wallet.
Esta API é responsável por verificar o login e senha do usuário e retornar os ativos que ele possui guardado em sua carteira.

Ela tambem possui um link que pode ser utilizado sem login, que é o seguinte:

[Lista de ações com seus dividendos](https://wallet-bazin-api.herokuapp.com/consultar)
Esse link retorna uma array com os papeis e seus detalhes na seguinte estrutura:

[(id-papel, ticket-papel, nome-da-empresa, dividendo2022, dividendo2021, dividendo2020, dividendo2019, dividendo2018)]

Essa API possui o cadastro dos usuário, ações da bolsa rankeadas conforme o didend e também a relação de ativos que o usuário escolheu.

O banco de dados foi construido no sqlite e possui 4 tabelas, que são as seguintes:
1 - Investidor (dados como nome, senha, login)
2 - Ação (dados como ticket, nome da empresa, cotação, dividendos)
3 - Fii (mesmas informações das ações)
4 - Tabela relacional para ligar os ativos e suas quantidades aos investidores.