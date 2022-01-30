import time
from modules.Temperature import Temperature
from modules.Humidity import Humidity
from modules.Luminocity import Luminocity


def main():
    temperature = Temperature()
    humidity = Humidity()
    luminocity = Luminocity()

    temperature.save_temperature()
    humidity.save_humidity()
    luminocity.save_luminocity()


if __name__ == '__main__':
    while True:
        main()
        time.sleep(24)
