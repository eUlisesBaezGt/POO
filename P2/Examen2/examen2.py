########  Lineas 3 al 24: Generacion aleatoria de archivo VisitasAlHospital.txt ########

#import random

#depts = ["Otorrinolaringologia","Oftalmologia","Hematologia","Urologia","Nefrologia","Ortopedia","Cirugia Plastica","Dermatologia","Geriatria","Laboratorio","Radiologia e Imagenologia","Consulta Externa","Medicina Preventiva","Banco de Sangre","Neurologia y Neurocirugia"]

#def genNumbers(lim):
#    numbers = []
#    i = random.randint(1,4)
#    for j in range(i):
#        t = random.randint(1,10)
#        if (t%3) == 1 and lim < 3:
#            numbers.append(genNumbers(lim+1))
#        else:
#            for k in range(i):
#                numbers.append(random.randint(8860,8900))
#    return  numbers

#file = open("VisitasAlHospital.txt","w")
#for k in depts:
#    file.write(k+"=")
#    file.write(str(genNumbers(0)))
#    file.write("\n")
#file.close()



########  Solución de examen 2do parcial ########

from ast import literal_eval
import json

departamentos={}

visitasFile = open("VisitasAlHospital.txt","r")
visitas = visitasFile.readlines()
visitasFile.close()

for v in visitas:
    v = v.split("=")
    departamentos[v[0]] = literal_eval(v[1])


pacientes = {}
anidados={}

def analizar(codigo, departamento):
    if type(codigo) == int:
        if codigo in pacientes.keys():
            if departamento in pacientes[codigo].keys():
                pacientes[codigo][departamento] += 1
            else:
                pacientes[codigo][departamento] = 1
        else:
            pacientes[codigo] = {}
            pacientes[codigo][departamento] = 1
    else:
        if departamento not in anidados.keys(): anidados[departamento] = 0
        anidados[departamento] += 1
        for c in codigo:
            analizar(c,departamento)


for k in departamentos.keys():
    analizar(departamentos[k],k)

print(pacientes)

resultados = open("analisis.json","w")
resultados.write(json.dumps(pacientes, indent=4))
resultados.close()