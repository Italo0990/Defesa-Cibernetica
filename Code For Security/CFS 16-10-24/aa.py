# Desafio extra no exercício 2,
# verifique qual foi o IP que acessou mais vezes o servidor


ip_acessou = dict()


with open('access_log.txt') as logs:
    for log in logs:
        linha = log.split()
        if linha:
            if linha[0] in ip_acessou:
                ip_acessou[linha[0]] += 1
            else:
                ip_acessou[linha] = 1

maior = 0

ip_maior = ''

for ip in ip_acessou:
    if ip_acessou[ip] > maior:
        ip_maior = ip
        maior = ip_acessou[ip]

print(f'O IP {ip_maior} teve {maior} acessos')