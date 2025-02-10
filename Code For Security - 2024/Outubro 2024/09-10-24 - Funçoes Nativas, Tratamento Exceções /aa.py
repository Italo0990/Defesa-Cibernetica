# lista = [1,2,8,90,0,101]


# listao = sorted(lista, reverse=True)
# print(listao)


# ls = ['e','a','t','j','d','v','h','X','S','!']
# lso = sorted(ls)
# print(lso)

# palavras = ['for','coding','security','aula']
# print(sorted(palavras))
# print(sorted(palavras,key=len))

# print(len('for'))
# print(len('coding'))

# numeros = [-1,2,-100,10,9]
# print(sorted(numeros))
# print(sorted(numeros,key=abs))


# letras = ['a','AA','b','BB','z','ZZZ']
# print(sorted(letras))
# print(sorted(letras,key=str.upper))

lista = [5,3,1,11,2,12,17]

def funcao(x):
    return abs(10 - x)

listaordenada =  sorted(lista, key=funcao)
print(listaordenada)