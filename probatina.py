import requests

#Prueba para revisar la tasa de cambio actual de BTC (Bitcoin), se compara con USD por defecto
respuesta = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC?apikey=C87220DC-4A09-4D8E-B11B-EE898282AAA0")

#Muestra el codigo que arroja CoinAPI, 200 = Bueno
print(respuesta.status_code)

data = respuesta.json()

#Muestra la tasa de cambio
print(data["rates"][3]["rate"])