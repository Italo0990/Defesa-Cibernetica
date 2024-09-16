lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

lanche[3] = 'picole'

print(lanche)

lanche.append('cookie') 
# adiciona coisas na lista

print(lanche)

lanche.insert(0,'coxinha')
# adiciona coisas em uma posição na lista

print(lanche)

lanche.pop(3) 
# exclui coisas da lista

print(lanche)

lanche.pop()
# o vlaor pop com o () vazio, elimina sempre o
# ultimo item da lista

print(lanche)

if 'pizza' in lanche:
    lanche.pop('pizza')
else:
    print('Pizza já foi removida da lista')
    print(lanche)
    
