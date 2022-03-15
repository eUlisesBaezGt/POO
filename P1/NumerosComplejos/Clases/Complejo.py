class Complejo:

    def __init__(self):
        self.__Real = 0.0
        self.__Imag = 0.0

    @property
    def real(self):
        return self.__Real

    @real.setter
    def real(self, r):
        self.__Real = r

    @property
    def imag(self):
        return self.__Imag

    @imag.setter
    def imag(self, i):
        self.__Imag = i

    def separar(self, com):
        sep = com.split('/')
        for x in range(len(sep)):
            if "i" in sep[x]:
                temp = "0"
                if len(sep[x]) == 2 and sep[x][0] == "-":
                    temp = "-1"
                elif len(sep[x]) == 2 and sep[x][0] == "+":
                    temp = "1"
                elif len(sep[x]) > 1:
                    temp = sep[x]
                else:
                    temp = "1"
                temp = temp.replace("i", "").replace("+", "")
                self.__Imag = float(temp)
            else:
                self.__Real = float(sep[x])
