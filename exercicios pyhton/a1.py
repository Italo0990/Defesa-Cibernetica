a = (5, 6, 7, 8)
b = (10, 20, 30, 40)

num = int(input('Digite um número: '))

for n in a:
    for nn in b:
        resultado = nn * n
        print(f'{a} + {b} = {resultado}')
        print(f'{a} - {b} = {resultado}')
        print(f'{a} * {b} = {resultado}')
        print(f'{a} / {b} = {resultado}')