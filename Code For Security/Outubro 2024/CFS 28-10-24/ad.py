import socket
import sys

#IMPORT SOCKET

host = input('Digite o alvo: ')
portal_inicial = int(input('Digite a porta inicial: '))
portal_final = int(input('Digite a porta final: '))

for porta in range(portal_final, portal_final +1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)


    try:
        s.connect((host, porta))
        print(f'[OPEN] Portal {porta}')
    except:
        print(f'[CLOSED/FILTRED] Porta {porta}')   