from Felidae import *

# lion = Lion("Simba", "Savannah", "Mufasa", "Nala", 8, 500, 1.5, "Africa", 50)
#  tiger = Tiger("Richard Parker", "Jungle", "Diego", "Tigress", 7, 300, 1.2, "Asia", 40)
#  panther = Panther("Bagheera", "Swamp", "Lucifer", "Felicia", 15, 400, 1.4, "America", 30)
#  cheetah = Cheetah("Azad", "Sub-saharan africa", "Rocky", "Cybil", 10, 200, 1.1, "Africa", 80)
#  cougar = Cougar("P-22", "Scrub", "Zeus", "Stella", 13, 350, 1.25, "America", 60)

felines = []


def create_feline():
    print("1) Lion")
    print("2) Tiger")
    print("3) Panther")
    print("4) Cheetah")
    print("5) Cougar")
    print("R) Return to main menu")
    opt = input("Please select an option: ")

    if opt.isdigit():
        opt = int(opt)
        if opt == 1:
            print("You choose Lion")
            Lion.create()
        elif opt == 2:
            print("You choose Tiger")
            Tiger.create()
        elif opt == 3:
            print("You choose Panther")
            Panther.create()
        elif opt == 4:
            print("You choose Cheetah")
            Cheetah.create()
        elif opt == 5:
            print("You choose Cougar")
            Cougar.create()

    elif opt == "R":
        pass

    else:
        print("Invalid option")


def menu():
    while True:
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
                show_feline()

        elif opt == "E":
            break

        else:
            print("Invalid option")
            continue


menu()
