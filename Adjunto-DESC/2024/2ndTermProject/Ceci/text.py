num_textos = int(input("Cuántos textos? "))
textos = []

def llenar_textos():
    for indice, _ in enumerate(range(0, num_textos), 1):
        nuevo_texto = input(f"Ingresa texto {indice}: ").lower()
        textos.append(nuevo_texto)
llenar_textos()


def separar_palabras(texto):
    palabras = texto.split(" ")
    return palabras

diccionarios = []

for texto in textos:
    palabras = separar_palabras(texto)
    contador = {}
    for palabra in palabras:
        cuenta = palabras.count(palabra)
        contador[palabra] = cuenta
    diccionarios.append(contador)

print("Contadores de vocales: ")
print(diccionarios)

en_todos = True
for diccionario in diccionarios[1:]:
    if diccionario.keys() != diccionarios[0].keys():
        en_todos = False
        break

if en_todos:
    palabras_frecuentes = {}
    for palabra in diccionarios[0].keys():
        frecuencia = sum([diccionario[palabra] for diccionario in diccionarios])
        palabras_frecuentes[palabra] = frecuencia
    print("Palabras frecuentes y su frecuencia: ", palabras_frecuentes)
else:
    print("No hay palabras que aparezcan en todos los textos")
