lista = [
   [],
   []
]

num = 0

for x in range(1,11):
   num = int(input('Digite um número: '))
   if num % 2 == 0:
    lista[0].append(num)
   else:
    lista[1].append(num)

lista[0].sort
lista[1].sort


print()
print(f'Números ímpares: {lista[0]}')
print(f'Números pares: {lista[1]}')
