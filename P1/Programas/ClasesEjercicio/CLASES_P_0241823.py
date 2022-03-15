# Pelota
class Pelota:             # ATRIBUTOS
    Deporte = ""
    Tamano = 0
    __Rebote = 0
    __Presion = 0

    def __init__(self, deporte, tamano, rebote, presion):  # CONSTRUCTOR
        self.Deporte = deporte
        self.Tamano = tamano
        self.rebote = rebote
        self.presion = presion

    @property
    def rebote(self):
        return self.__Rebote

    @rebote.setter
    def rebote(self, rebote):
        self.__Rebote = rebote

    @property
    def presion(self):
        return self.__Presion

    @presion.setter
    def presion(self, presion):
        self.__Presion = presion

    def inflar(self):
        print("Inflando..............")
        print("Presión inicial --> " + str(self.presion))
        print("Rebote inicial --> " + str(self.rebote))
        self.presion += 1
        self.rebote += 5
        print("Presión final --> " + str(self.presion))
        print("Rebote final --> " + str(self.rebote))

    def desinflar(self):
        print("Desinflando..............")
        print("Presión inicial --> " + str(self.presion))
        print("Rebote inicial --> " + str(self.rebote))
        self.presion -= 1
        self.rebote -= 5
        print("Presión final --> " + str(self.presion))
        print("Rebote final --> " + str(self.rebote))


pelota1 = Pelota("Futbol", 5, 110, 2)
pelota2 = Pelota("Basketball", 7, 200, 5)

print("Pelota 1: ")
pelota1.inflar()
print("\n")
pelota1.desinflar()

print("\n Pelota 2: ")
pelota2.inflar()
print("\n")
pelota2.desinflar()


# CASA
class Casa:             # ATRIBUTOS
    Calle = ""
    Numero = 0
    CP = ""
    __Luces = 0
    __Ventanas = 0

    def __init__(self, calle, numero, cp, luces, ventanas):
        self.Calle = calle
        self.Numero = numero
        self.CP = cp
        self.Luces = luces
        self.Ventanas = ventanas

    @property
    def ventanas(self):
        return self.__Ventanas

    @ventanas.setter
    def ventanas(self, ventanas):
        self.__Ventanas = ventanas

    @property  # GETTER
    def luces(self):
        return self.__Luces

    @luces.setter  # SETTER
    def luces(self, luces):
        self.__Luces = luces

    def salir(self):            # MÉTODOS
        print("Saliendo...................")
        print("Apagando las luces...")
        self.__Luces = 0
        print("Hay " + str(self.__Luces) + " luces encendidas")
        print("Cerrando las ventanas...")
        self.__Ventanas = 0
        print("Hay " + str(self.__Luces) + " ventanas abiertas")

    def entrar(self):
        print("Entrando.....................")
        print("Encendiendo las luces...")
        self.__Luces = 10
        print("Hay " + str(self.__Luces) + " luces encendidas")
        print("Abriendo las ventanas...")
        self.__Ventanas = 5
        print("Hay " + str(self.__Luces) + " ventanas abiertas")


casa1 = Casa("Calle 2", 73, "024", 4, 1)
casa2 = Casa("Calle 8", 21, "098", 7, 3)

print("\n\n Casa 1: ")
casa1.entrar()
print("\n")
casa1.salir()

print("\n Casa 2: ")
casa2.entrar()
print("\n")
casa2.salir()


# Carro
class Carro:
    Marca = ""
    Modelo = ""
    __Color = ""
    __Estado = ""

    def __init__(self, marca, modelo, color, estado):
        self.Marca = marca
        self.Modelo = modelo
        self.__Color = color
        self.__Estado = estado

    @property
    def color(self):
        return self.__Color

    @color.setter
    def color(self, color):
        self.__Color = color

    @property
    def estado(self):
        return self.__Estado

    @estado.setter
    def estado(self, estado):
        self.__Estado = estado

    def apagar(self):
        print("Color inicial --> " + self.__Color)
        print("Apagando.....................")
        self.__Color = "Negro"
        print("Color final --> " + self.__Color)
        self.__Estado = "Apagado"
        print("Estado --> " + str(self.__Estado))

    def encender(self):
        print("Color inicial --> " + self.__Color)
        print("Encendiendo.....................")
        self.__Color = "Blanco"
        print("Color final --> " + self.__Color)
        self.__Estado = "Encendido"
        print("Estado --> " + str(self.__Estado))


carro1 = Carro("Lamborghini", "Huracan", "Amarillo", "Apagado")
carro2 = Carro("Bugatti", "Veyron", "Negro", "Apagado")


print("\n\n Carro 1: ")
carro1.encender()
print("\n")
carro1.apagar()

print("\n\n Carro 2: ")
carro2.encender()
print("\n")
carro2.apagar()
