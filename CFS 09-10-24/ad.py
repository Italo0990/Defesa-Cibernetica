# Crie um script que dada duas listas
# [1,2,3,4,5] e [6,7,8,9,10] retorne uma nova lista
# com a média entre os itens nas mesmas posições:


lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]


# for k,v in zip(lista1,lista2):
#     print(k,v)

lista3 = [(x + y)/2 for x, y in zip(lista1,lista2)]
print(lista3)