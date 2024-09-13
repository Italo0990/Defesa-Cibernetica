print ('Atividade 3 - Code For Security\n')

usr, pss = 'User', 'adm'



usrr = input('Digite o usuário: ')
psss = input('Digite sua senha: ')


if usrr == usr and psss == pss:
     print('Acesso liberado!')
else:
     print('Credenciais Inválidas!')



#OU TAMBÉM:



username, password = 'usuario', 'fiap'
 
usuario = input('Digite seu login: ')
senha = input('Digite sua senha: ')
 
admin = int(input('1-Admin/0-Comum'))
 
if username == usuario and senha == password:
    if admin:
        print('Bem vindo a pagina,  admin')
    else:
        print('Bem vindo a pagina')
else:
    print('Dados incorretos')

    
