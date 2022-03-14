import threading as th
from Dog import Dog

now = 0
limit = 30
thread = None
dog = Dog()


def hungry():
    global now, limit, thread

    dog.mk_hung()
    now = dog.hunger

    if dog.alive:
        thread = th.Timer(5, hungry)
        thread.start()

    elif not dog.alive:
        print("Dog's hunger exceeded the limit, Dog is now dead")
        thread.cancel()


hungry()
op = ""

while now < limit:

    if dog.hunger >= 10:

        op = input("Dog is hungry {}: ... Do you want to feed it? (Y/N): ".format(dog.hunger))

        if op == "Y":

            if now >= limit:
                dog.alive = False
                break

            else:
                dog.mk_feed()
                print("Hunger reduced to ---> {}".format(dog.hunger))
                now = dog.hunger

        elif op == "N":

            if now >= limit:
                dog.alive = False
                break

            else:
                print("Dog is still hungry {}".format(dog.hunger))
                now = dog.hunger

        else:
            print("Invalid input")
            now = dog.hunger
