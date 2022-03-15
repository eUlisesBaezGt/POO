class Persona(object):
    __Nombre = ""
    __Edad = 0
    __CURP = ""

    def __init__(self, nombre="", edad=0, curp=""):
        self.menor_edad = None
        self.__Nombre = nombre
        self.__Edad = edad
        self.__CURP = curp

    @property
    def nombre(self):
        return self.__Nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__Nombre = nombre

    @property
    def edad(self):
        return self.__Edad

    @edad.setter
    def edad(self, edad):
        self.__Edad = edad

    @property
    def curp(self):
        return self.__CURP

    @curp.setter
    def curp(self, curp):
        self.__CURP = curp

    def valores(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
        self.curp = input("CURP (8 dígitos): ")
        self.validar_entradas()

    def validar_entradas(self):
        while self.edad <= 0:
            print("Edad no válida")
            self.edad = int(input("Ingrese de nuevo su edad: "))

        if self.edad < 18:
            self.menor_edad = True

        while len(self.__CURP) != 8:
            print("CURP no válida")
            self.__CURP = input("Ingrese de nuevo su CURP: ")

    def mostrar(self):
        print("Imprimiendo datos")
        print("----------------------\n")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("CURP:", self.curp)
