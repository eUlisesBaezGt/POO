from Classes.Boat import Boat, create_weapon

battleships = []


def create_main_weapon_battleship():
    li = 10000
    ls = 1000000
    bullets = create_weapon(li, ls)
    return bullets


def create_secondary_weapon_battleship():
    li = 1000
    ls = 10000
    bullets = create_weapon(li, ls)
    return bullets


class Battleship(Boat):

    def __init__(self):
        super().__init__()
        self.main_weapon = create_main_weapon_battleship()
        self.secondary_weapon = create_secondary_weapon_battleship()
        self.type = "Battleship"

    def main_shoot(self, f_secs):
        if self.main_weapon > 0:
            spend = round(f_secs * 500)
            self.main_weapon -= spend


def secondary_shoot(self, f_secs):
    if self.secondary_weapon > 0:
        spend = f_secs * 50
        spend = round(spend)
        self.secondary_weapon -= spend
