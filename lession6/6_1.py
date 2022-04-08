#1. Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.

from enum import IntEnum
import time


class LightColor(IntEnum):

    red = 7
    yellow = 2
    green = 1


class TrafficLight:

    def __init__(self):
        self.__color = LightColor.red

    def running(self):
        for color in LightColor:
            self.__color = color
            print(f"{self.__color}")
            time.sleep(int(self.__color))


x = TrafficLight()
x.running()
