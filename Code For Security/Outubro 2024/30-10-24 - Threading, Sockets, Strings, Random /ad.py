'''SERVIDOR CONS'''

import socket
import threading
import random
import string

host = '192.168.56.1'
port = 8000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        listen(s)

def lida_client(con,end):
    print(f'[CONEXÃO] {end}')
    with con:
        while True:
            msg = con.recv(1024)
            if not msg:
                break
            senha = gerar_senha(msg.decode())
            print(f'[RECEBIDA] {end} : {msg.decode()}')
            con.sendall(f'[MSG RECEBIDA] {host}:{port} - Sua senha: {senha}'.encode())

def listen(s):
    s.listen()
    print(f'[ESCUTANDO] {host}:{port}')

    while True:
        con, end = s.accept()
        thread = threading.Thread(target=lida_client, args=(con,end))
        thread.start()
        print(f'[CONEXÃO ATIVAS] {threading.active_count() - 1}')


def gerar_senha(caracteres):
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([random.choice(alfabeto) for _ in range(caracteres)])
    return password

main()
