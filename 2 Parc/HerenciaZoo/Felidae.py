import random


def generar_id():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    id_generado = ""
    n = 0
    while n < 3:
        id_generado += random.choice(chars)
        n += 1
    return id_generado


class Felidae:
    name = ""
    habitat = ""
    __father = ""  # private
    __mother = ""  # private
    food = 0  # M
    weight = 0  # M
    height = 0  # M
    zone = ""  # M
    __speed = 0  # private

    __sleep = False  # private # M
    __check = False  # private # M
    __sterilize = False  # private # M

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, father):
        self.__father = father

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, mother):
        self.__mother = mother

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if speed < 0:
            self.__speed = 0
        else:
            self.__speed = speed

    @property
    def sleep(self):
        return self.__sleep

    @sleep.setter
    def sleep(self, sleep):
        self.__sleep = sleep

    @property
    def check(self):
        return self.__check

    @check.setter
    def check(self, check):
        self.__check = check

    @property
    def sterilize(self):
        return self.__sterilize

    @sterilize.setter
    def sterilize(self, sterilize):
        self.__sterilize = sterilize

    def __init__(self):
        self.id = generar_id()
        self.special_characteristic = ""
        i = input("Complete data? (y/n): ")
        if i == "y":
            self.complete_data()

    def complete_data(self):
        self.name = input("Name: ")
        self.habitat = input("Habitat: ")
        self.father = input("Father: ")
        self.mother = input("Mother: ")
        self.food = float(input("Food: "))
        self.weight = float(input("Weight: "))
        self.height = float(input("Height: "))
        self.zone = input("Zone: ")
        self.speed = float(input("Speed: "))

    def show(self):
        print("Name: {}\t".format(self.name), "Habitat: {}\t".format(self.habitat),
              "Father: {}\t".format(self.__father),
              "Mother: {}\t".format(self.__mother), "Food: {}\t".format(self.food),
              "Weight: {}\t".format(self.weight), "Height: {}\t".format(self.height),
              "Zone: {}\t".format(self.zone), "Speed: {}\t".format(self.__speed), "Sleep: {}\t".format(self.__sleep),
              "Check: {}\t".format(self.__check), "Sterilize: {}\t".format(self.__sterilize),
              "Special characteristic: {}\t".format(self.special_characteristic))

    def m_feed(self):
        food = float(input("How much food?: "))
        self.food += food
        print("{} is eating {} kgs".format(self.name, food))

    def m_sleep(self):
        self.__sleep = True
        print("{} is sleeping".format(self.name))

    def m_transfer(self):
        n_zone = input("New zone: ")
        self.zone = n_zone
        print("{} is transferring to {}".format(self.name, n_zone))

    def m_check(self):
        if self.food >= 10:
            self.__check = True
            print("{} was checked".format(self.name))
        else:
            print("{} doesn´t need a check'".format(self.name))

    def m_sterilize(self):
        self.__sterilize = True
        print("{} is being sterilized".format(self.name))

    def update(self):
        print("1) Food")
        print("2) Sleep")
        print("3) Transfer")
        print("4) Check")
        print("5) Sterilize")
        opt = input("Select status to update: ")

        if opt.isdigit():
            opt = int(opt)
            if opt == 1:
                self.m_feed()
            elif opt == 2:
                self.m_sleep()
            elif opt == 3:
                self.m_transfer()
            elif opt == 4:
                self.m_check()
            elif opt == 5:
                self.m_sterilize()
            else:
                print("Invalid option")
        else:
            print("Invalid option")


class Lion(Felidae):
    def __init__(self):
        super().__init__()
        self.special_characteristic = "mane"


class Tiger(Felidae):
    def __init__(self):
        super().__init__()
        self.special_characteristic = "stripes"


class Panther(Felidae):
    def __init__(self):
        super().__init__()
        self.special_characteristic = "black fur"


class Cheetah(Felidae):
    def __init__(self):
        super().__init__()
        self.special_characteristic = "speed"


class Cougar(Felidae):
    def __init__(self):
        super().__init__()
        self.special_characteristic = "tawny fur"
