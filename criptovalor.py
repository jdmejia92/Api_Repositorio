import requests

endopoint = "https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey=C87220DC-4A09-4D8E-B11B-EE898282AAA0"

moneda_from = input("Moneda de origen ")

moneda_to = input("Moneda a conseguir: ")

r = requests.get(endopoint.format(moneda_from, moneda_to))
print(r.json())
print(r.status_code)
print(round(r.json()["rate"], 2))

