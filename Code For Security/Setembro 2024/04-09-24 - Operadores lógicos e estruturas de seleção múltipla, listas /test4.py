print ('Atividade - Code For Security\n')

usr, pss = 'User', '123'

admin = False


usrr = input('Digite o usuário: ')
psss = input('Digite sua senha: ')

admin = int(input('1-Admin/0-Comum: '))

#usrr = []
#usrr.append(input('Digite seu login'))
#usrr.append(input('Digite sua senha'))
#usrr.append(int(input('Digite seu login')))




if usrr == usr and psss == pss:
    match admin:
        case 1:
            print('Bem vindo apágina, admin!')
        case _:
            print('Bem vindo a página!')
else:
    print ('Credenciais Inválidas!')