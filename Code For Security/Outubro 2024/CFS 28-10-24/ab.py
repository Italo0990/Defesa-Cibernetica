import socket

host = '192.168.56.101'
port = 11500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((host, port))

    s.sendall(b'ENVIANDO MENSAGEM DO WINDOWS')

    data = s.recv(1024)

    print(f'[RECEBIDO] : {data.decode()}')