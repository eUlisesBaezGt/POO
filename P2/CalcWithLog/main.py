import time


def clear_console():
    import os
    def clear(): os.system('cls')
    clear()


def save(line):
    hist = open('hist.txt', 'a')
    hist.write(line + "\n")
    hist.close()
    print("Saved successfully.")


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
            time.sleep(2)

        elif opt == "-":
            subtraction(x, y)
            time.sleep(2)
            clear_console()
            time.sleep(2)

        elif opt == "*":
            multiplication(x, y)
            time.sleep(2)
            clear_console()
            time.sleep(2)

        elif opt == "/":
            division(x, y)
            time.sleep(2)
            clear_console()
            time.sleep(2)

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
    res = x + y
    line = "{} + {} = {}".format(x, y, res)
    print(line)
    save(line)


def subtraction(x, y):
    res = x - y
    line = "{} - {} = {}".format(x, y, res)
    print(line)
    save(line)


def multiplication(x, y):
    res = x * y
    line = "{} * {} = {}".format(x, y, res)
    print(line)
    save(line)


def division(x, y):
    res = x / y
    line = "{} / {} = {}".format(x, y, res)
    print(line)
    save(line)


if __name__ == "__main__":
    main()
