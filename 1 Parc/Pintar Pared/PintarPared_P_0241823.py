class Rectangulo:
    Largo = 0
    Ancho = 0

    def __init__(self, largo, ancho):
        self.Largo = largo
        self.Ancho = ancho

    @property
    def largo(self):
        return self.Largo

    @largo.setter
    def largo(self, largo):
        self.Largo = largo

    @property
    def ancho(self):
        return self.Ancho

    @ancho.setter
    def ancho(self, ancho):
        self.Ancho = ancho

    @property
    def area(self):
        return self.Largo * self.Ancho

    @area.setter
    def area(self, area):
        self.area = area

    print("Pintar Pared")
    print("-----------")


pared_ancho = int(input("Ingrese el ancho de la pared: "))
pared_alto = int(input("Ingrese el alto de la pared: "))
pared = Rectangulo(pared_ancho, pared_alto)
print("Area de la pared: ", pared.area)

ventana_ancho = int(input("Ingrese el ancho de la ventana: "))
ventana_alto = int(input("Ingrese el alto de la ventana: "))
ventana = Rectangulo(ventana_ancho, ventana_alto)
print("Area de la ventana: ", ventana.area)


def calcular_tiempo():
    total = 0
    if pared.area > ventana.area:
        total = pared.area - ventana.area
    else:
        print("La ventana es mas grande que la pared")
    tiempo = total * 10
    print("El tiempo para pintar es: ", tiempo, "minutos.")


calcular_tiempo()
