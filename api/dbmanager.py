import MySQLdb as mdb


class DBmanager:
    def __init__(self):
        self.dsn = {
            "host": "localhost",
            "user": "raspi",
            "passwd": "pwd",
            "db": "prueba",
        }
        self.connection = mdb.connect(**self.dsn)

    def get_temp(self):
        slqQuery = "SELECT temp, time FROM temp_y_humedad;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        temperature = cursor.fetchall()
        cursor.close()

        return temperature

    def insert_temp(self, temp):
        cur = self.connection.cursor()
        cur.execute("""INSERT INTO temperatura(temperatura) VALUES (%s);""", (temp,))
        self.connection.commit()
        cur.close()

    def get_humedad(self):
        slqQuery = "SELECT time, hum FROM humedad;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        humedad = cursor.fetchall()
        cursor.close()

        return humedad

    def insert_humedad(self, hum):
        cur = self.connection.cursor()
        cur.execute("""INSERT INTO humedad(hum) VALUES (%s);""", (hum,))
        self.connection.commit()
        cur.close()

    def get_distancia(self):
        slqQuery = "SELECT time, hum FROM humedad;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        distancia = cursor.fetchall()
        cursor.close()

        return distancia

    def insert_distancia(self, dist):
        cur = self.connection.cursor()
        cur.execute("""INSERT INTO distancia(dist) VALUES (%s);""", (dist,))
        self.connection.commit()
        cur.close()

    def get_lumens(self):
        slqQuery = "SELECT time, lum FROM luminosidad;"
        cursor = self.connection.cursor()
        cursor.execute(slqQuery)
        luminosidad = cursor.fetchall()
        cursor.close()

        return luminosidad

    def insert_lumens(self, lum):
        cur = self.connection.cursor()
        cur.execute("""INSERT INTO luminosidad(lum) VALUES (%s);""", (lum,))
        self.connection.commit()
        cur.close()
