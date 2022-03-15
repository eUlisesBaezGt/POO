class Persona:

    def __init__(self, nombre, edad, sexo):
        self.Nombre = nombre
        self.__Edad = edad
        self.Sexo = sexo

    @property
    def edad(self):
        return self.__Edad

    @edad.setter
    def edad(self, edad):
        self.__Edad = edad

    def ver_datos(self):
        print("Nombre: ", self.Nombre)
        print("Edad: ", self.__Edad)
        print("Sexo: ", self.Sexo)


class Alumno(Persona):
    def __init__(self, nombre, edad, sexo, mid, carrera, semestre):
        super().__init__(nombre, edad, sexo)
        self.Id = mid
        self.Carrera = carrera
        self.Semestre = semestre

    def mostrar_datos(self):
        super().ver_datos()
        print("Id: ", self.Id)
        print("Carrera: ", self.Carrera)
        print("Semestre: ", self.Semestre)


class Profesor(Persona):
    def __init__(self, nombre, edad, sexo, mid, materia, salario):
        super().__init__(nombre, edad, sexo)
        self.Id = mid
        self.Materia = materia
        self.__Salario = salario

    @property
    def salario(self):
        return self.__Salario

    @salario.setter
    def salario(self, salario):
        self.__Salario = salario

    def mostrar_datos(self):
        super().ver_datos()
        print("Id: ", self.Id)
        print("Materia: ", self.Materia)
        print("Salario: ", self.salario)
