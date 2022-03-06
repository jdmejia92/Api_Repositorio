import requests
from cryptos import URL_TASA_ESPECIFICA 
from cryptos.errors import APIError

class CriptoValorModel:
    def __init__(self, origen = "", destino = "", key = ""):
        self.origen = origen
        self.destino = destino
        self.key = key
        self.tasa = 0.0

    def obtener_tasa(self):
        self.respuesta = requests.get(URL_TASA_ESPECIFICA. format(
            self.origen,
            self.destino,
            self.key
        ))

        if self.respuesta.status_code != 200:
           raise APIError(self.respuesta.json()["error"])
        
        self.tasa = round(self.respuesta.json()["rate"], 2)



        