from ast import literal_eval
import json

archivo = open("VisitasAlHospital.txt", "r")
visitas = archivo.readlines()
archivo.close()

departamentos = {}
for v in visitas:
    v = v.split("=")
    departamentos[v[0]] = literal_eval(v[1])

pacientes = {}
anidados = {}

def iterar_grupo(arreglo,departamento):
    for codigo in arreglo:
        if type(codigo) ==int:
            if codigo in pacientes.keys():
                if departamento in pacientes[codigo].keys():
                    pacientes[codigo][departamento] += 1
                else:
                    pacientes[codigo][departamento] = 1
            else:
                pacientes[codigo] = {}
                pacientes[codigo][departamento] = 1
        else:
            iterar_grupo(codigo,departamento)



def iterar_grupo_avanzado(arreglo,departamento):
    pass

for i in departamentos.keys():
    iterar_grupo(departamentos[i], i)

print(pacientes)


with open("Resolucion.json", "w") as f:
    json.dump(pacientes, f, indent=4)
