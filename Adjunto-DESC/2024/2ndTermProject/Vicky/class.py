def estructurar_datos(datos):
    estudiantes = []
    lineas = datos.strip().split('\n')
    for linea in lineas:
        nombre, calificacion = linea.split(', ')
        estudiante = {"nombre": nombre.strip(), "calificacion": int(calificacion)}
        estudiantes.append(estudiante)
    return estudiantes

def encontrar_estudiantes_en_comun(clase1, clase2):
    estudiantes_comun = []
    for estudiante in clase1:
        for estudiante2 in clase2:
            if estudiante['nombre'] == estudiante2['nombre']:
                estudiantes_comun.append({'nombre': estudiante['nombre'], 'calif1': estudiante['calificacion'], 'calif2': estudiante2['calificacion']})
                break
    return estudiantes_comun

def encontrar_estudiantes_unicos(clase1, clase2):
    estudiantes_unicos = []
    for estudiante in clase1:
        encontrado = False
        for estudiante2 in clase2:
            if estudiante['nombre'] == estudiante2['nombre']:
                encontrado = True
                break
        if not encontrado:
            estudiantes_unicos.append(estudiante)
    for estudiante in clase2:
        encontrado = False
        for estudiante2 in clase1:
            if estudiante['nombre'] == estudiante2['nombre']:
                encontrado = True
                break
        if not encontrado:
            estudiantes_unicos.append(estudiante)
    return estudiantes_unicos

def calcular_promedio(estudiantes):
    total = 0
    for estudiante in estudiantes:
        total += estudiante['calificacion']
    return total / len(estudiantes)

datos_clase1 = '''
John Doe, 85
Jane Smith, 78
Michael Brown, 92
Emily Johnson, 88
Daniel Wilson, 74
Olivia Jones, 95
William Garcia, 81
Ava Martinez, 87
Isabella Rodriguez, 90
Sophia Anderson, 77
Mason Lee, 83
Ella Young, 79
James Hernandez, 84
Charlotte Gonzalez, 91
Benjamin Perez, 75
Amelia Lopez, 89
Ethan White, 93
Mia Thompson, 80
Alexander Harris, 85
Aria Clark, 82
Henry Lewis, 76
Evelyn Walker, 94
Sebastian Hall, 72
Abigail Allen, 86
Liam Scott, 78
Sophie Adams, 73
Oscar Nelson, 88
Luna King, 91
Jack Wright, 79
Lucas Green, 84
'''

datos_clase2 = '''
Isaac Moore, 89
Eva Turner, 88
Nathan Martin, 76
Grace Hill, 92
Samuel Adams, 85
Zoe Davis, 81
Aiden Robinson, 87
Chloe Campbell, 90
Gabriel Mitchell, 77
Lily Anderson, 83
Jane Smith, 82
Emily Johnson, 90
Daniel Wilson, 78
Olivia Jones, 97
Ella Young, 81
Charlotte Gonzalez, 89
Amelia Lopez, 91
Mia Thompson, 82
Alexander Harris, 88
Sophia Anderson, 79
Lucas Green, 86
Jack Wright, 82
Luna King, 93
Oscar Nelson, 90
Sophie Adams, 75
Liam Scott, 80
Henry Lewis, 88
Aria Clark, 84
Ethan White, 95
Benjamin Perez, 77
'''

clase1 = estructurar_datos(datos_clase1)
clase2 = estructurar_datos(datos_clase2)

print("Promedio clase 1: ", calcular_promedio(clase1))
print("Promedio clase 2: ", calcular_promedio(clase2))

estudiantes_com = encontrar_estudiantes_en_comun(clase1, clase2)
print("\nEstudiantes en común: ")
for estudiante in estudiantes_com:
    promedio = (estudiante['calif1'] + estudiante['calif2']) / 2
    print(f"{estudiante['nombre']}: {promedio}")

unicos_en_1 = encontrar_estudiantes_unicos(clase1, clase2)
unicos_en_2 = encontrar_estudiantes_unicos(clase2, clase1)
print("\nPromedio de unicos en 1:", calcular_promedio(unicos_en_1))
print("Promedio de unicos en 2:", calcular_promedio(unicos_en_2))

todos_unicos = unicos_en_1 + unicos_en_2
print("\nPromedio de todos los unicos:", calcular_promedio(todos_unicos))
