import random


def generar_id():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    id_generado = ""
    n = 0
    while n < 8:
        id_generado += random.choice(chars)
        n += 1
    return id_generado


class Cuenta:
    __ID_Cuenta = generar_id()
    __Monto = 0.0

    def __init__(self, titular):
        self.titular = titular

    @property
    def id_cuenta(self):
        return self.__ID_Cuenta

    @id_cuenta.setter
    def id_cuenta(self, id_cuenta):
        self.__ID_Cuenta = id_cuenta

    @property
    def monto(self):
        return self.__Monto

    @monto.setter
    def monto(self, monto):
        self.__Monto = monto

    def imprimir(self):
        self.titular.mostrar()
        print("ID Cuenta: ", self.id_cuenta)
        print("Monto: ", self.monto)
        print("----------------------\n")

    def depositar(self):
        print("\nDepositando dinero")
        print("----------------------")
        print("Monto inicial: ", self.monto)
        print("----------------------")
        v = float(input("Ingrese el monto a depositar: "))
        self.validar_deposito(v)
        print("Monto final: ", self.monto)
        print("----------------------\n")

    def validar_deposito(self, v):
        while v <= 0:
            print("ERROR: El monto debe ser mayor a 0")
            v = float(input("Ingrese el monto a depositar: "))
        self.monto += v

    def retirar(self):
        print("\nRetirando dinero")
        print("----------------------")
        print("Monto inicial: ", self.monto)
        print("----------------------")
        v = float(input("Ingrese el monto a retirar: "))
        self.validar_retiro(v)
        print("Monto final: ", self.monto)
        print("----------------------\n")

    def validar_retiro(self, v):
        while v > self.monto:
            print("ERROR: Saldo insuficiente")
            v = float(input("Ingrese el monto a retirar: "))
        self.monto -= v
