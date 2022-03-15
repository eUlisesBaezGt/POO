from Classes.Boat import Boat, create_weapon
from datetime import datetime


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


    def main_shoot(self):
        c = 1
        while c == 1:
            if self.main_weapon > 0:
                t = datetime.today()
                secs = t.timestamp()
                print("Shooting main weapon")
                c = input("Press 0 to stop shooting: ")
                if c.isdigit():
                    c = int(c)
                    if c == 0:
                        t2 = datetime.today()
                        secs2 = t2.timestamp()
                        f_secs = secs2 - secs
                        print("Stopped")
                        print("Shooted main weapon for: {} seconds".format(f_secs))
                        spend = f_secs * 50
                        spend = round(spend)
                        self.main_weapon -= spend
                        if self.main_weapon < 0:
                            self.main_weapon = 0
                        print("Bullets left on main weapon: {}".format(self.main_weapon))
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
            else:
                print("No bullets left on main weapon")
                break

    def secondary_shoot(self):
        c = 1
        while c == 1:
            if self.secondary_weapon > 0:
                t = datetime.today()
                secs = t.timestamp()
                print("Shooting secondary weapon")
                c = input("Press 0 to stop shooting: ")
                if c.isdigit():
                    c = int(c)
                    if c == 0:
                        t2 = datetime.today()
                        secs2 = t2.timestamp()
                        f_secs = secs2 - secs
                        print("Stopped")
                        print("Shooted secondary weapon for: {} seconds".format(f_secs))
                        spend = f_secs * 5
                        spend = round(spend)
                        self.secondary_weapon -= spend
                        if self.secondary_weapon < 0:
                            self.secondary_weapon = 0
                        print("Bullets left on secondary weapon: {}".format(self.secondary_weapon))
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")
            else:
                print("No bullets left on secondary weapon")
                break
