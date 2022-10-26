from flask import Flask
from Controller.investidor import investidor_blueprint
from Controller.acao import acao_blueprint
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


app.register_blueprint(investidor_blueprint)
app.register_blueprint(acao_blueprint)


if __name__ == '__main__':
    app.run()