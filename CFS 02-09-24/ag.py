print ('Atividade 3 - Code For Security\n')

usr, pss = 'User', 'adm'



usrr = input('Digite o usuário: ')
psss = input('Digite sua senha: ')


if usrr == usr and psss == pss:
     print('Acesso liberado!')
else:
     print('Credenciais Inválidas!')
