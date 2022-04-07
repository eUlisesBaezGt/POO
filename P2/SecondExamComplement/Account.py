# 1. (1p) Crea la clase Cuenta con titular, número de cuenta y balance, con getters y setter necesarios.
class Account:
    def __init__(self, owner, _id, balance):
        self.__owner = owner
        self.__id = _id
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, _id):
        self.__id = _id

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # def deposit(self, amount):
    #     self.__balance += amount
    #
    # def withdraw(self, amount):
    #     if self.__balance >= amount:
    #         self.__balance -= amount
    #     else:
    #         print("Not enough money")

# 3. (1p) Crea un diccionario de cuentas donde cada llave del diccionario es un número de cuenta y el
# contenido de dicha llave es un objeto de la clase Cuenta.
# a. Los atributos número de cuenta y titular del objeto se deben extraer de forma automática del archivo
# “ResumenBancario.txt”.
