import requests

#Prueba para verificar que nos arroja coinapi al momento de solicitar los datos

endopoint = "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey=C87220DC-4A09-4D8E-B11B-EE898282AAA0"

moneda_from = input("Moneda de origen ")

moneda_to = input("Moneda a conseguir: ")

r = requests.get(endopoint.format(moneda_from, moneda_to))
#Imrpime la lista json completa
print(r.json())
#Muestra el codigo de estado de la solicitud, 200 = bueno
print(r.status_code)
#Muestra la tasa actual de cambio entre la moneda_from y la moneda_to
print(round(r.json()["rate"], 2))