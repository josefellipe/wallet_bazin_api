from flask import Flask
from Controller.investidor import investidor_blueprint
from Controller.acao import acao_blueprint
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)


app.register_blueprint(investidor_blueprint)
app.register_blueprint(acao_blueprint)


def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()