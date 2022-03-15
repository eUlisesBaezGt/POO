class Perro:
    nombre = ""
    color = ""
    identidad = ""
    raza = ""
    hambre = 0

    def __init__(self, nombre):
        self.nombre = nombre

    def alimentar(self, comida):
        if self.hambre - comida < 0:
            self.hambre = 0
        else:
            self.hambre -= comida

    def pasear(self):
        self.hambre = 10


perro1 = Perro("Firulais")
print(perro1.nombre)

if perro1.hambre == 0:
    perro1.pasear()

for x in range(6):
    perro1.alimentar(2)

print(perro1.hambre)
