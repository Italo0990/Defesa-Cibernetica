# EXERCICIO Crie um script que solicite ao usuario um ip
# ou url, realize um ping e verifique se o ip ou 
# sistema está respondendo, se sim faça a consulta 
# a api mostre na tela de forma amigável os dados 
# retornados pela api 
 

host = input('Digite um IP/URL: ')

p = f'ping -n 1 google.com'
print(p)

if 'Recebidos = 1' in p.read():
    print()

