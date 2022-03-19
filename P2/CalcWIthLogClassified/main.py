import time
import json

dict_data = {
    "addition": [],
    "subtraction": [],
    "multiplication": [],
    "division": [],
}


def dump(line, opt):
    save(line)
    dict_data[opt].append(line)
    with open('hist.json', 'w') as hist:
        json.dump(dict_data, hist)


def load():
    with open('hist.json', 'r') as hist:
        dict_data = json.load(hist)



def clear_console():
    import os
    def clear(): os.system('cls')
    clear()


def save(line):
    hist = open('hist.txt', 'a')
    hist.write(line + "\n")
    hist.close()
    print("Saved successfully.")
    clear_console()


def main():
    print("""
        🖩 KIKIN CALCULATOR 🖩
        -------------------------------------------------
    """)

    while True:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        print("""
            + ) Addition
            - ) Subtraction
            * ) Multiplication
            / ) Division
            E ) Exit
        """)

        opt = input("Enter the symbol of your choice: ")

        if opt == "+":
            addition(x, y)
            time.sleep(2)
            clear_console()

        elif opt == "-":
            subtraction(x, y)
            time.sleep(2)
            clear_console()

        elif opt == "*":
            multiplication(x, y)
            time.sleep(2)
            clear_console()

        elif opt == "/":
            division(x, y)
            time.sleep(2)
            clear_console()

        elif opt == "E":
            print("\nExiting...")
            time.sleep(3)
            break

        else:
            print("\nInvalid option. Try again.")
            time.sleep(3)
            clear_console()
            continue


def addition(x, y):
    load()
    res = x + y
    line = "{} + {} = {}".format(x, y, res)
    print(line)
    opt = "addition"
    dump(line, opt)


def subtraction(x, y):
    load()
    res = x - y
    line = "{} - {} = {}".format(x, y, res)
    print(line)
    opt = "subtraction"
    dump(line, opt)


def multiplication(x, y):
    load()
    res = x * y
    line = "{} * {} = {}".format(x, y, res)
    print(line)
    opt = "multiplication"
    dump(line, opt)


def division(x, y):
    load()
    res = x / y
    line = "{} / {} = {}".format(x, y, res)
    print(line)
    opt = "division"
    dump(line, opt)


if __name__ == "__main__":
    main()
