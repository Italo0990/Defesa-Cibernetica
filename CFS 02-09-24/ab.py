print ('Bem vindo ao site do Banco Super Cash!\n')

opcao = int(input('Digite a Opção 1 - Saldo ou Opção 2 - Extrato: '))

if opcao == 1:
    print('Seu saldo é de R$100,00')
elif opcao == 2:
    print('''
          Dia 10/09/24 - Recebimento R$1000,00
          Dia 10/09/24 - Compra Adega R$ 949,75
          ''')
else:
    print('opção inválida')