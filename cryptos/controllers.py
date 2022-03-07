from sys import api_version
from cryptos.models import CriptoValorModel, APIError
from cryptos.view import CriptoValorView
from cryptos.config import API_KEY

class CriptoValorController:
    def __init__(self):
        self.vista = CriptoValorView()
        self.modelo = CriptoValorModel(API_KEY)

    def ejecutar(self):
        self.vista.pedir()
        self.modelo.origen = self.vista.origen
        self.modelo.destino = self.vista.destino
        try:
            self.modelo.obtener_tasa()
            self.vista.mostrar(self.modelo.tasa)
        except APIError as e:
            self.vista.mostrar_error(e.args[0])
