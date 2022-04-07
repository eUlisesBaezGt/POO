# 2. Lee el archivo “ResumenBancario.txt” línea por línea. Formato de archivo:
# [0] - Los primeros 8 dígitos corresponden al número de cuenta de origen
# [1,2] - Luego aparece el nombre y apellido del titular origen
# [3] - El segundo bloque de 8 dígitos corresponde al número de cuenta de destino
# [4,5] - Luego aparece el nombre y apellido del titular de destino
# [6] - El penúltimo carácter es la moneda de la transacción, que puede estar en dólares ($), libras (£) o yenes (¥)
# [7] - El ultimo valor es el monto de la transacción

file_name = "ResumenBancario.txt"


def read_file():
    with open(file_name, "rb") as file:
        for line in file:
            line = line.rstrip()
            # line = line.split(" ")
            print(line)

# with open(file, "r") as f:
#         lines = f.readlines()
#         for line in lines:
#             line = line.strip()
#             line = line.split("=")
#
#             # Extract area
#             line[0] = line[0].strip()
#
#             # Extract data
#             line[1] = literal_eval(line[1])
#
#             # add it as a dictionary key
#             # add the line as a value to the key
#             dict[line[0]] = line[1]


# 4. (2p) Itera sobre cada línea del archivo “ResumenBancario.txt” y completa el balance en pesos
# mexicanos (MXN). No se requiere recursividad.
# a. El balance puede tener número negativos
# b. Deberás restar el monto de la transacción (MXN) de la cuenta origen
# c. Deberás sumar el monto de la transacción (MXN) a la cuenta de destino
# d. Conversión USD a MXN = 20.17, libra a MXN = 26.35, YEN a MXN = 0.16
# e. Puedes leer el archivo 2 veces (uno crea el diccionario y otro analiza las operaciones) o hacerlo todo en la misma
# lectura.


# 5. (1p) Imprime tus resultados en un archivo “analisis.txt” en la forma:
# [Número de cuenta] [Nombre y apellido] [balance]
# 12345678 ERNESTO ROBLES -1245.25
# 79453579 MAYRA PEREZ 458.58
