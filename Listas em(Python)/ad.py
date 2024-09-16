num = list()

for n in range(0,3):
    num.append(int(input('Digite um valor: ')))

print(f'Você digitou os números {num}\n')
for c, v in enumerate(num):

    print(f'Na posição {c} encontrei o valor {v}!', end='\n')
print('Cheguei ao final da lista')