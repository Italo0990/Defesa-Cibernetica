def somar_1(x):
    print(x)
    return x + 1

#Map - faz operções(transformções)

numeros = [0,2,4,6,8]

novalista = map(somar_1, numeros)
                #função  #interavel(lista, tupla, dicionario)
print(list(novalista))