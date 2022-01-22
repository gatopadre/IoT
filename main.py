import time
from modules.Temperature import Temperature
from modules.Humidity import Humidity


def main():
    temperature = Temperature()
    humidity = Humidity()

    temperature.save_temperature()
    humidity.save_humidity()


if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)
