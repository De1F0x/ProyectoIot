from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from seeed_dht import DHT
import RPi.GPIO as GPIO
import time
import requests

url = "http://localhost/"

raspi_sensors = {"temperatura": 1, "distancia": 1, "humedad": 1, "luz": 1}

url_dict = {key: url + key for key in raspi_sensors.keys()}

GPIO.setup(22, GPIO.IN)
sensor = GroveUltrasonicRanger(16)
sensor_luz = GroveLightSensor(0)
sensorHT = DHT("11", 5)

while True:
    # Temperatura y Humedad
    humi, temp = sensorHT.read()
    print("temperature {}C, humidity {}%".format(temp, humi))
    data = {"temperatura": temp}
    r = requests.post(url_dict["temperatura"], data)
    data = {"humedad": humi}
    r = requests.post(url_dict["humedad"], data)

    # Distancia
    distance = sensor.get_distance()
    print("{} cm".format(distance))
    data = {"distancia": distance}
    r = requests.post(url_dict["distancia"], data)

    # Luz
    light = sensor_luz.light
    print("light value {}".format(light))
    data = {"luz": light}
    r = requests.post(url_dict["luz"], data)

    time.sleep(3)
