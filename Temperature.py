from SensorDHT import SensorDHT
from PostgreSQL import PostgreSQL


class Temperature:
    temperature = -1

    def get_temperature(self):
        sensor = SensorDHT()
        self.temperature = sensor.read_temperature()
        return self.temperature

    def save_temperature(self):
        result = False
        database = PostgreSQL()
        temperature = self.get_temperature()
        query = 'insert into temperature(valor) values ({})'.format(int(temperature))
        if database.run_insert(query):
            print('Se ha guardado la temperatura {}°C'.format(temperature))
            result = True
        return result
