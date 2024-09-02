print ('Atividade 3 - Code For Security\n')

usr = 'User'
pss = 123

usr = input('Digite o usuário: ')
if usr == 'User':
    pss = int(input('Digite sua senha: '))
else:
    print('Usuário Inválido!')
    
    pss = input('Digite sua senha: ')
if pss == 123:
    print('Acesso liberado!')
else:
    print('Senha Inválido!')