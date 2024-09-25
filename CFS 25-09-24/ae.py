'''SET'''

#set não permite duplictas
#

conjunto = {1,2,3,4,4,5}
print(conjunto)

conjunto2 = set([1,1,2,3,3,4,5])
print(conjunto2)

conjunto3 = set('palavra')
print(conjunto3)

for x in conjunto:
    print(x)

print(1 in conjunto)

lista = list(conjunto)
print(lista)

