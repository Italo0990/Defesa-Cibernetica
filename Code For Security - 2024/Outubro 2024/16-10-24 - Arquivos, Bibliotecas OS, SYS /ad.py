import os

#EXERCICIO - crie um script com uma função que 
# receba o caminho de um diretorio como 
# argumento e conte a quantidade de arquivos
# nesse diretorio


# os.listdir('C:\\Users\\Majo Nobre\\Desktop\\CFS 16-10-24')
# print(len(os.listdir()))

def contar_palavras(dir):
    contador = 0
    for item in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,item)):
            contador += 1

    return contar_palavras

print(contar_palavras('C:\\Users\\Majo Nobre\\Desktop\\CFS 16-10-24'))
