# FIBONACCI
# ------------------------------------------------------------------------------ WITH RECURSION
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# FACTORIAL
# ------------------------------------------------------------------------------ WITH RECURSION
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# SANDGLASS
# ------------------------------------------------------------------------------ WITH RECURSION
def sandglass(spaces, limit, char):
    if not (char.endswith(" ")):
        char += " "

    if limit <= 0:
        pass

    elif limit == 1:
        print(" " * spaces + char)

    else:
        print(" " * spaces + char * limit)
        sandglass(spaces + 2, limit - 2, char)
        print(" " * spaces + char * limit)


if __name__ == '__main__':
    print("-------FACTORIAL-------")
    limit = int(input('Enter a number: '))
    print(factorial(limit))

    print("-------FIBONACCI-------")
    limit = int(input('Enter a number: '))
    print(fibonacci(limit))

    print("-------SANDGLASS-------")
    print("Works with *, +, -, /, ★, ✺, ✤, ❄, ✈, ©, ✉, ♫, ♚, ♜, ♠, ♣, ♥")
    sandglass(5, 7, input('Enter a character: '))

#%%
