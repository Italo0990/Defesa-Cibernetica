print ('Bem vindo ao site!\n')

idade = int(input('Digite a sua idade: '))


if idade >= 18 and idade < 65:
    print (f'Sua idade é {idade}, vocé é maior de idade!\n')
elif idade >=65:
    print (f'Sua idade é {idade}, Você é preferencial!\n')
else:
    print(f'Sua idade é {idade}, Você é menor de idade!\n')