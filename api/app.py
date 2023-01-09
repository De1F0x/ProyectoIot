from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import render_template
import time
from dbmanager import DBmanager

db = DBmanager()

raspi_activator = {
    "bombilla" : 0,
    "sonido" : 0,
    "servo" : 0
}

app = Flask(__name__)
CORS(app)

@app.route('/index')
def get_index():
    return "<p> Hola, Mikel </p>"

# @app.route('/conf', methods = ["GET"])
# def get_conf():
#     print("hola")
#     return jsonify(raspi_activator)

# @app.route('/conf', methods = ["POST"])
# def post_conf():
#     data = request.json
#     print(data)
#     raspi_activator = data
#     return jsonify(raspi_activator)

@app.route('/conf', methods = ["GET","POST"])
def get_conf():
    global raspi_activator
    if request.method == "GET":
        app.logger.info("Petición GET recibida")
        return jsonify(raspi_activator)
    elif request.method == "POST":
        app.logger.info("Petición POST recibida")
        data = request.json
        app.logger.info(data)
        raspi_activator = data
        return jsonify(raspi_activator)

# Distancia POST y GET
@app.route('/distancia', methods = ["POST"])
def post_distancia():
    data = request.form["distancia"]
    db.insert_distancia(data)
    return jsonify(data)

@app.route('/distancia', methods = ["GET"])
def get_distancia():
    data = {
        "distancia" : db.get_distancia()
    }
    return jsonify(data)

# Temperatura POST y GET
@app.route('/temperatura', methods = ["POST"])
def post_temperature():
    data = request.form["temperatura"]
    db.insert_temp(data)
    # raspi_activator["bombilla"] = 1 if data > 15 else 0
    return jsonify(data)

@app.route('/temperatura', methods = ["GET"])
def get_temperature():
    data = {
        "temperatura" : db.get_temp()
    }
    return jsonify(data)

# Humedad POST y GET
@app.route('/humedad', methods = ["POST"])
def post_humedad():
    data = request.form["humedad"]
    db.insert_humedad(data)
    return jsonify(data)

@app.route('/humedad', methods = ["GET"])
def get_humedad():
    data = {
        "humedad" : db.get_humedad()
    }
    return jsonify(data)

# Lumens POST y GET
@app.route('/luz', methods = ["POST"])
def post_lumens():
    data = request.form["luz"]
    db.insert_lumens(data)
    return jsonify(data)

@app.route('/luz', methods = ["GET"])
def get_lumens():
    data = {
        "luz" : db.get_lumens()
    }
    return jsonify(data)

# Movimiento POST y GET
@app.route('/movimiento', methods = ["POST"])
def post_movimiento():
    data = request.form["move"]
    db.insert_movement(data)
    return jsonify(data)

@app.route('/movimiento', methods = ["GET"])
def get_movimiento():
    data = {
        "movimiento" : db.get_movements()
    }
    return jsonify(data)

# Movimiento POST y GET last values
@app.route('/lastmovimiento', methods = ["GET"])
def get_lastmovimiento():
    data = {
        "lastmovimiento" : db.get_lastmovements()
    }
    return jsonify(data)

@app.route('/lastdistancia', methods = ["GET"])
def get_lastdistancia():
    data = {
        "distancia" : db.get_lastdistancia()
    }
    return jsonify(data)

@app.route('/lastluminosidad', methods = ["GET"])
def get_lastluminosidad():
    data = {
        "movimiento" : db.get_lastluminosidad()
    }
    return jsonify(data)

@app.route('/lasttemperatura', methods = ["GET"])
def get_temperatura():
    data = {
        "movimiento" : db.get_lasttemperatura()
    }
    return jsonify(data)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=4000, debug=True)
