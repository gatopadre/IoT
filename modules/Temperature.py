from modules.SensorDHT import SensorDHT
from modules.PostgreSQL import PostgreSQL
from helpers import terminal_messages


class Temperature:
    temperature = -1

    def get_temperature(self):
        sensor = SensorDHT()
        terminal_messages.show_message('info', 'Reading temperature')
        self.temperature = sensor.read_temperature()
        return self.temperature

    def save_temperature(self):
        result = False
        database = PostgreSQL()
        temperature = self.get_temperature()
        query = 'insert into temperature(valor) values ({:.2f})'.format(float(temperature))
        if database.run_insert(query):
            terminal_messages.show_message('success', 'Temperature {:.2f}°C saved'.format(float(temperature)))
            result = True
        return result
