nome = input('Nome: ')

while not nome:
    nome = input('Nome: ')

print(nome)


######################


nome = ''

while not nome:
    nome = input('Digite o nome ou sair: ')
    if nome == 'sair':
        break

print(nome)