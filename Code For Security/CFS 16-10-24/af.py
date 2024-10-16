import sys

# print(sys.argv)

args = sys.argv

# print(f'Nome do arquivo: {sys.argv[0]}')
# print('Argumentos: ')

# for arg in args[1:]:
#     print(arg)


if len(sys.argv) != 3:
    sys.exit('São necessários dois números')

def soma(x,y):
    return int(x) + int(y)

print(f'SOMA: {soma(sys.argv[1], sys.argv[2])}')
