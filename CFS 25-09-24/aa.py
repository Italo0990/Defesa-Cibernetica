'''LISTA'''

lista = [1,2,3,4,5]
print(lista)

lista2 = [x ** 2 for x in lista]
print(lista2)

lista3 = list([5,6,7,8])
print(lista3)

lista4 = list('coding')
print(lista4)

print(lista4[3])

lista4.append('M')
print(lista4)

lista4.insert(0,'P')
print(lista4)

lista4.remove('P')
print(lista4)

lista4.pop()
print(lista4)

del lista4[0]
print(lista4)

lista4.clear()
print(lista4)