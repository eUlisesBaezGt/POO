texto = input("Ingresa tu texto: ").lower()

def contar_palabras(texto):
    palabras = texto.split(" ")
    return len(palabras)

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
letras = list(texto)

def contar_vocales(texto):
    for letra in letras:
        if letra in vocales:
            vocales[letra] += 1

num_palabras = contar_palabras(texto)
print(f"El número de palabras es {num_palabras}\n")

contar_vocales(texto)
print("Contador de vocales:")
print(vocales)
