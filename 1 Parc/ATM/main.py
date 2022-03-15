from Clases.Cuenta import Cuenta
from Clases.Persona import Persona

opcion = 0

persona1 = Persona()
cuenta1 = Cuenta(persona1)

persona1.valores()

while opcion != 4:
    print("Iniciando Menu")
    print("--------------------------------------\n")

    print("1. Mostrar datos la cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir.")

    opcion = int(input("Ingrese una opción: "))
    print("--------------------------------------")

    if opcion == 1:
        cuenta1.imprimir()
    elif opcion == 2:
        cuenta1.depositar()
    elif opcion == 3:
        cuenta1.retirar()
    elif opcion == 4:
        print("Saliendo...\n\n")
    else:
        print("Opción no valida")
