from modules.SensorDHT import SensorDHT
from modules.PostgreSQL import PostgreSQL
from helpers import terminal_messages

class Humidity:
    humidity = -1

    def get_humidity(self):
        sensor = SensorDHT()
        terminal_messages.show_message('info', 'Reading humidity')
        self.humidity = sensor.read_humidity()
        return self.humidity

    def save_humidity(self):
        result = False
        database = PostgreSQL()
        get_humidity = self.get_humidity()
        query = 'insert into humidity(valor) values ({:.2f})'.format(float(get_humidity))
        if database.run_insert(query):
            terminal_messages.show_message('success', 'Humidity {:.2f}% Saved'.format(float(get_humidity)))
            result = True
        return result
