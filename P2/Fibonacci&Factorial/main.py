# ------------------------------------------------------------------------------ FIBONACCI

# def fibonacci(n):
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a + b
#     print()


# if __name__ == '__main__':
#     fibonacci(int(input('Enter a number: ')))

# ------------------------------------------------------------------------------ WITHOUT RECURSION


# ------------------------------------------------------------------------------ WITH RECURSION
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# if __name__ == '__main__':
#     limit = int(input('Enter a number: '))
#     print(fibonacci(limit))


# ------------------------------------------------------------------------------ FACTORIAL
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# if __name__ == '__main__':
#     limit = int(input('Enter a number: '))
#     print(factorial(limit))

# ------------------------------------------------------------------------------ WITH RECURSION

# SANDGLASS
# draw sandglass with recursion

def sandglass(n):
    if n == 0:
        return
    else:
        print('❤' * n, align='center')
        sandglass(n - 2)
        print('❤' * n, align='center')


if __name__ == '__main__':
    sandglass(int(input('Enter a number: ')))
