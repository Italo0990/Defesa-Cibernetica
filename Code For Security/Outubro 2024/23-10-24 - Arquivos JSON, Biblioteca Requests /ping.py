import os

host = input('Digite o IP/URL: ')
# os.system(f'ping -n 1 {host}')
comando = f'ping -n 1 {host}'
print(comando)


resposta = os.popen(comando)


if 'Recebidos = 1' in resposta.read():
    print(f'{host} UP')
else:
    print(f'{host} DOWN')