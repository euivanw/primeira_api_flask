''' Importações '''
from flask import Flask, jsonify, make_response, request
from db import carros

app = Flask(__name__)


@app.route("/carros", methods=['GET'])
def get_carros():
    ''' Retorna a lista de carros cadastrada. '''
    return make_response(jsonify(carros))


@app.route('/carros', methods=['POST'])
def create_carro():
    ''' Insere um carro na lista. '''
    carro = request.json
    carros.append(carro)
    return carro


if __name__ == '__main__':
    app.run()
