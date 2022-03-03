class Boat:
    def __init__(self, name, crew, fuel, coordinates, destination, speed, main_weapon, secondary_weapon, extras=""):
        self.name = name
        self.__crew = crew  # private
        self.fuel = fuel
        self.__coordinates = coordinates  # private
        self.destination = destination
        self.speed = speed
        self.main_weapon = main_weapon
        self.secondary_weapon = secondary_weapon
        self.extras = extras
        self.__engine_status = False  # private # M

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

    def increase_speed(self, n_speed):
        self.speed += n_speed

    def decrease_speed(self, n_speed):
        self.speed -= n_speed

    def turn_on_engine(self):
        self.engine_status = True

    def turn_off_engine(self):
        self.engine_status = False

    # dmétodos isparar arma, donde cada barco tendrá su perfil de armas y munición. Tienen diferente cadencia de
    # disparo y costo (munición, energía)


class Battleship(Boat):
    def __init__(self, name, crew, fuel, coordinates, destination, speed, main_weapon, secondary_weapon, extras=""):
        super().__init__(name, crew, fuel, coordinates, destination, speed, main_weapon, secondary_weapon, extras)


class Destroyer(Boat):
    def __init__(self, name, crew, fuel, coordinates, destination, speed, main_weapon, secondary_weapon, extras=""):
        super().__init__(name, crew, fuel, coordinates, destination, speed, main_weapon, secondary_weapon, extras)


class Cruiser(Boat):
    def __init__(self, name, crew, fuel, coordinates, destination, speed, main_weapon, secondary_weapon, extras=""):
        super().__init__(name, crew, fuel, coordinates, destination, speed, main_weapon, secondary_weapon, extras)
