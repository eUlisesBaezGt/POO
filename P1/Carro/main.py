from Clase.Carro import Carro

opcion = 0
carro1 = Carro()

while opcion != 5:
    print("INICIANDO\n")
    print("--------------------------")
    print("1. Impresión de datos")
    print("2. Presionar botón ENGINE (START/STOP)")
    print("3. Presionar botón Trunk Release (OPEN/CLOSE)")
    print("4. Revisar aceite")
    print("5. Salir")

    opcion = int(input("\nIngrese una opción: "))

    if opcion == 1:
        carro1.imprimir()

    elif opcion == 2:
        carro1.enciende_apaga()

    elif opcion == 3:
        carro1.abre_cierra_cajuela()

    elif opcion == 4:
        carro1.revisar_aceite()

    elif opcion == 5:
        print("\nSaliendo...\n")
        print("--------------------------")
