username, password = 'usuario', 'senha'

# usuario = input('Digite seu login: ')
# senha = input('Digite sua senha: ')

# admin = int(input('1-Admin/0-Comum')) 
usuario = []
usuario.append(input('Digite seu login: '))
usuario.append(input('Digite sua senha: '))
usuario.append(int(input('1-Admin/0-Comum: '))) #simular retorno de alguma rotina

print(usuario)
if username == usuario[0] and usuario[1] == password:
    match usuario[2]:
        case 1:
            print(f'Bem vindo a pagina, {usuario[0]} admin')
        case 0:
            print(f'Bem vindo a pagina  {usuario[0]}')
        case _:
            print('PANE')
    # if admin:
    #     print('Bem vindo a pagina,  admin')
    # else:
    #     print('Bem vindo a pagina')
else:
    print('Dados incorretos')