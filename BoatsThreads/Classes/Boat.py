import random
import threading as th


def create_weapon(li, ls):
    bullets = random.randint(li, ls)
    return bullets


def generar_id():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    id_generado = ""
    n = 0
    while n < 3:
        id_generado += random.choice(chars)
        n += 1
    return id_generado


def stop_shooting():
    th.cancel()


class Boat:
    name = ""
    __crew = 0  # private
    fuel = 100
    __coordinates = ""  # private
    destination = ""
    speed = 50
    main_weapon = ""
    secondary_weapon = ""
    extras = ""

    __engine_status = False  # private # M

    @property
    def crew(self):
        return self.__crew

    @crew.setter
    def crew(self, new_crew):
        self.__crew = new_crew

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, new_coordinates):
        self.__coordinates = new_coordinates

    @property
    def engine_status(self):
        return self.__engine_status

    @engine_status.setter
    def engine_status(self, status):
        self.__engine_status = status

    def __init__(self):
        self.id = generar_id()
        i = input("Complete data? (y/n): ")
        if i == "y":
            self.complete_data()

    def complete_data(self):
        self.name = input("Name: ")
        self.crew = int(input("Crew: "))
        self.fuel = float(input("Fuel: "))
        self.coordinates = input("Coordinates: ")
        self.destination = input("Destination: ")
        self.speed = float(input("Speed: "))
        self.extras = input("Extras: ")

    def increase_speed(self):
        if self.engine_status:
            self.speed += 2
            print("Speed increased to {}".format(self.speed))
        else:
            print("The engine is off")

    def decrease_speed(self):
        if self.engine_status:
            self.speed -= 2
            if self.speed < 0:
                self.speed = 0
            print("Speed decreased to {}".format(self.speed))
        else:
            print("The engine is off")

    def turn_on_engine(self):
        if self.fuel > 0:
            if not self.engine_status:
                self.engine_status = True
                print("The engine is on")
            else:
                print("The engine is already on")
        else:
            print("Not enough fuel")

    def turn_off_engine(self):
        if self.engine_status:
            self.engine_status = False
            print("The engine is off")
        else:
            print("The engine is already off")

    def show(self):
        print("Name: {}\t".format(self.name), "Crew: {}\t".format(self.crew), "Fuel: {}\t".format(self.fuel),
              "Coordinates: {}\t".format(self.coordinates), "Destination: {}\t".format(self.destination),
              "Speed: {}\t".format(self.speed), "Main weapon: {}\t".format(self.main_weapon),
              "Secondary weapon: {}\t".format(self.secondary_weapon), "Extras: {}\t".format(self.extras),
              "Engine status: {}".format(self.engine_status))
