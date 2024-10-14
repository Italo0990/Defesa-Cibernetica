
# nome = input('Digite o nome: ')

# file = open('test.txt', 'w')
# file.write(nome)
# file.close()


# file = open('test.txt', 'a')
# file.write(f'{nome}\n')
# file.close

# with open('test.txt', 'r') as file:
#     linhas = file.readlines()
#     print(linhas)


# with open('test.txt', 'r') as file:
#     for linha in file.readlines():
#         print(linha.rstrip())


# with open('test.txt', 'r') as file:
#      for linha in file:
#           print(linha.rstrip())


# nome = []

# with open('test.txt') as file:
#      for linha in file:
#           nome.append(linha.rstrip())


# print(nome)
# for n in sorted(nome):
#      print('ola', n)


# with open('test.txt') as file:
#     for linha in sorted(file):
#         print('Olá', linha.rstrip())

# try:
#     with open('C:\\outrapasta\\test.txt') as file:
#         # print(file.read(10))
#         # print(file.readlines(3))
#         print(file.readline())
#         print(file.readline())
# except FileNotFoundError:
#     print('Arquivo não existe')


with open('capa.jpg', 'rb') as cape:
    content = cape.read()

with open('capa_copia.jpg', 'wb') as copia:
    copia.write(content)

