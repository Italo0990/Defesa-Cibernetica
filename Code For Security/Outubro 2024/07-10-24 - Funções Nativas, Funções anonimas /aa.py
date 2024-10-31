def funcao(x):
    print(x)
    return x > 3 # True ou False


numeros = [0,0,2,4,5,7]
tupla = (0,0,2,4,5,7)
dicionario = {1:1,2:2,5:5,6:6}

novalista = filter(funcao, numeros)
                #função  #interavel(lista, tupla, dicionario)



print(list(novalista))