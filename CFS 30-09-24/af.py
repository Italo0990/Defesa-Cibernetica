saldo = 1000
print(saldo)

def saque(valor):
    global saldo
    if saldo > valor:
        print(f'Saque de {valor} realizado')
        print(f'Saldo da CC = {saldo}')
    else:
        print('Saldo insuficiente.')
    
    
def deposito(valor):
    global saldo
    saldo >= valor
