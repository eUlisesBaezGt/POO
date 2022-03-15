from Class.Cuadrilateros import Cuadrado
from Class.Cuadrilateros import Rectangulo
from Class.Cuadrilateros import Trapecio

c1 = Cuadrado(20, 20, 20, 20)  # 4 LADOS
c2 = Rectangulo(40, 20, 40, 20)  # 1 base y 1 altura (ciclo repetido 2 veces)
c3 = Trapecio(50, 30, 20, 35)  # base mayor, base menor, altura, lateral

print("\nCuadrado:")
c1.area_cuadrado()

print("\nRectangulo:")
c2.area_rectangulo()

print("\nTrapecio")
c3.area_trapecio()
