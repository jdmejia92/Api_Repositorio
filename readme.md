# Consulta de valor de cryptos en tiempo actual

Programa para practicar el uso de APIs en python

Para esta prueba se utilizo el API **Coinapi**. Esta API se encarga de rastrear en tiempo real la tasa de cambio entre una criptomoneda y una moneda tradicional *(USD, EUR, etc)*

## API Key

Para poder utilizar el programa **cryptos**, primero debes pedir una APIKey a la pagina de [CoinAPI.io](https://www.coinapi.io/)

Posteriormente debes:

1. Copiar el fichero `config_template.py`, usando el siguiente comando en [powershell](https://windows-powershell.uptodown.com/windows):

```powershell
cp config_template.py config.py
```

2. Introducir tu APIKey en el nuevo fichero
```
API_KEY=<tu clave aqui>
```
3. Ejecutar el archivo fuera de la carpeta **cryptos**: **Main.py**