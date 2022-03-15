from Class.Cuadrilatero import Cuadrado
from Class.Cuadrilatero import Rectangulo
from Class.Cuadrilatero import Trapecio

c1 = Cuadrado(2, 2, 2, 2)  # 4 LADOS
c2 = Rectangulo(2, 3, 2, 3)  # 1 base y 1 altura (ciclo repetido 2 veces)
c3 = Trapecio(3, 2, 1.5, 2)  # base mayor, base menor, altura, lateral

print("\nCuadrado:")
c1.perimetro()
c1.area()

print("\nRectangulo:")
c2.perimetro()
c2.area()

print("\nTrapecio")
c3.perimetro_trapecio()
c3.area_trapecio()
