def fibonaaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonaaci(n - 1) + fibonaaci(n - 2)


if __name__ == '__main__':
    print(fibonaaci(10))
