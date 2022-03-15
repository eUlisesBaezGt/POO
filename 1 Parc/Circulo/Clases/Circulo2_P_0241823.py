import math


class Circulo:
    __Radio = 0

    def __init__(self, radio=0):
        self.__Radio = radio

    @property
    def radio(self):
        return self.__Radio

    @radio.setter
    def radio(self, nuevo_radio):
        self.__Radio = nuevo_radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
