from Felidae import *

# lion = Lion("Simba", "Savannah", "Mufasa", "Nala", 8, 500, 1.5, "Africa", 50)
#  tiger = Tiger("Richard Parker", "Jungle", "Diego", "Tigress", 7, 300, 1.2, "Asia", 40)
#  panther = Panther("Bagheera", "Swamp", "Lucifer", "Felicia", 15, 400, 1.4, "America", 30)
#  cheetah = Cheetah("Azad", "Sub-saharan africa", "Rocky", "Cybil", 10, 200, 1.1, "Africa", 80)
#  cougar = Cougar("P-22", "Scrub", "Zeus", "Stella", 13, 350, 1.25, "America", 60)

felines = []


def create_feline():
    print("-------------CREATE FELINE----------------")
    print("1) Lion")
    print("2) Tiger")
    print("3) Panther")
    print("4) Cheetah")
    print("5) Cougar")
    print("R) Return to main menu")
    opt2 = input("Please select a type: ")
    if opt2.isdigit():
        opt2 = int(opt2)
        if opt2 == 1:
            print("You choose Lion")
            felines.append(Lion())
        elif opt2 == 2:
            print("You choose Tiger")
            felines.append(Tiger())
        elif opt2 == 3:
            print("You choose Panther")
            felines.append(Panther())
        elif opt2 == 4:
            print("You choose Cheetah")
            felines.append(Cheetah())
        elif opt2 == 5:
            print("You choose Cougar")
            felines.append(Cougar())
    elif opt2 == "R":
        pass
    else:
        print("Invalid option")
        return


def show_felines():
    for feline in felines:
        feline.show()


def show_specific_feline():
    name = input("Please enter the name of the feline: ")
    for feline in felines:
        if feline.name == name:
            feline.show()
            break
    else:
        print("No feline found")


def menu():
    while True:
        print("-------------MAIN MENU----------------")
        print("1) Create a new feline")
        print("2) Show all felines")
        print("3) Show a specific feline")
        print("E) Exit")
        opt = input("Please select an option: ")

        if opt.isdigit():
            opt = int(opt)
            if opt == 1:
                create_feline()
            elif opt == 2:
                show_felines()
            elif opt == 3:
                show_specific_feline()

        elif opt == "E":
            break

        else:
            print("Invalid option")
            continue


menu()
