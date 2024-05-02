""" Importações """
from flask import Flask, jsonify, make_response
from db import carros

app = Flask(__name__)


@app.route("/carros", methods=['GET'])
def get_carros() -> list:
    """ Retorna a lista de carros cadastrada. """
    return make_response(jsonify(carros))


if __name__ == "__main__":
    app.run()
