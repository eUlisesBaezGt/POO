num_textos = int(input("¿Cuántos textos? "))
textos = []

def obtener_textos(num_textos, textos):
    for indice in range(1, num_textos + 1):
        nuevo_texto = input(f"Ingrese texto {indice}: ").lower()
        textos.append(nuevo_texto)
    return num_textos, textos

def dividir_en_palabras(texto):
    return texto.split(" ")

def obtener_frecuencia_palabra(palabra, diccionario):
    return diccionario.get(palabra, 0)

def encontrar_palabras_comunes(diccionarios):
    """
    This function takes a list of dictionaries as input and returns a set of words that are common to all dictionaries.

    :param diccionarios: A list of dictionaries where each dictionary represents a set of words and their frequencies.
    :return: A set of words that are common to all dictionaries.
    """
    palabras_comunes = set()  # Initialize an empty set to store the common words
    for palabra in diccionarios[0].keys():  # Iterate over the keys of the first dictionary
        # Check if the current word is present in all dictionaries except the first one
        if all(palabra in dic.keys() for dic in diccionarios[1:]):
            palabras_comunes.add(palabra)  # If it is, add it to the set of common words
    return palabras_comunes  # Return the set of common words

num_textos, textos = obtener_textos(num_textos, textos)

contadores = []
for i, texto in enumerate(textos, start=1):
    palabras = dividir_en_palabras(texto)
    contador_de_palabras = {}
    for palabra in palabras:
        contador_de_palabras[palabra] = contador_de_palabras.get(palabra, 0) + 1
    contadores.append(contador_de_palabras)

    print(f"\nPalabras y repeticiones en el texto {i}:")
    for palabra, repeticiones in contador_de_palabras.items():
        print(f"{palabra}: {repeticiones}")

palabras_comunes = encontrar_palabras_comunes(contadores)

if palabras_comunes:
    print("\nPalabras que aparecen en todos los textos:")
    frecuencias_palabras_comunes = {}
    for palabra in palabras_comunes:
        frecuencias_palabras_comunes[palabra] = sum(contador.get(palabra, 0) for contador in contadores)
    for palabra, frecuencia in frecuencias_palabras_comunes.items():
        print(f"{palabra}: {frecuencia}")
else:
    print("\nNo hay palabras que aparezcan en todos los textos")
