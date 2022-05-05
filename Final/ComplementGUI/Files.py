from Account import Account

# ------------------------------------------------------------------------------------------------------
# 2. Lee el archivo “ResumenBancario.txt” línea por línea. Formato de archivo:
# [0] - Los primeros 8 dígitos corresponden al número de cuenta de origen
# [1,2] - Luego aparece el nombre y apellido del titular origen
# [3] - El segundo bloque de 8 dígitos corresponde al número de cuenta de destino
# [4,5] - Luego aparece el nombre y apellido del titular de destino
# [6] - El penúltimo carácter es la moneda de la transacción, que puede estar en dólares ($), libras (£) o yenes (¥)
# [7] - El ultimo valor es el monto de la transacción

file_name = "ResumenBancario.txt"
dict_transactions = {}


def read_file():
    with open(file_name) as file:
        for line in file:
            line = line.rstrip()
            line = line.split(" ")

            o_id = line[0]
            o_name = line[1]
            o_last_name = line[2]
            new_o_name = o_name + " " + o_last_name

            d_id = line[3]
            d_name = line[4]
            d_last_name = line[5]
            new_d_name = d_name + " " + d_last_name

            currency = line[6]
            amount = line[7]
            check_currency(currency, amount)
            balance = complete_balance(currency, amount)
            # ------------------------------------------------------------------------------------------------------
            # 3. (1p) Crea un diccionario de cuentas donde cada llave del diccionario es un número de cuenta y el
            # contenido de dicha llave es un objeto de la clase Cuenta.
            # A) Los atributos número de cuenta y titular del objeto se deben extraer de forma automática del archivo
            # “ResumenBancario.txt”.
            # Check if the key exists
            if o_id in dict_transactions:
                # if the key exists, update the balance
                # discount balance from origin account
                dict_transactions[o_id].balance -= balance
            else:
                # if the key doesn't exist, create a new account
                dict_transactions[o_id] = Account(new_o_name, o_id)
                dict_transactions[o_id].balance -= balance

            if d_id in dict_transactions:
                # add balance to destination account
                dict_transactions[d_id].balance += balance
            else:
                dict_transactions[d_id] = Account(new_d_name, d_id)
                dict_transactions[d_id].balance += balance


# ------------------------------------------------------------------------------------------------------
# 4. (2p) Itera sobre cada línea del archivo “ResumenBancario.txt” y completa el balance en pesos
# mexicanos (MXN). No se requiere recursividad.
# a. El balance puede tener número negativos
# b. Deberás restar el monto de la transacción (MXN) de la cuenta origen
# c. Deberás sumar el monto de la transacción (MXN) a la cuenta de destino
# d. Conversión USD a MXN = 20.17, libra a MXN = 26.35, YEN a MXN = 0.16
# e. Puedes leer el archivo 2 veces (uno crea el diccionario y otro analiza las operaciones) o hacerlo todo en la misma
# lectura.

def complete_balance(currency, amount):
    amount = float(amount)
    if currency == "$":
        amount = amount * 20.17
    elif currency == "£":
        amount = amount * 26.35
    elif currency == "¥":
        amount = amount * 0.16
    return amount


# ------------------------------------------------------------------------------------------------------
currency_dict = {"$": 0, "£": 0, "¥": 0}


# Crea un segundo diccionario y acumula también el monto por tipo de moneda.
# Guarda estos resultados en un archivo de texto.
def check_currency(currency, amount):
    amount = float(amount)
    if currency == "$":
        currency_dict["$"] += amount
    elif currency == "£":
        currency_dict["£"] += amount
    elif currency == "¥":
        currency_dict["¥"] += amount


# ------------------------------------------------------------------------------------------------------

# 5. (1p) Imprime tus resultados en un archivo “analisis.txt” en la forma:
# [Número de cuenta] [Nombre y apellido] [balance]
# 12345678 ERNESTO ROBLES -1245.25
# 79453579 MAYRA PEREZ 458.58
def print_analysis():
    with open("analisis.txt", "w") as file:
        for key, value in dict_transactions.items():
            file.write(str(key) + " " + value.owner + " " + str(value.balance) + "\n")


# ------------------------------------------------------------------------------------------------------

def print_currency_amount():
    with open("currency_amount.txt", "w") as file:
        for key, value in currency_dict.items():
            file.write(str(key) + " " + str(value) + "\n")
