import os
import serial
import time


class Arduino:
    arduino = serial.Serial()
    arduino.baudrate = 9600
    arduino.bytesize = serial.EIGHTBITS
    arduino.parity = serial.PARITY_NONE
    arduino.stopbits = serial.STOPBITS_ONE
    arduino.timeout = 1
    arduino.xonxoff = False
    arduino.rtscts = False
    arduino.dsrdtr = False
    arduino.writeTimeout = None
    if os.name == 'nt':
        arduino.port = 'COM6'  # para windows
    else:
        arduino.port = '/dev/ttyACM0'  # para linux

    def __init__(self):
        if self.arduino.is_open:
            print('Arduino is connected')
        else:
            print('Arduino is not connected')
            print('Trying to connect with Arduino')
            self.arduino.open()
            time.sleep(2)
            if self.arduino.is_open:
                print('Arduino is now connected')

    def __del__(self):
        try:
            if self.arduino.is_open:
                print('disconnecting from Arduino')
                self.arduino.close()
            else:
                print('Arduino is disconnected')
        except BaseException as exception:
            print(f'An exception has ocurred: {exception}')

    def send_data(self, data):
        if self.arduino.is_open:
            print('Sending data to arduino:"{}"'.format(data))
            self.arduino.write(data.encode())

    def read_line(self):
        if self.arduino.is_open:
            result = self.arduino.readline()
            if result:
                print('Message from Arduino : {}'.format(result.decode('utf-8')))
            else:
                print('Arduino doesn\'t response')

    def send_order(self, data):
        result = False
        if self.arduino.is_open:
            print('Sending data to arduino: {}'.format(data))
            self.arduino.write(data.encode())
            time.sleep(1)
            data = self.arduino.readline()
            if not data or data == b'\r\n':
                print('Arduino response empty')
            else:
                result = data.decode('utf-8').strip('\n')
                print('Arduino response: {}'.format(result))
        else:
            print('Arduino is disconnected')
        return result

    def status(self):
        if self.arduino.is_open:
            print('Arduino is connected')
        else:
            print('Arduino is not connected')
