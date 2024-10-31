'''RANDOM'''

import random
import string


letras = string.ascii_letters
print(letras)
letras = string.ascii_lowercase
print(letras)
letras = string.ascii_uppercase
print(letras)
letras = string.digits
print(letras)
letras = string.punctuation
print(letras)

#float
print(random.random())
print(random.uniform(0,2))

#int
print(random.randrange(0,10,2))
print(random.randint(0,50))

#lista
lista = ['sarah', 'maria', 'jose', 'luigi']

print(random.choice(lista))
print(random.choices(lista, k=2))
print(random.choices(lista, weights=[1,1,1,10,2], k=2))
print(random.sample(lista,k=3))

random.shuffle(lista)
print(lista)