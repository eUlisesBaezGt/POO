# CSV. (8 partes a evaluar)
import csv
import pandas as pd


#      a) Genere un archivo csv que tenga tres columnas, la primera con nombre completo, la segunda con la edad y última
#     con el salario.


class CSV:
    #     b) Genere una clase que procesará su el archivo csv. En el constructor de la clase use pandas
    #     para cargar los datos en un atributo (un dataframe), la ruta del archivo le llega como parámetro.

    def __init__(self, path):
        self.path = path
        self.dataframe = pd.read_csv(path)
        # c) En un atributo asigne el MEDIA de las edades.
        self.average_age = self.dataframe['age'].mean()
        # d) En otro atributo asigne la MEDIA de los salarios.
        self.average_salary = self.dataframe['salary'].mean()
        #  e) Añada al atributo dataframe una columna con la diferencia entre el salario y la media.
        self.dataframe['difference'] = self.dataframe['salary'] - self.average_salary
        #  f) En un último atributo asigne el porcentaje del número de salarios por arriba de la media.
        self.percentage = self.dataframe['salary'].mean() / self.dataframe['salary'].mean() * 100

    # g) Implemente el método mágico __repr__ para mostrar los atributos de las medias de las edades, de los salarios
    # #     y el porcentaje del número de salarios por arriba de la media, es decir, el atributo dataframe aquí no se entrega.

    def __repr__(self):
        return f"Average age: {self.average_age}\nAverage salary: {self.average_salary}\nPercentage: {self.percentage}"

#     h) Muestre que su clase ejecuta al implementar un ejemplar.
test = CSV('data.csv')
