from modules.SensorLight import SensorLight
from modules.PostgreSQL import PostgreSQL
from helpers import terminal_messages


class Luminocity:
    """
    status:
    - 1 light is not suficient
    - 0 light is on
    """
    luminocity = -1

    def get_luminocity(self):
        sensor = SensorLight()
        terminal_messages.show_message('info', 'Reading luminocity')
        self.luminocity = sensor.read_luminocity()
        return self.luminocity

    def save_luminocity(self):
        result = False
        database = PostgreSQL()
        luminocity = self.get_luminocity()
        query = 'insert into luminocity(valor) values ({})'.format(float(luminocity))
        if database.run_insert(query):
            terminal_messages.show_message('success', 'Luminocity {} saved'.format(float(luminocity)))
            result = True
        return result
