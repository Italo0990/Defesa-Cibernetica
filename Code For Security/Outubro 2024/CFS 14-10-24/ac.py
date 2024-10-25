# Acesse o arquivo access_log com informações de logs do apache.
# Exiba uma lista e quantidade de IPS únicos que 
# acessaram o servidor durante o período 

with open('access_log') as logs:
    #podemos iterar sobre o logs ou sobre o readlines
    for log in logs:
    #for log in logs.readlines():
        #Agora usamos split para separar os campos do log na linha
        linha = log.split()
        #prevenimos erro de linha em branco verificando se ela é uma lista valida
        if linha:
            #add a linha ao conjunto
            ips.add(linha[0])

print(ips)
print(len(ips)) #para sabermos a quantidade de IPs
