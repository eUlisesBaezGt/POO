from Classes.Boat import Boat, create_weapon


def create_main_weapon_cruiser():
    li = 100
    ls = 10000
    bullets = create_weapon(li, ls)
    return bullets


def create_secondary_weapon_cruiser():
    li = 10
    ls = 100
    bullets = create_weapon(li, ls)
    return bullets


class Cruiser(Boat):
    def __init__(self):
        super().__init__()
        self.main_weapon = create_main_weapon_cruiser()
        self.secondary_weapon = create_secondary_weapon_cruiser()
        self.type = "Cruiser"

    def main_shoot(self, f_secs):
        if self.main_weapon > 0:
            spend = round(f_secs * 5)
            self.main_weapon -= spend

    def secondary_shoot(self, f_secs):
        if self.secondary_weapon > 0:
            spend = f_secs * 2
            spend = round(spend)
            self.secondary_weapon -= spend
