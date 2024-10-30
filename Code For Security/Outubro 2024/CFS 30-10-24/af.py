'''Exercicio: Utilize as bibliotecas random e string 
para criar senhas para o usuário com a quantidade de caracteres  solicitada '''''

import random
import string


caracteres = int(input('Digite quantos caracteres na senha: '))
alfabeto = string.ascii_letters + string.digits + string.punctuation

password = ''.join([random.choice(alfabeto) for _ in range(caracteres)])
print(password)