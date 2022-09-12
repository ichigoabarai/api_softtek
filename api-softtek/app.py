from flask import Flask, request, jsonify
from api_softtek import Api_Softtek


app = Flask(__name__)


@app.route("/OrderStatus", methods=["POST"])
def orderStatus():
    datos = request.json["datos"]
    resultado = Api_Softtek().orderStat(datos)
    return jsonify(resultado)


@app.route("/Seasons", methods=["POST"])
def seasons():
    datos = request.json["datos"]
    resultado = Api_Softtek().seasons(datos)
    return jsonify(resultado)


@app.route("/Weather", methods=["POST"])
def weather():
    datos = request.json["datos"]
    resultado = Api_Softtek().weather(datos)
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
# http://127.0.0.1:5000/OrderStatus
# http://127.0.0.1:5000/Seasons
# http://127.0.0.1:5000/Weather
