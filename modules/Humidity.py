from modules.SensorDHT import SensorDHT
from modules.PostgreSQL import PostgreSQL


class Humidity:
    humidity = -1

    def get_humidity(self):
        sensor = SensorDHT()
        self.humidity = sensor.read_humidity()
        return self.humidity

    def save_humidity(self):
        result = False
        database = PostgreSQL()
        get_humidity = self.get_humidity()
        query = 'insert into humidity(valor) values ({})'.format(int(get_humidity))
        if database.run_insert(query):
            print('Se ha guardado la humedad {}°C'.format(get_humidity))
            result = True
        return result
