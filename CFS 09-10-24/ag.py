

# try:
#     var = input('Digite um número: ')
#     print(int(var))
# except ValueError:
#     print('ERRO - Precisa ser um número')
# else:
#     print(f'Digitou {var}')


alunos = {
    'Sarah': '20',
    'Maria': '21',
    'José': '25,0'
}

info = input('Digite um nome: ')

try:
    print(f'{info} tem {int(alunos[info])} anos de idade')
except ValueError:
    print('A idade não é válida')
except KeyError:
    print('ERRO - Não está na lista')