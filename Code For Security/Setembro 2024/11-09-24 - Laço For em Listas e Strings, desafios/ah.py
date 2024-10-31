#for _ in range(10):
    #print('Qualqer coisa')

#LIST COMPREHENSION

#nome = 'Sarah' if 1 > 0 else 'Sah'
#print(nome)

numeros = [1,2,3,4,5,6,7,8,9,10]

pares = [num for num in numeros if num % 2 == 0]
print(pares)

#OU

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    print(pares)