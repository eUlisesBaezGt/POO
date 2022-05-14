#      Genere una clase llamada dependiente que siga las siguientes condiciones:
#     • Sus atributos son: nombre, edad, sexo(H hombre, M mujer), idEmpleado.
class Dependiente:
    __idEmpleado = ""

    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.__edad = edad
        self.sexo = sexo

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idEmpleado.setter
    def idEmpleado(self, idEmpleado):
        self.__idEmpleado = idEmpleado

    # El idEmpleado debe ser privado y solamente se podrá llenar a través del método llenarID().
    def llenarID(self):
        self.idEmpleado = input("Ingrese el ID del empleado: ")

    @property
    def edad(self):
        return self.__edad

    # La edad capturada no podrá ser menor a 18 años. Si es menor a eso se le asignará el valor de 18.
    @edad.setter
    def edad(self, edad):
        if edad < 18:
            self.__edad = 18
        else:
            self.__edad = edad

    # cobrar () Recibe como parámetro de entrada el precio del producto y el pago del cliente. Si es suficiente emite
    # un cartel que diga “El cliente pagó (pago) y hay que devolverle (pago – precio)”, de lo contrario dice
    # “No es suficiente lo cobrado para pagar el producto”.

    def cobrar(self, precio, pago):
        if pago >= precio:
            print("El cliente pagó", pago, "y hay que devolverle", pago - precio)
            self.darRecibo()
        else:
            print("No es suficiente lo cobrado para pagar el producto")

    # darRecibo() Indica que se entregó el recibo a través de un cartel.
    def darRecibo(self):
        print("Se entregó el recibo")

    # mostrarDatos(): Mostrar toda la información del objeto.
    def mostrarDatos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("ID:", self.idEmpleado)

    # Crear una subclase que herede de Dependiente y que sea Vendedor.
    # Debe tener todos los atributos y métodos de la clase Dependiente, pero además debe tener el atributo
    # dineroVentas y este debe llenarse también a través del constructor.


class Vendedor(Dependiente):
    def __init__(self, nombre, edad, sexo, dineroVentas):
        super().__init__(nombre, edad, sexo)
        self.llenarID()
        self.dineroVentas = dineroVentas

    # El método cobrar(), aparte de hacer lo mismo que en la clase Dependiente, debe acumular lo que va cobrando.
    def cobrar(self, precio, pago):
        if pago >= precio:
            print("El cliente pagó", pago, "y hay que devolverle", pago - precio)
            self.darRecibo()
            self.dineroVentas += precio
        else:
            print("No es suficiente lo cobrado para pagar el producto")


# Crear una subclase que herede de Dependiente y que sea Emisor_de_Facturas.
# Debe tener todos los atributos y métodos de la clase Dependiente, pero además debe tener el atributo pagoFactura y
# este debe llenarse también a través del constructor.
class Emisor_de_Facturas(Dependiente):
    def __init__(self, nombre, edad, sexo, pagoFactura):
        super().__init__(nombre, edad, sexo)
        self.llenarID()
        self.pagoFactura = pagoFactura

    #  El método cobrar(), aparte de hacer lo mismo que en la clase Dependiente, debe acumular lo que va cobrando y sumarle el 16 %.
    def cobrar(self, precio, pago):
        if pago >= precio:
            print("El cliente pagó", pago, "y hay que devolverle", pago - precio)
            self.darRecibo()
            self.pagoFactura += precio * 1.16


# Crear una subclase Vendedor_que_factura que herede de Vendedor y de Emisor_de_Facturas y que en pago_factura ponga por default 1,000.
# Su método cobrar() debe ser el mismo de la clase Emisor_de_Facturas.
class Vendedor_que_factura(Vendedor, Emisor_de_Facturas):

    # Crear un constructor que herede doble a las clases Vendedor y Emisor_de_Facturas.
    def __init__(self, nombre, edad, sexo, dineroVentas):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.dineroVentas = dineroVentas
        self.pagoFactura = 1000
        self.llenarID()

        # La clase Vendedor_que_factura debe tener un método facturas_especiales() que simule la sobrecarga de métodos.
        # Este método debe tener uno o dos parámetros de entrada: facturacion_especial que es un número flotante que
        # entra como parámetro de entrada y que está entre 20,000 y 100,000 y pago_extra que puede ser definido por
        # default con un 0 o ser capturado. La salida de este método es “La facturación especial de (nombre) es
        # (facturación_especial + pago_extra)”.

    def facturas_especiales(self, facturacion_especial, pago_extra=0):
        print("La facturación especial de", self.nombre, "es", facturacion_especial + pago_extra)

    # La clase Vendedor_que_factura debe tener un destructor que emita un cartel que diga “Este vendedor que factura fue eliminado”.
    def __del__(self):
        print("Este vendedor que factura fue eliminado")


# Crear un Vendedor que hereda de Dependiente y que sea Vendedor.
v1 = Vendedor("Juan", 15, "M", 0)
v1.cobrar(100, 500)
print("Dinero de ventas:", v1.dineroVentas)
v1.mostrarDatos()

# Crear un Vendedor que hereda de Dependiente y que sea Emisor_de_Facturas.
ef1 = Emisor_de_Facturas("Juan", 25, "M", 0)
ef1.cobrar(100, 500)
print("Pago de factura:", ef1.pagoFactura)
ef1.mostrarDatos()

# Crear un Vendedor que factura que hereda de Vendedor_que_factura que sea Vendedor_que_factura
vqf1 = Vendedor_que_factura("Juan", 25, "M", 0)
vqf1.cobrar(100, 500)
print("Dinero de ventas:", vqf1.dineroVentas)
print("Pago de factura:", vqf1.pagoFactura)
vqf1.mostrarDatos()
vqf1.facturas_especiales(100000)
vqf1.facturas_especiales(100000, 200)
