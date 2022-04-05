from ast import literal_eval
import json


def program():
    file = "VisitasAlHospital.txt"
    dict = {}

    # --------------------------------------------------
    # Leer el archivo de texto y crea el diccionario según departamento médico.
    # Donde cada departamentos es una llave del diccionario y el contenido de la l
    # lave es la linea correspondiente al archivo
    # can Use literal_eval() to coiert a string to a dictionary
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.split("=")

            # Extract area
            line[0] = line[0].strip()

            # Extract data
            line[1] = literal_eval(line[1])

            # add it as a dictionary key
            # add the line as a value to the key
            dict[line[0]] = line[1]

    print(dict)

    # --------------------------------------------------
    # Crear un nuevo diccionario de pacientes vacio
    pacientes = {}

    # Usando recursividad, itera sobre cada grupo de cada departamento y agrega else id del paciente al nuevo
    # diccionario como una llave como algunos de los ids de pacientes sep respectivamente, se hace un contador
    # cuenta1 las visitas por departamentos y añade al diccionario para determinar si está un grupo o un solo dato,
    # usar type()

    # split dict by department
    for key in dict:
        for key2 in dict[key]:
            if key2 not in pacientes:
                pacientes[key2] = dict[key][key2]
                # print(pacientes)
            else:
                pacientes[key2] += dict[key][key2]
                # print(pacientes)


    for key, value in dict.items():
        for i in value:
            if type(i) == list:
                for j in i:
                    if j in pacientes:
                        pacientes[j] += 1
                    else:
                        pacientes[j] = 1
            else:
                if i in pacientes:
                    pacientes[i] += 1
                else:
                    pacientes[i] = 1

    print(pacientes)

    # --------------------------------------------------
    # Al terminar las clasificaciones de los pacientes, guardar en un archivo diccionario.json, usar prettyprint
    # json > indent
    with open("analisis.json", "w") as f:
        json.dump(pacientes, f, indent=4)
        json.dump(dict, f, indent=4)
