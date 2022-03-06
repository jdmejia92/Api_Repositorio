from cryptos import MONEDAS
from cryptos import URL_TASA_ESPECIFICA
import requests

class CriptoValorView:
    def __init__(self):
        self.origen = ""
        self.destino = ""
        self.key = ""

    def pedir(self):
        key = input("Ingresa tu APIkey: ")
        while len(key) != 36:
            print("La APIKey no es correcta")
            key = input("Ingresa tu APIKey: ")
        confirmacion = requests.get(URL_TASA_ESPECIFICA. format("BTC","EUR",key))
        while confirmacion.status_code == 401:
            print("La APIKey no es valida")
            key = input("Ingresa tu APIKey: ")
            confirmacion = requests.get(URL_TASA_ESPECIFICA. format("BTC","EUR",key))

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