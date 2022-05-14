# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:05:14 2022

@author: User
"""


class Persona():
    def __init__(self, nombre, edad, sexo, peso):
        self.nombre = nombre
        self.edad = int(edad)
        self.__RFC = ""
        self.sexo = sexo
        self.peso = float(peso)
        self.altura = 0.0

    def llenarAltura(self, altura):
        if (altura < 100):
            self.altura = 100
        else:
            self.altura = altura

    def llenarRFC(self, RFC):
        self.__RFC = RFC

    def calcularIMC(self):
        IMC = (self.peso / (self.altura * self.altura))

        if (IMC < 20):
            print("la persona" + self.nombre + " está por debajo de su peso ideal.")
        elif (IMC >= 20 and IMC <= 25):
            print("la persona " + self.nombre + " está en su peso ideal.")
        elif (IMC > 25):
            print("La persona " + self.nombre + " tiene sobrepeso.")

    def esMayorDeEdad(self):
        if (self.edad >= 18):
            print("La persona " + self.nombre + " es mayor de edad.")
        elif (self.edad < 18):
            print("la persona " + self.nombre + " es menor de edad.")

    def mostrarDatos(self):
        print(vars(self))


class Profesionista(Persona):
    def __init__(self, nombre, edad, sexo, peso, grado_de_estudios):
        super().__init__(nombre, edad, sexo, peso)
        self.grado_de_estudios = grado_de_estudios

    def esMayorDeEdad(self):
        if (self.edad >= 18):
            print("La persona " + self.nombre + " es mayor de edad y profesionista.")
        elif (self.edad < 18):
            print(
                "Parece que " + self.nombre + " es una persona superdotada porque es Profesionista sin ser mayor de edad. ")


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, peso, nivel_de_estudios):
        super().__init__(nombre, edad, sexo, peso)
        self.nivel_de_estudios = nivel_de_estudios

    def esMayorDeEdad(self):
        if (self.edad >= 18):
            print("La persona " + self.nombre + " es mayor de edad y estudiante.")
        elif (self.edad < 18):
            print("la persona " + self.nombre + " es menor de edad. ")


class Profesionista_Alto_Nivel(Profesionista, Estudiante):
    def __init__(self, nombre, edad, sexo, peso, grado_de_estudios):
        self.nombre = nombre
        self.edad = int(edad)
        self.sexo = sexo
        self.peso = float(peso)
        self.altura = 0.0
        self.grado_de_estudios = grado_de_estudios
        self.nivel_de_estudios = "Posgrado"

    def esMayorDeEdad(self):
        Profesionista.esMayorDeEdad(self)

    def PercentilDeRespondabilidad(self, pc, pe=0):
        percentil_calculado = (pc)
        percentil_extra = (pe)
        try:
            print("El percentil de responsabilidad calculado de " + self.nombre + " es " + str(
                percentil_calculado + percentil_extra) + ".")
        except TypeError:
            print("El percentil tiene que tener un valor númerico.")

    def __del__(self):
        print("Este profesionista de alto nivel fue eliminado.")


persona1 = Profesionista('Ana Sofía', 20, 'M', 52, 'Universidad')
persona1.llenarAltura(1.60)
persona1.llenarRFC('180502')
persona1.calcularIMC()
persona1.esMayorDeEdad()
persona1.mostrarDatos()
print("")

persona2 = Estudiante('Nayeli', 17, 'M', 48, 'Preparatoria')
persona2.llenarAltura(1.55)
persona2.llenarRFC('070902')
persona2.calcularIMC()
persona2.esMayorDeEdad()
persona2.mostrarDatos()
print("")

persona3 = Profesionista_Alto_Nivel('Carlos', 50, 'H', 65, 'Maestría')
persona3.llenarAltura(1.70)
persona3.llenarRFC('191102')
persona3.calcularIMC()
persona3.esMayorDeEdad()
persona3.mostrarDatos()

percentil_calculado1 = input("Ingrese el percentil calculado como un número entero entre 0 y 100: ")
try:
    percentil_calculado1 = int(percentil_calculado1)
    if (percentil_calculado1 >= 0 and percentil_calculado1 <= 100):
        capturar = input("¿Quieres ingresar el valor percentil extra? (Sí/No) ")
        if (capturar == "Sí"):
            percentil_extra1 = input("Ingrese el percentil extra como un número entero entre 0 y 100: ")
            try:
                percentil_extra1 = int(percentil_extra1)
                if (percentil_extra1 >= 0 and percentil_extra1 <= 100):
                    persona3.PercentilDeRespondabilidad(percentil_calculado1, percentil_extra1)
                else:
                    print("El percentil extra tiene que ser un número entero entre 0 y 100.")

            except TypeError:
                print("NO letras")
                # print("El percentil extra únicamente acepta valores de números enteros, por lo tanto, " + str(
                #     percentil_extra1) + " no es un número entero.")
        elif (capturar == "No"):
            print("El percentil extra es definido por default con un 0.")
            persona3.PercentilDeRespondabilidad(percentil_calculado1)
    else:
        print("El percentil calculado deben estar entre 0 y 100: ")
except ValueError:
    print("NO letras")
except TypeError:
    print("El percentil calculado únicamente acepta valores de números enteros, por lo tanto, " + str(
        percentil_calculado1) + " no es un número entero.")
print("")
del persona3

# print(vars(persona3))