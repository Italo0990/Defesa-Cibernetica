import os

dir_atual = os.getcwd()
print(dir_atual)

# lista_path = dir_atual.split('\\')
# print(lista_path)
# print(len(lista_path))


# with open('aula4.sh') as file:
#     print(file.read())

# os.chdir('C:\\Users\\Majo Nobre\\Desktop')

# with open('aula4.sh') as file:
#     print(file.read())

# print(os.getcwd())


# lista_dir = os.listdir(os.getcwd())
# print(lista_dir)

# for x in lista_dir:
#     print('*',x)

# os.makedirs('NOVO')

# with open('NOVO\\test.txt', 'w') as file:
#     file.write('Nova pasta')


# with open('born_to_die.txt', 'w') as file:
#     file.write('qq coisa')

# os.remove('born_to_die.txt')

# os.rename('aula.txt', 'aula1.txt') 


print(os.path.exists('aula.txt'))
print(os.path.exists('NOVO'))

print(os.path.isfile('aula.txt'))
print(os.path.isfile('NOVO'))

print(os.path.isfile('access_log.txt'))
print(os.path.isdir('NOVO'))

novo_path = os.path.join('C:\\Windows', 'System32', 'drivers', 'etc')
print(novo_path)

os.chdir(novo_path)

with open('hosts') as hosts:
    print(hosts.read())