'''SERVIDOR'''

import socket

host = '192.168.56.1'
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen()

con, end = s.accept()

while True:
    msg = con.recv(1024)
    if not msg:
        con.close()
        break
    print(f'[RECEBIDO] {end}: {msg.decode()}')
    con.sendall(f'[MSG RECEBIDA] {host}:{port}'.encode())

s.close()