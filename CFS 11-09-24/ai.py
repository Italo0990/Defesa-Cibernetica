#Crie um programa que 
# solicite ao usuário 10 
# números e ao final mostre 
# ao usuário qual o maior e qual o menor número

numeros = []

for i in range(10):
    num = int(input(f'Digite o {i + 1}º: '))
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(numeros)
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

