import threading as th
from Dog import Dog

now = 0
limit = 30
alive = True
dog = Dog()


def first():
    global now, limit, alive
    dog.mk_hung()
    now = dog.hunger

    thread = th.Timer(5, first)
    thread.start()

    if now > limit:
        alive = False
        print("Dog is dead")
        thread.cancel()


first()
op = ""

while dog.hunger < limit:

    if alive:

        if dog.hunger >= 10:
            op = input("Dog is hungry {}: ... Do you want to feed it? (Y/N): ".format(dog.hunger))

            if op == "Y":
                dog.hunger -= 5
                print("HUNGER reduced to -->", dog.hunger)

            elif op == "N":
                print("Dog is still hungry {}".format(dog.hunger))

            else:
                print("Invalid input")

    else:
        print("Dog is dead")
        break
