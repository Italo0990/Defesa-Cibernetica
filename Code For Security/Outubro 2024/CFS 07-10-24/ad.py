def caixa_alta(x):
    print(x)
    return x.upper()

nome = 'tesla'

resultado = map(caixa_alta, nome)
print(list(resultado))