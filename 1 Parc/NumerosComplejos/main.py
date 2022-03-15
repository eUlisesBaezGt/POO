from Clases.Complejo import Complejo


def suma(c1, c2):
    s = str(c1.real + c2.real) + ", " + str(c1.imag + c2.imag) + "i"
    print("Resultado de la suma: " + s)


def resta(c1, c2):
    s = str(c1.real - c2.real) + ", " + str(c1.imag - c2.imag) + "i"
    print("Resultado de la resta: " + s)


def multiplica(c1, c2):
    s = str((c1.real * c2.real) - (c1.imag * c2.imag)) + " , " + str((c1.real * c2.imag) + (c1.imag * c2.real)) + "i"
    print("Resultado de la multiplicación: " + s)


def multiplica_por_numero(c, n):
    s = str(c.real * n) + " , " + str(c.imag * n) + "i"
    print("Resultado de la multiplicación: " + s)


def divide(c1, c2):
    s = str(((c1.real * c2.real) +
             (c1.imag * c2.imag)) / (c2.real ** 2 + c2.imag ** 2)) + " , " + \
        str(((c1.imag * c2.real) - (c1.real * c2.imag)) / (c2.real ** 2 + c2.imag ** 2)) + "i"
    print("Resultado de la división: " + s)


opcion = 0

entrada = input("Ingrese su primer número: ")
cn1 = Complejo()
cn1.separar(entrada)

entrada2 = input("Ingrese su segundo número: ")
cn2 = Complejo()
cn2.separar(entrada2)

while opcion != 6:
    print("Iniciando Menu")
    print("--------------------------------------")

    print("1. Sumar dos números complejos.")
    print("2. Restar dos números complejos.")
    print("3. Multiplicar dos números complejos.")
    print("4. Multiplicar un número complejo por un número double.")
    print("5. Dividir dos números complejos.")
    print("6. Salir")

    opcion = int(input("Ingrese una opción: "))
    print("--------------------------------------")

    if opcion == 1:
        suma(cn1, cn2)
    elif opcion == 2:
        resta(cn1, cn2)
    elif opcion == 3:
        multiplica(cn1, cn2)
    elif opcion == 4:
        v = int(input("Ingrese el número por el cual quiere multiplicar: "))
        cn = int(input("Ingrese 1 o 2 para multiplicar por el primer o segundo número respectivamente: "))
        if cn == 1:
            cn = cn1
        elif cn == 2:
            cn = cn2
        else:
            print("Opción no valida")
        multiplica_por_numero(cn, v)
    elif opcion == 5:
        divide(cn1, cn2)
    elif opcion == 6:
        print("Saliendo...")
    else:
        print("Opción inválida.")
