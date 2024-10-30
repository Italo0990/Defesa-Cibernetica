''''CLIENT'''

import socket

host = '192.168.56.1'
port = 8000

lista = [x for x in 'ABCDE']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    for letra in lista:
        s.sendall(letra.encode())
        input()
        data = s.recv(1024)
        print(f'{data.decode()}')

    car =  int(input('Digite quantos caracteres na senha: '))
    s.sendall(car.encode())

    # s.sendall(b'Teste CLient')
    # data = s.recv(1024)
    # print(f'{data.decode()}')