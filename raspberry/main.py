from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from seeed_dht import DHT
from emailing import Email
import RPi.GPIO as GPIO
import time
import requests

email = Email()

url = "http://192.168.1.130:4000/"

url_conf = url + "conf"

raspi_sensors = {
    "temperatura" : 1,
    "distancia" : 1,
    "humedad" : 1,
    "luz" : 1,
    "movimiento" : 1,
    "conf" : 0,
    "lastluminosidad" : 0,
    "lasttemperatura" : 0,
    "lastdistancia" : 0,
    "lastmovimiento" : 0,
    "lasthumedad" : 0
}

raspi_activator = {'raspberry' :{
    "bombilla" : 0,
    "sonido" : 0,
    "servo" : 0
}
}

url_dict = {
    key: url + key for key in raspi_sensors.keys()
}

GPIO.setmode(GPIO.BCM)

sensor = GroveUltrasonicRanger(16)
sensor_luz = GroveLightSensor(0)
sensorHT = DHT('11', 5)

# Bombilla
GPIO.setup(18, GPIO.OUT)
# Servo
GPIO.setup(26, GPIO.OUT)
p = GPIO.PWM(26, 50)
p.start(0)
servo_control = False
# Movimiento
GPIO.setup(22, GPIO.IN)
#Sonido 
GPIO.setup(24, GPIO.OUT)

while True:
    # Temperatura y Humedad
    humi, temp = sensorHT.read()
    print('temperature {}C, humidity {}%'.format(temp, humi))
    data = {"temperatura": temp}
    r = requests.post(url_dict["temperatura"], data)

    # print(r.content)
    data = {"humedad": humi}
    r = requests.post(url_dict["humedad"], data)

    # Distancia
    distance = sensor.get_distance()
    print('{} cm'.format(distance))
    data = {"distancia": distance}
    r = requests.post(url_dict["distancia"], data)

    # Luz
    light = sensor_luz.light
    print('light value {}'.format(light))
    data = {"luz": light}
    r = requests.post(url_dict["luz"], data)

    #movimiento
    move = GPIO.input(22)
    print('move value {}'.format(move))
    data = {"move": move}
    r = requests.post(url_dict["movimiento"], data)
    
    #controller
    time.sleep(0.5)
    c = requests.get(url_conf)
    print(c.json())
    bombilla = c.json()['raspberry']['bombilla']
    servo = c.json()['raspberry']['servo']
    print(servo)
    if servo == False:
        servo_control = False
        print('servo control {}'.format(servo_control))
    sonido = c.json()['raspberry']['sonido']

    #Sonido
    GPIO.output(24, sonido)

    #Luz
    GPIO.output(18, bombilla)

    #Last Luz
    l = requests.get(url_dict["lastluminosidad"])
    print(l.json()['lastlum'][0][0])
    if l.json()['lastlum'][0][0] < 150:
        GPIO.output(18, True)
    else:
        GPIO.output(18, bombilla)
    
    #Last Temp
    t = requests.get(url_dict["lasttemperatura"])
    if t.json()['lasttemp'][0][0] > 15:
        print("ultima temp {}".format(t.json()['lasttemp'][0][0]))
        email.send_email("diego.miquelez@opendeusto.es", "Fuego",
         "El contenedor tiene más de {}º".format(t.json()['lasttemp'][0][0]))

    #Last Hum
    h = requests.get(url_dict["lasthumedad"])
    if h.json()['lasthum'][0][0] > 20:
        email.send_email("diego.miquelez@opendeusto.es", "Vertido",
         "Posible vertido, humedad:{}".format(h.json()['lasthum'][0][0]))

    #Last dist
    d = requests.get(url_dict["lastdistancia"])
    print(d.json())
    if d.json()['lastdist'][0][0] < 20:
        email.send_email("diego.miquelez@opendeusto.es", "Basura llena",
         "Al contenedor le quedan {} cm de espacio".format(d.json()['lastdist'][0][0]))

    #Last move
    m = requests.get(url_dict["lastmovimiento"])
    if m.json()['lastmove'][0][0] == False:
        servo_control = False
        print('servo control {}'.format(servo_control))
    
    if (servo or m.json()['lastmove'][0][0]) and servo_control == False:
        print(servo_control)
        try:
            p.start(0)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)

        except KeyboardInterrupt:
            p.stop()
            GPIO.cleanup()

        servo_control = True
    # move
    time.sleep(3)