'''DICIONÁRIO'''

dicionario = {'nome': 'Sarah', 'sobrenome': 'Lima'}
print(dicionario)

print(dicionario['nome'])
print(dicionario.get('idade', 'não existe'))
dicionario['idade'] = 22
print(dicionario)
dicionario.update({'cidade': 'SP'})
print(dicionario)
dicionario.pop('cidade')
print(dicionario)
dicionario.popitem() # remove o último item da lista
print(dicionario)




# dicionario2 = dict(nome= 'Sarah', sobrenome= 'Lima')
# print(dicionario2)

