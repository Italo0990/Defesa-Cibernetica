notas = [
    4,6,5,8,9,10,10,7,8,8,7,8,7,9,4,2,1
]

aprovados = [0]
reprovados = [1]

media = 7

print('-='*30)
print('NOTA DOS ALUNO: ')
print('-='*30,'\n')

for n in notas:
    if n >= media:
        print(f'Está na média (Aprovado): {n}\n')
    else:
        print(f'Não está na média (reprovou): {n}\n')

print(f'Aprovados {aprovados}')
print(f'Reprovados {reprovados}')
    
