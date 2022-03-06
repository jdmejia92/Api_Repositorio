from cryptos.models import CriptoValorModel
from cryptos.view import CriptoValorView
from cryptos.errors import APIError

vista = CriptoValorView()
vista.pedir()

cvm = CriptoValorModel(vista.origen, vista.destino)
try:
    cvm.obtener_tasa()
    print(cvm.tasa)

except APIError:
    print("No se puede calcular la tasa")