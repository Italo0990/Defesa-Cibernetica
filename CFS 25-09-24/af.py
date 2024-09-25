conjunto = {1,2,3,4,4,5}
print(conjunto)
conjunto.add(100)
print(conjunto)

conjunto2 = {100,101,102,103}
print(conjunto2)

conjunto.update(conjunto2)
print(conjunto)

conjunto.remove(100)
print(conjunto)

conjunto.discard(101)
print(conjunto)