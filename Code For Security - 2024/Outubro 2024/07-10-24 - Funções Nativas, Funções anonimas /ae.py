#Crie um script no qual dado uma lista [1,2,3,4,5], 
# elevamos todos os seus elementos ao quadrado em uma nova lista, 
# que por sua vez deverá ser filtrada para um conjunto 
# contendo apenas os itens que forem > 5 e < 20. 


def quadrado(x):
    print(x)
    return x**2

def filtrar(x):
    return 5 < x <20

numero = [1,2,3,4,5]
resultado = list(map(quadrado, numero))
print(resultado)
print(set(filter(filtrar, resultado)))



