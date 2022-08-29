import requests
import json
import time
from prometheus_client import start_http_server, Gauge

url_numero_pessoas = 'http://api.open-notify.org/astros.json'

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
        
        while True:
            numero_pessoas.set(pega_numero_astronautas())
            time.sleep(10)
            print("O número atual de astronautas na Estação Espacial é: %s" % pega_numero_astronautas())
    except Exception as e:
        print("A quantidade de astronautas não pode ser atualizada!")
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