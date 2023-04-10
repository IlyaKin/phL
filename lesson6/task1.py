# Задание1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from datetime import datetime as dt


class TrafficLight:
    states = {'red': 7, 'yellow': 2, 'green': 5}
    __color = ''

    def running(self):
        for color, sw_time in self.states.items():
            self.__color = color
            start_state_time = dt.now()

            print(f"{self.__color} "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"{self.__color} after"
                  f"{(dt.now() - start_state_time).seconds} seconds")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
