import time
from Temperature import Temperature


def main():
    temperature = Temperature()
    temperature.save_temperature()


if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)
