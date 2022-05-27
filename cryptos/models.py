import requests
from cryptos import URL_TASA_ESPECIFICA 
from cryptos.errors import APIError

class CriptoValorModel:
    def __init__(self, apikey, origen = "", destino = ""):
        self.origen = origen
        self.destino = destino
        self.apikey = apikey
        self.tasa = 0.0

    def obtener_tasa(self):
        respuesta = requests.get(URL_TASA_ESPECIFICA.format(
            self.origen,
            self.destino,
            self.apikey
        ))

        if respuesta.status_code != 200:
            #El codigo de la linea 21 es el mismo que el de la linea 22
            #raise APIError(respuesta.status_code, respuesta.json()["error"])
            raise APIError(respuesta.status_code)
        
        self.tasa = round(respuesta.json()["rate"], 2)



        