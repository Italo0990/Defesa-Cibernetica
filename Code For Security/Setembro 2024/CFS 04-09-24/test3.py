msg = '''
..........................
***EURO TRUCK SIMULATOR***
..........................


Menu

1 - Novo jogo
2 - Continuar
3 - Opções
4 - Sair

'''
menu = int(input(msg))

match menu:
    case 1 | 2:
        print('Bem vindo...')
    case 3:
        print('Abrindo menu de opções:')
    case 4:
        print('Saindo')
    case _:
        print('Valor Inválido')