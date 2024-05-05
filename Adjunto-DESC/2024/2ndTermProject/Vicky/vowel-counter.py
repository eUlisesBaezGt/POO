texto = input("Ingresa texto: ").lower()

def contar_palabras(texto):
    palabras = texto.split(" ")
    num_palabras = len(palabras)
    print(f"Tienes {num_palabras} palabras")

contar_palabras(texto)

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
letras = list(texto)

def contar_vocales(letras):
    for letra in letras:
        if letra in vocales:
            vocales[letra] += 1

contar_vocales(letras)

print("Diccionario de vocales:")
for vocal, cantidad in vocales.items():
    print(f"{vocal}: {cantidad}")
