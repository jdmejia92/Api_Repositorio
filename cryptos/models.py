import requests
from cryptos import URL_TASA_ESPECIFICA 
from cryptos.errors import APIError
from cryptos.config import API_KEY

class CriptoValorModel:
    def __init__(self, origen = "", destino = "", key = ""):
        self.origen = origen
        self.destino = destino
        self.key = key
        self.tasa = 0.0

    def obtener_tasa(self):
        respuesta = requests.get(URL_TASA_ESPECIFICA.format(
            self.origen,
            self.destino,
            API_KEY
        ))

        if respuesta.status_code != 200:
           raise APIError(respuesta.status_code, respuesta.json()["error"])
        
        self.tasa = round(respuesta.json()["rate"], 2)



        