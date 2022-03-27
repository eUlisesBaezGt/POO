# %%
# TIRE LIFE
def usage(t2, life2):
    life2 -= ((1 / 100 * (t2 - 20) ** 3) + 10)
    if life2 > 3000:
        life2 = 3000
    if life2 >= 1000:
        t2 += 1
        print("Tire life left {} in time {}".format(life2, t2))
        usage(t2, life2)
    else:
        t2 += 1
        print("Tire life left {} in time {}".format(life2, t2))
        return print("CHANGE TIRE\n\n\n")


if __name__ == '__main__':
    print("--------------- TIRE LIFE ---------------")
    t = 0
    life = 3000
    usage(t, life)


# %%
# HOUSE PRICE
def price(year, value, time):
    value = value * 1.04
    if year <= 15:
        if year < 10:
            print("Value after {} years is \t----> \t{}".format(year, value))
            time += 1
            year += 1
            price(year, value, time)
        else:
            print("Value after {} years is ----> \t{}".format(year, value))
            time += 1
            year += 1
            price(year, value, time)
    else:
        return


if __name__ == '__main__':
    print("--------------- HOUSE PRICE ---------------")
    years = 0
    ini = 15000000
    print("Initial Value (after {} years) is ----> \t{}\n".format(years, ini))
    years = 1
    time = 0
    price(years, ini, time)
