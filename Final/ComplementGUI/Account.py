# 1. (1p) Crea la clase Cuenta con titular, número de cuenta y balance, con getters y setter necesarios.

class Account:
    def __init__(self, owner, _id):
        self.owner = owner
        self.__id = _id
        self.__balance = 0.0

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
