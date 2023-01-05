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


@app.route("/distancia", methods=["GET"])
def get_distancia():

    return jsonify(nabo)


@app.route("/distancia", methods=["POST"])
def led2on():
    data = request.json
    return jsonify(data)


@app.route("/temperatura", methods=["POST"])
def post_temperature():
    data = request.form["temperatura"]
    db.insert_temp(data)
    raspi_activator["bombilla"] = 1 if data > 15 else 0
    return jsonify(data)


@app.route("/temperatura", methods=["GET"])
def get_temperature():
    data = {"temperatura": db.get_temp()}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
