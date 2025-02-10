import os

# print(os.name)
# print(os.getlogin())

# os.system('cls')
# os.system('ipconfig')


# processos = os.popen('tasklist')
# print(processos.read())


with open('aula.txt') as file:
    # print(file.read())
    for x, linha in enumerate(file,1):
        print(x,linha,end='')