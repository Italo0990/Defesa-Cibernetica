'''SERVIDOR'''

import socket

host = '192.168.56.101 '
port = 11500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((host, port))
    
    s.listen()
    
    s.accept()
    
    conn, addr = s.accept()
    
    with conn:
        print(f'[CONEXÃO] Conexão de {addr}')


        while True:
            data = conn.recv(1024)
            if not data:
                break

            print(f'[MENSAGEM] {addr} : {data.decode()}')
            conn.sendall(data)
