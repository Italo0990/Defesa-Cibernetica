idade = 23

import os

def menu():
    num = int(input('Digite uma idade: '))

    if num >= idade and num < 65:
        print(f'Essa idade é maior que {idade} anos\n')
        input('Digite uma tecla para voltar')
        main()
    elif num >= 65:
        print(f'Essa idade é muito maior do que {idade} anos\n')
        input('Digite uma tecla para voltar')
        main()
    else:
        print(f'Essa idade é menor que {idade} anos\n')
        input('Digite uma tecla para voltar')
        main()


def main():
    os.system('cls')
    menu()


if __name__ == '__main__':
    main()