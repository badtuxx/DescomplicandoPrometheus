import requests
import json
import time
from prometheus_client import start_http_server, Gauge

url_numero_pessoas = 'http://api.open-notify.org/astros.json'
url_local_ISS = 'http://api.open-notify.org/iss-now.json'


def pega_local_ISS():
    try:
        """
        Pegar o local da estação espacial internacional
        """
        response = requests.get(url_local_ISS)
        data = response.json()
        return data['iss_position']
    except Exception as e:
        print("Não foi possível acessar a url!")
        raise e

def pega_numero_astronautas():
    try:
        """
        Pegar o número de astronautas na estação espacial internacional
        """
        response = requests.get(url_numero_pessoas)
        data = response.json()
        return data['number']
    except Exception as e:
        print("Não foi possível acessar a url!")
        raise e

def atualiza_metricas():
    try:
        """
        Atualiza as métricas com o número de astronautas e local da estação espacial internacional
        """
        numero_pessoas = Gauge('numero_de_astronautas', 'Número de astronautas na Estação Espacial Internacional')
        longitude = Gauge('longitude_ISS', 'Longitude da Estação Espacial Internacional')
        latitude = Gauge('latitude_ISS', 'Latitude da Estação Espacial Internacional')

        while True:
            numero_pessoas.set(pega_numero_astronautas())
            longitude.set(pega_local_ISS()['longitude'])
            latitude.set(pega_local_ISS()['latitude'])
            time.sleep(10)
            print("O número atual de astronautas na Estação Espacial é: %s" % pega_numero_astronautas())
            print("A longitude atual da Estação Espacial Internacional é: %s" % pega_local_ISS()['longitude'])
            print("A latitude atual da Estação Espacial Internacional é: %s" % pega_local_ISS()['latitude'])
    except Exception as e:
        print("Problemas para atualizar as métricas! \n\n====> %s \n" % e)
        raise e
        
def inicia_exporter():
    try:
        """
        Iniciar o exporter
        """
        start_http_server(8899)
        return True
    except Exception as e:
        print("O Servidor não pode ser iniciado!")
        raise e


def main():
    try:
        inicia_exporter()
        print('Exporter Iniciado')
        atualiza_metricas()
    except Exception as e:
        print('\nExporter Falhou e Foi Finalizado! \n\n======> %s\n' % e)
        exit(1)


if __name__ == '__main__':
    main()
    exit(0)
