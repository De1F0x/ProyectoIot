from flask import Flask, request, jsonify
from flask import render_template
from grove.grove_light_sensor_v1_2 import GroveLightSensor
import RPi.GPIO as GPIO
import time
from dbmanager import DBmanager

db = DBmanager()
app = Flask(__name__)

raspi_activator = {"bombilla": 0, "sonido": 0, "servo": 0}


@app.route("/conf", methods=["GET"])
def get_conf():
    return jsonify(raspi_activator)


@app.route("/conf", methods=["POST"])
def post_conf():
    return jsonify(raspi_activator)


# Distancia POST y GET
@app.route("/distancia", methods=["POST"])
def post_distancia():
    data = request.form["distancia"]
    db.insert_distancia(data)
    return jsonify(data)


@app.route("/distancia", methods=["GET"])
def get_distancia():
    data = {"distancia": db.get_distancia()}
    return jsonify(data)


# Temperatura POST y GET
@app.route("/temperatura", methods=["POST"])
def post_temperature():
    print(request.json)
    data = request.form["temperatura"]
    db.insert_temp(data)
    # raspi_activator["bombilla"] = 1 if data > 15 else 0
    return jsonify(data)


@app.route("/temperatura", methods=["GET"])
def get_temperature():
    data = {"temperatura": db.get_temp()}
    return jsonify(data)


# Humedad POST y GET
@app.route("/humedad", methods=["POST"])
def post_humedad():
    data = request.form["humedad"]
    db.insert_humedad(data)
    return jsonify(data)


@app.route("/humedad", methods=["GET"])
def get_humedad():
    data = {"humedad": db.get_humedad()}
    return jsonify(data)


# Lumens POST y GET
@app.route("/lumens", methods=["POST"])
def post_lumens():
    data = request.form["luz"]
    db.insert_lumens(data)
    return jsonify(data)


@app.route("/lumens", methods=["GET"])
def get_lumens():
    data = {"luz": db.get_lumens()}
    return jsonify(data)


# Movimiento POST y GET
@app.route("/movimiento", methods=["POST"])
def post_movimiento():
    data = request.form["luz"]
    db.insert_movement(data)
    return jsonify(data)


@app.route("/movimiento", methods=["GET"])
def get_movimiento():
    data = {"movimiento": db.get_movements()}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
