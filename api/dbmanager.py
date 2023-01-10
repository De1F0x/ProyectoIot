import mysql.connector

class DBmanager:
    def __init__(self):
        self.dsn = {
            "host": "db",
            "user": "raspi",
            "passwd": "pwd",
            "db": "iot"
        }
        self.connection = mysql.connector.connect(**self.dsn)

    # temperatura
    def get_temp(self):
        slqQuery = "SELECT temp, time FROM temperatura;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        temperature = cursor.fetchall()
        cursor.close()

        return temperature

    def insert_temp(self, temp):
        cur = self.connection.cursor()
        cur.execute('''INSERT INTO temperatura(temp) VALUES (%s);''', (temp, ))
        self.connection.commit()
        cur.close()

    #humedad
    def get_humedad(self):
        slqQuery = "SELECT time, hum FROM humedad;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        humedad = cursor.fetchall()
        cursor.close()

        return humedad

    def insert_humedad(self, hum):
        cur = self.connection.cursor()
        cur.execute('''INSERT INTO humedad(hum) VALUES (%s);''', (hum, ))
        self.connection.commit()
        cur.close()

    # distancia
    def get_distancia(self):
        slqQuery = "SELECT time, hum FROM humedad;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        distancia = cursor.fetchall()
        cursor.close()

        return distancia

    def insert_distancia(self, dist):
        cur = self.connection.cursor()
        cur.execute('''INSERT INTO distancia(dist) VALUES (%s);''', (dist, ))
        self.connection.commit()
        cur.close()

    # lumens 
    def get_lumens(self):
        slqQuery = "SELECT time, lum FROM luminosidad;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        luminosidad = cursor.fetchall()
        cursor.close()

        return luminosidad

    def insert_lumens(self, lum):
        cur = self.connection.cursor()
        cur.execute('''INSERT INTO luminosidad(lum) VALUES (%s);''', (lum, ))
        self.connection.commit()
        cur.close()

    # movement
    def get_movements(self):
        slqQuery = "SELECT time, move FROM movimiento;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        move = cursor.fetchall()
        cursor.close()

        return move

    def insert_movement(self, move):
        cur = self.connection.cursor()
        cur.execute('''INSERT INTO movimiento(move) VALUES (%s);''', (move, ))
        self.connection.commit()
        cur.close()

    # last
    def get_lastmovements(self):
        slqQuery = "SELECT move FROM movimiento ORDER BY time DESC LIMIT 1;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        move = cursor.fetchall()
        cursor.close()

        return move

    def get_lastdistancia(self):
        slqQuery = "SELECT dist FROM distancia ORDER BY time DESC LIMIT 1;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        dist = cursor.fetchall()
        cursor.close()

        return dist

    def get_lastluminosidad(self):
        slqQuery = "SELECT lum FROM luminosidad ORDER BY time DESC LIMIT 1;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        lum = cursor.fetchall()
        cursor.close()

        return lum
    
    def get_lasttemperatura(self):
        slqQuery = "SELECT temp FROM temperatura ORDER BY time DESC LIMIT 1;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        temp = cursor.fetchall()
        cursor.close()

        return temp
    
    def get_lasthumedad(self):
        slqQuery = "SELECT hum FROM humedad ORDER BY time DESC LIMIT 1;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        hum = cursor.fetchall()
        cursor.close()

        return hum