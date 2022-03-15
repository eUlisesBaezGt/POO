from Classes.Boat import Boat, create_weapon


def create_main_weapon_destroyer():
    li = 1000
    ls = 100000
    bullets = create_weapon(li, ls)
    return bullets


def create_secondary_weapon_destroyer():
    li = 100
    ls = 1000
    bullets = create_weapon(li, ls)
    return bullets


class Destroyer(Boat):
    def __init__(self):
        super().__init__()
        self.main_weapon = create_main_weapon_destroyer()
        self.secondary_weapon = create_secondary_weapon_destroyer()
        self.type = "Destroyer"

    def main_shoot(self, f_secs):
        if self.main_weapon > 0:
            spend = f_secs * 50
            spend = round(spend)
            self.main_weapon -= spend

    def secondary_shoot(self, f_secs):
        if self.secondary_weapon > 0:
            spend = f_secs * 5
            spend = round(spend)
            self.secondary_weapon -= spend
