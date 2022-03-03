class Felidae:
    def __init__(self, name, habitat, father, mother, food, weight, height, zone, speed):
        self.name = name
        self.habitat = habitat
        self.__father = father  # private
        self.__mother = mother  # private
        self.food = food  # M
        self.__weight = weight  # private
        self.__height = height  # private
        self.zone = zone  # M
        self.__speed = speed  # private

        self.__sleep = False  # private # M
        self.__check = False  # private # M
        self.__sterilize = False  # private # M

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

    def create(self):
        self.name = input("Name: ")
        self.habitat = input("Habitat: ")
        self.__father = input("Father: ")
        self.__mother = input("Mother: ")
        self.food = input("Food: ")
        self.__weight = input("Weight: ")
        self.__height = input("Height: ")
        self.zone = input("Zone: ")
        self.__speed = input("Speed: ")

    def show(self):
        print("Name: {}\t".format(self.name), "Habitat: {}\t".format(self.habitat),
              "Father: {}\t".format(self.__father),
              "Mother: {}\t".format(self.__mother), "Food: {}\t".format(self.food),
              "Weight: {}\t".format(self.__weight), "Height: {}\t".format(self.__height),
              "Zone: {}\t".format(self.zone), "Speed: {}\t".format(self.__speed), "Sleep: {}\t".format(self.__sleep),
              "Check: {}\t".format(self.__check), "Sterilize: {}\t".format(self.__sterilize))

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


class Lion(Felidae):
    def __init__(self, name, habitat, father, mother, food, weight, height, zone, speed):
        super().__init__(name, habitat, father, mother, food, weight, height, zone, speed)


class Tiger(Felidae):
    def __init__(self, name, habitat, father, mother, food, weight, height, zone, speed):
        super().__init__(name, habitat, father, mother, food, weight, height, zone, speed)


class Panther(Felidae):
    def __init__(self, name, habitat, father, mother, food, weight, height, zone, speed):
        super().__init__(name, habitat, father, mother, food, weight, height, zone, speed)


class Cheetah(Felidae):
    def __init__(self, name, habitat, father, mother, food, weight, height, zone, speed):
        super().__init__(name, habitat, father, mother, food, weight, height, zone, speed)


class Cougar(Felidae):
    def __init__(self, name, habitat, father, mother, food, weight, height, zone, speed):
        super().__init__(name, habitat, father, mother, food, weight, height, zone, speed)
