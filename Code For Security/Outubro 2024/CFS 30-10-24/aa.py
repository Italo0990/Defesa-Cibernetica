'''THREAD'''

import threading
import time
import random

def correr(carro):
    distancia = 0
    while distancia < 20:
        distancia += 1
        time.sleep(random.uniform(0,1.5))
        print(f'{carro} correu a distancia {distancia} KM')


carro1 = threading.Thread(target=correr, args=('Ford Mustang',))
carro2 = threading.Thread(target=correr, args=('GM Opala',))

carro1.start()
carro2.start()

correr()