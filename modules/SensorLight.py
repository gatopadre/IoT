from modules.Arduino import Arduino


class SensorLight:
    key_read_luminocity = '4'

    def read_luminocity(self):
        result = False
        try:
            arduino = Arduino()
            result = arduino.send_order(self.key_read_temp)
        except BaseException as exception:
            print('An Exception has ocurred: {}'.format(exception))
        return result
