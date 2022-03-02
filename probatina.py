import requests

respuesta = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC?apikey=C87220DC-4A09-4D8E-B11B-EE898282AAA0")

print(respuesta.status_code)

data = respuesta.json()

print(data["rates"][3]["rate"])