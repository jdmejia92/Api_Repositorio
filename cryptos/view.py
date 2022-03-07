from cryptos import MONEDAS

class CriptoValorView:
    def __init__(self):
        self.origen = ""
        self.destino = ""
        self.key = ""

    def pedir(self):
        origen = input("Moneda origen: ")
        while origen not in MONEDAS:
            print("La moneda debe ser una de las siguientes: ")
            print(", ".join(MONEDAS))
            origen = input("Moneda origen: ")

        self.origen  = origen 

        destino = input("Moneda a convertir: ")
        while destino not in MONEDAS:
            print("La moneda debe ser una de las siguientes: ")
            print(", ".join(MONEDAS))
            destino = input("Moneda origen: ")

        self.destino = destino

    def mostrar(self, tasa):
        print("1 {} son {:.2f} {}".format(self.origen, tasa, self.destino))

    def mostrar_error(self, codigo):
        if codigo == 400:
            print("Hay algo erroneo en tu peticion")
        elif codigo == 401:
            print("No autorizado - tu APIKey es erronea")
        elif codigo == 403:
            print("Prohibido - Tu APIKey no tiene acceso a esta funcionalidad")
        elif codigo == 429:
            print("Has excedido el limite de peticiones de tu APIKey")
        elif codigo == 550:
            print("Sin datos - La moneda pedida no existe en nuestra base de datos")
        else:
            print("{}, no sabemos que error es este codigo".format(codigo))
