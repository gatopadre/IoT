from modules.Arduino import Arduino
'''
Sensor must be conected this way:
    - if you look the sensor from the front the order is data, energy, ground
    - if you look the sensor from behind the order is ground, energy, data
    - actually the pin set into arduino code for read data is the pin n:5
'''


class SensorDHT:
    key_read_temp = '2'
    key_read_hum = '3'

    def read_temperature(self):
        result = False
        try:
            arduino = Arduino()
            result = arduino.send_order(self.key_read_temp)
        except BaseException as exception:
            print('An Exception has ocurred: {}'.format(exception))
        return result

    def read_humidity(self):
        result = False
        try:
            arduino = Arduino()
            result = arduino.send_order(self.key_read_hum)
        except BaseException as exception:
            print('An Exception has ocurred: {}'.format(exception))
        return result
