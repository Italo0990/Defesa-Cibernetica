log = '192.168.1.10 - - [08/Sep/2024:14:23:45 -0300] "GET /index.html HTTP/1.1" 200 1024'

print(f'Acesso do {log[:13]} em {log[19:30]}')