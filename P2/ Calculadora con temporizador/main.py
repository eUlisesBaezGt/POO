import threading as th


def main():
    hilo = None
    print("""
        🖩 Calculator 🖩
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
            hilo = th.Timer(3, addition, args=(x, y))
            hilo.start()

        elif opt == 2:
            hilo = th.Timer(3, subtraction, args=(x, y))
            hilo.start()

        elif opt == 3:
            hilo = th.Timer(3, multiplication, args=(x, y))
            hilo.start()

        elif opt == 4:
            hilo = th.Timer(3, division, args=(x, y))
            hilo.start()

        elif opt == 5:
            print("\nExiting...")
            hilo.cancel()
            break
        else:
            print("\nInvalid option. Try again.")
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
