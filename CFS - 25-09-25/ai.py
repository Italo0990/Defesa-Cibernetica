dicionario = {'nome': 'Sarah', 'sobrenome': 'Lima'}
print(dicionario)

# print(dicionario['nome'])
# print(dicionario.get('idade', 'não existe'))

dicionario['idade'] = 22
print(dicionario)

# print(dicionario.keys())
# print(dicionario.values())
# print(dicionario.items())

for x in dicionario.keys():
    print(x)

for x in dicionario.values():
    print(x)

for chave, valor in dicionario.items():
    print(chave,'=',valor)

