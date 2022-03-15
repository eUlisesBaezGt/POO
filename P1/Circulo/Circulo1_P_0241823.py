from Clases.Circulo2_P_0241823 import Circulo


circulo = Circulo()

respuesta = 0

while respuesta != 4:
    print("--------------------------")
    print("El radio del círculo es: ", circulo.radio)
    print("Opciones: ")

    print("1. Cambiar el radio")
    print("2. Calcular el área")
    print("3. Calcular el perímetro")
    print("4. Salir")

    respuesta = int(input("¿Que desea realizar?: "))

    if respuesta == 1:
        circulo.radio = int(input("Ingrese el nuevo radio: "))
    elif respuesta == 2:
        print("El área del círculo es: ", circulo.area())
        temp = input("Presione enter para continuar ")
    elif respuesta == 3:
        print("El perímetro del círculo es: ", circulo.perimetro())
        temp = input("Presione enter para continuar ")
    elif respuesta == 4:
        print("Gracias por usar el programa")
        temp = input("Presione enter para salir ")
        break
    else:
        print("Opción inválida")
        temp = input("Presione enter para continuar ")
