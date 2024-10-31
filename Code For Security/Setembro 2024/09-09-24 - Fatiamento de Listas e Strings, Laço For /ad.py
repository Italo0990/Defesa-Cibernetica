logs = [
'192.168.1.10 - - [08/Sep/2024:14:23:45 -0300] "GET /index.html HTTP/1.1" 200 1024',
'192.168.1.11 - - [08/Sep/2024:14:24:02 -0300] "POST /login HTTP/1.1" 302 512',
'192.168.1.120 - - [08/Sep/2024:14:24:15 -0300] "GET /about.html HTTP/1.1" 404 256',
'192.168.1.13 - - [08/Sep/2024:14:24:30 -0300] "GET /images/logo.png HTTP/1.1" 304 0',
'192.168.1.14 - - [08/Sep/2024:14:24:45 -0300] "DELETE /api/resource HTTP/1.1" 500 128'
]

for log in logs:
    print(log[:13])
