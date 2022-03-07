import unittest
from cryptos.models import CriptoValorModel, APIError, API_KEY

class TestModel(unittest.TestCase):
    def test_debes_informar_la_apikey(self):
        global API_KEY
        API_KEY = "0"
        cv = CriptoValorModel("BTC", "EUR")

        with self.assertRaises(APIError, "401"):
            cv.obtener_tasa()

    def test_la_moneda_debe_existir(self):
        cv = CriptoValorModel("BTC", "lolailos")

        with self.assertRaises(APIError, "550"):
            cv.obtener_tasa()


            