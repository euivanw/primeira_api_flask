""" Importações """
from flask import Flask
from db import carros

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_carros() -> list:
    """ Retorna a lista de carros cadastrada. """
    return carros


if __name__ == "__main__":
    app.run(port=8080)
