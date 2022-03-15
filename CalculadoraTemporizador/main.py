import threading as th
import time


def clear_console():
    import os
    clear = lambda: os.system('clear')
    clear()


def main():
    thread = None
    print("""
        🖩 KIKIN CALCULATOR 🖩
        -------------------------------------------------
    """)

    while True:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        print("""
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Exit
        """)

        opt = int(input("Enter your choice: "))

        if opt == 1:
            thread = th.Timer(3, addition, args=(x, y))
            thread.start()
            clear_console()
            time.sleep(4)

        elif opt == 2:
            thread = th.Timer(3, subtraction, args=(x, y))
            thread.start()
            clear_console()
            time.sleep(4)

        elif opt == 3:
            thread = th.Timer(3, multiplication, args=(x, y))
            thread.start()
            clear_console()
            time.sleep(4)

        elif opt == 4:
            thread = th.Timer(3, division, args=(x, y))
            thread.start()
            clear_console()
            time.sleep(4)

        elif opt == 5:
            print("\nExiting...")
            time.sleep(3)
            thread.cancel()
            break
        else:
            print("\nInvalid option. Try again.")
            time.sleep(3)
            clear_console()
            continue


def addition(x, y):
    res = x + y
    print("{} + {} = {}".format(x, y, res))


def subtraction(x, y):
    res = x - y
    print("{} - {} = {}".format(x, y, res))


def multiplication(x, y):
    res = x * y
    print("{} * {} = {}".format(x, y, res))


def division(x, y):
    res = x / y
    print("{} / {} = {}".format(x, y, res))


if __name__ == "__main__":
    main()
