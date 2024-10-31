'''ENUMERATE'''

pessoas = ['Sarah','Maria','Onofre']
lista = list(enumerate(pessoas))
print(lista)

lista2 = dict(enumerate(pessoas))
print(lista2)

for k,v in enumerate(pessoas):
    print(k,'=',v)


lista3 = list(enumerate(pessoas,150))
print(lista3)