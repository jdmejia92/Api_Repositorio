from cryptos import MONEDAS

muestra_api_key = "C87220DC-4A09-4D8E-B11B-EE898282AAA0"

class CriptoValorView:
    def __init__(self):
        self.origen = ""
        self.destino = ""
        self.key = ""

    def pedir(self):
        key = input("Ingresa tu APIkey: ")
        while len(key) != 36:
            print("La APIkey introducida no es correcta")
            key = input("Ingresa tu APIKey: ")
        
        self.key = key

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