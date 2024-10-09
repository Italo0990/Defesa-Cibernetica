'''ZIP'''

# lista1 = [1,2,3,4,5]
lista1 = [1,2,3,4,5,6,7,8]

# lista2 = ['a','b','c','d','e']
lista2 = ['a','b','c','d','e','f']

lista3 = list(zip(lista1,lista2))
print(lista3)


lista4 = dict(zip(lista1,lista2))
print(lista4)

for k,v in zip(lista1,lista2):
    print(k,'=',v)


# lista5 = list(zip(lista1,lista2,strict=True))
lista5 = ['SP','MG','GO','RS','PA']

lista6 = list(zip(lista1,lista2,lista5))
print(lista6)


lista7 = list(zip(range(len(lista5)),lista5))
print(lista7)
