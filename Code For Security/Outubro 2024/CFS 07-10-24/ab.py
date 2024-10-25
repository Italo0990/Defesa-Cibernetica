def funcao(x):
    print(x)
    return x != 'a'

#Filter - Retorna apenas True ou False

novalista = filter(funcao, 'palavra')
print(list(novalista))