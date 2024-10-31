'''TUPLA'''

tupla = ()
tupla = ('a','b',)
print(tupla)


tupla = tuple([1,2,3,4])
print(tupla)
print(tupla[0])


lista = list(tupla)
print(tupla)
lista[0] = 10
tupla = tuple(lista)
print(tupla)