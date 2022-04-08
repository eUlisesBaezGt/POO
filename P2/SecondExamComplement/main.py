from Files import *

# Han pedido tu ayuda para procesar los datos de transacciones bancarias y poder realizar una auditoría.
# ------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    read_file()
    print_analysis()
    print_currency_amount()

    # ------------------------------------------------------------------------------------------------------
    # SI FUNCIONA IMPRIMIR EL KEY, Y DESPUÉS, El OBJETO
    # print all keys and all balances from the dictionary
    for key, value in dict_transactions.items():
        print(key, value)
