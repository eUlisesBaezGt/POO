from Classes.Battleship import *
from Classes.Cruiser import *
from Classes.Destroyer import *

fleet = []


def create_ship():
    print("-------------CREATE SHIP----------------")
    print("1) Battleship")
    print("2) Destroyer")
    print("3) Cruiser")
    print("R) Return to main menu")
    opt2 = input("Please select a type: ")
    if opt2.isdigit():
        opt2 = int(opt2)
        if opt2 == 1:
            print("Battleship selected")
            fleet.append(Battleship())
        elif opt2 == 2:
            print("Destroyer selected")
            fleet.append(Destroyer())
        elif opt2 == 3:
            print("Cruiser selected")
            fleet.append(Cruiser())
    elif opt2 == "R":
        pass
    else:
        print("Invalid option")
        return


def show_fleet():
    print("-------------SHOW FLEET----------------")
    if len(fleet) == 0:
        print("No boats in the fleet")
    else:
        for boat in fleet:
            boat.show()


def show_specific_boat():
    print("-------------SHOW SPECIFIC BOAT----------------")
    name = input("Please enter the name of the ship: ")
    for boat in fleet:
        if boat.name == name:
            boat.show()
            break
    else:
        print("Boat not found")


def actions():
    while actions != "R":
        print("-------------ACTIONS----------------")
        print("1) Start engine")
        print("2) Stop engine")
        print("3) Increase speed")
        print("4) Decrease speed")
        print("5) Shoot main weapon")
        print("6) Shoot secondary weapon")
        print("R) Return to main menu")
        return input("Please select an action: ")


def boats_to_war():
    print("-------------BOATS TO WAR----------------")
    for boat in range(len(fleet)):
        print(str(boat + 1) + ") " + fleet[boat].name + "\n")

    opt2 = input("Select your boat: ")
    i = int(opt2) - 1

    if i < 0 or i >= len(fleet):
        print("Invalid option")
        return
    a = ""
    while a != "R":
        a = actions()
        if a == "1":
            fleet[i].turn_on_engine()
        elif a == "2":
            fleet[i].turn_off_engine()
        elif a == "3":
            fleet[i].increase_speed()
        elif a == "4":
            fleet[i].decrease_speed()
        elif a == "5":
            fleet[i].main_shoot()
        elif a == "6":
            fleet[i].secondary_shoot()


def open_fire():
    if len(fleet) == 0:
        print("No boats in the fleet")
        return
    for boat in fleet:
        boat.thread_shoot()


def stop_fire():
    if len(fleet) == 0:
        print("No boats in the fleet")
        return
    for boat in fleet:
        boat.stop_shooting()


def menu():
    while True:
        print("-------------MAIN MENU----------------")
        print("1) Create ship")
        print("2) Show all boats")
        print("3) Show specific boat")
        print("4) Get boats to War")
        print("5) Open fire")
        print("6) Stop fire")
        print("E) Exit")
        opt = input("Please select an option: ")
        if opt.isdigit():
            opt = int(opt)
            if opt == 1:
                create_ship()
            elif opt == 2:
                show_fleet()
            elif opt == 3:
                show_specific_boat()
            elif opt == 4:
                boats_to_war()
            elif opt == 5:
                open_fire()
            elif opt == 6:
                stop_fire()
        elif opt == "E":
            print("Program ended")
            break
        else:
            print("Invalid option")
            continue


if __name__ == "__main__":
    menu()
