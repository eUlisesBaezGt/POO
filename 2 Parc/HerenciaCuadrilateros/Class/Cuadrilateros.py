class Cuadrilateros:
    def __init__(self, la, lb, lc, ld):
        self.la = la
        self.lb = lb
        self.lc = lc
        self.ld = ld

    def area(self):
        a = self.lb * self.la
        print("Area cuadrilatero--- > ", a, "u²")


class Cuadrado(Cuadrilateros):
    def __init__(self, la, lb, lc, ld):
        super().__init__(la, lb, lc, ld)

    def area_cuadrado(self):
        super().area()


class Rectangulo(Cuadrilateros):
    def __init__(self, la, lb, lc, ld):
        super().__init__(la, lb, lc, ld)

    def area_rectangulo(self):
        super().area()


class Trapecio(Cuadrilateros):

    def __init__(self, la, lb, lc, ld):
        super().__init__(la, lb, lc, ld)

    def area_trapecio(self):
        a = ((self.la + self.lb) * self.lc) / 2
        print("Area trapecio--- > ", a, "u²")
