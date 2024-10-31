import socket
import sys

#PORT SCAN

host, port = sys.argv[1], int(sys.argv[2])

print(host,port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(0.5)


    try:
        s.connect((host, port))
        print(f'[OPEN] Portal {port}')
    except:
        print(f'[CLOSED/FILTRED] Porta {port}')   