class Cuadrilateros:
    def __init__(self, la, lb, lc, ld):
        self.la = la
        self.lb = lb
        self.lc = lc
        self.ld = ld

    def area(self):
        a = self.lb * self.la
        print("Area cuadrilatero--- > ", a, "u²")

    def perimetro(self):
        p = self.la + self.lb + self.lc + self.ld
        print("Perimetro cuadrilatero--- > ", p, "u")


class Cuadrado(Cuadrilateros):
    def __init__(self, la, lb, lc, ld):
        super().__init__(la, lb, lc, ld)


class Rectangulo(Cuadrilateros):
    def __init__(self, la, lb, lc, ld):
        super().__init__(la, lb, lc, ld)


class Trapecio(Cuadrilateros):

    def __init__(self, la, lb, lc, ld):
        super().__init__(la, lb, lc, ld)

    def area_trapecio(self):
        a = ((self.la + self.lb) * self.lc) / 2
        print("Area trapecio--- > ", a, "u²")

    def perimetro_trapecio(self):
        p = (self.la + self.lb) + (2 * self.ld)
        print("Perimetro trapecio--- > ", p, "u")
