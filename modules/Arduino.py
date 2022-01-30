import os
import serial
import time
from helpers import terminal_messages


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
        # arduino.port = '/dev/ttyACM0'  # para linux
        arduino.port = '/dev/ttyUSB0'  # para linux

    def __init__(self):
        if self.arduino.is_open:
            terminal_messages.show_message('success', 'Arduino is connected')
        else:
            terminal_messages.show_message('info', 'Arduino is not connected')
            terminal_messages.show_message('info', 'Trying to connect with Arduino')
            self.arduino.open()
            time.sleep(2)
            if self.arduino.is_open:
                terminal_messages.show_message('success', 'Arduino is connected')

    def __del__(self):
        try:
            if self.arduino.is_open:
                terminal_messages.show_message('info', 'disconnecting from Arduino')
                self.arduino.close()
            else:
                terminal_messages.show_message('success', 'Arduino is disconnected')
        except BaseException as exception:
            terminal_messages.show_message('error', 'An exception has ocurred: {}'.format(exception))

    def send_data(self, data):
        if self.arduino.is_open:
            terminal_messages.show_message('info', 'Sending data to arduino:"{}"'.format(data))
            self.arduino.write(data.encode())

    def read_line(self):
        if self.arduino.is_open:
            result = self.arduino.readline()
            if result:
                terminal_messages.show_message('info', 'Message from Arduino : {}'.format(result.decode('utf-8')))
            else:
                terminal_messages.show_message('error', 'Arduino doesn\'t response')

    def send_order(self, data):
        result = False
        if self.arduino.is_open:
            terminal_messages.show_message('info', 'Sending data to arduino: {}'.format(data))
            self.arduino.write(data.encode())
            time.sleep(1)
            data = self.arduino.readline()
            if not data or data == b'\r\n':
                terminal_messages.show_message('error', 'Arduino response empty')
            else:
                result = data.decode('utf-8').strip('\n')
                terminal_messages.show_message('success', 'Arduino response: {}'.format(result))
        else:
            terminal_messages.show_message('warning', 'Arduino is disconnected')
        return result

    def status(self):
        if self.arduino.is_open:
            terminal_messages.show_message('info', 'Arduino is connected')
        else:
            terminal_messages.show_message('info', 'Arduino is not connected')
