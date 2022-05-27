from cryptos.models import CriptoValorModel
from cryptos.view import CriptoValorView
from cryptos.errors import APIError
from cryptos.config import API_KEY

vista = CriptoValorView()
vista.pedir()

#Hace falta la API_KEY, no se agrega para probar la funcion try except de python
cvm = CriptoValorModel(vista.origen, vista.destino)

try:
    cvm.obtener_tasa()
    print(cvm.tasa)

except APIError:
    print("No se puede calcular la tasa")