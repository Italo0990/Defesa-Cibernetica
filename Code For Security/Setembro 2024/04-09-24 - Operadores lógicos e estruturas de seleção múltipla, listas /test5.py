carros_vendas = ['hb20', 'civic', 'argo', 'tesla']

print(carros_vendas)

carros_vendas.append('Onix')
print(carros_vendas)

carros_vendas.insert(0, 'Onix')
print(carros_vendas)

del carros_vendas[0]
print(carros_vendas)

valor = carros_vendas.pop(1)
print(carros_vendas, valor)