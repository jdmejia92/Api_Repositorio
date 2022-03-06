from cryptos.errors import APIError
from cryptos.models import CriptoValorModel
from cryptos.view import CriptoValorView

class CriptoValorController:
    def __init__(self):
        self.vista = CriptoValorView()
        self.modelo = CriptoValorModel()

    def ejecutar(self):
        self.vista.pedir()
        self.modelo.origen = self.vista.origen
        self.modelo.destino = self.vista.destino
        self.modelo.key = self.vista.key
        self.modelo.obtener_tasa()
        self.vista.mostrar(self.modelo.tasa)

    