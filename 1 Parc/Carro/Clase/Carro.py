import random


class Carro:
    __marca = ""
    __placas = ""  # 6DAFN
    __color = ""
    __duenio = ""
    __encendido = False
    __aceite = 100
    __cajuela_abierta = False

    def __init__(self):
        self.registrar()

    def registrar(self):
        self.__marca = input("Marca: ")
        self.matricular()  # 6DA
        self.__color = input("Color: ")
        self.__duenio = input("Dueño: ")
        self.checar_estado()
        self.cajuela()
        self.checar_aceite()

    def checar_aceite(self):
        st = float(input("Porcentaje de aceite de tu auto: "))
        while st < 0 or st > 100:
            print("Opción inválida")
            st = float(input("Porcentaje de aceite de tu auto: "))
        self.__aceite = st

    def cajuela(self):
        st = input("¿Está tu cajuela abierta? (S/N): ")
        while st != "S" and st != "N":
            print("Opción inválida")
            st = input("¿Está tu cajuela abierta? (S/N): ")
        if st == "S":
            self.__cajuela_abierta = True
        elif st == "N":
            self.__cajuela_abierta = False

    def checar_estado(self):
        st = input("¿Está tu auto encendido? (S/N): ")
        while st != "S" and st != "N":
            print("Opción inválida")
            st = input("¿Está tu auto encendido? (S/N): ")
        if st == "S":
            self.__encendido = True
        elif st == "N":
            self.__encendido = False

    def matricular(self):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '1234567890'
        placa1 = ''
        placa2 = ''
        n = 0
        while n < 3:
            placa1 += random.choice(chars)
            n += 1
        n = 0
        while n < 3:
            placa2 += random.choice(nums)
            n += 1
        self.__placas = placa1 + " - " + placa2

    def mostrar_matricula(self):
        print("Matrícula: ", self.__placas)

    def imprimir(self):
        print("Marca: ", self.__marca)
        self.mostrar_matricula()
        print("Color: ", self.__color)
        print("Dueño: ", self.__duenio)
        print("Encendido: ", self.__encendido)
        print("Cajuela abierta: ", self.__cajuela_abierta)
        print("Aceite: ", self.__aceite)

    def enciende_apaga(self):
        if self.__encendido is True:
            print("Estado inicial: ENCENDIDO")
            self.__encendido = False
            print("Estado final: APAGADO")
        elif self.__encendido is False:
            print("Estado inicial: APAGADO")
            self.__encendido = True
            print("Estado final: ENCENDIDO")

    def abre_cierra_cajuela(self):
        if self.__cajuela_abierta is True:
            print("Estado inicial: ABIERTA")
            self.__cajuela_abierta = False
            print("Estado final: CERRADA")
        elif self.__cajuela_abierta is False:
            print("Estado inicial: CERRADA")
            self.__cajuela_abierta = True
            print("Estado final: ABIERTA")

    def revisar_aceite(self):
        if self.__aceite == 0:
            print("Sin aceite")
        elif self.__aceite < 20:
            print("El aceite está por debajo del 20%")
        elif 20 >= self.__aceite < 40:
            print("El aceite está por debajo del 40%")
        elif 40 <= self.__aceite < 60:
            print("El aceite está por debajo del 60%")
        elif 60 <= self.__aceite < 80:
            print("El aceite está por debajo del 80%")
        elif 80 <= self.__aceite < 100:
            print("El aceite está entre 80% y 100%")
        elif self.__aceite == 100:
            print("El aceite está lleno")
