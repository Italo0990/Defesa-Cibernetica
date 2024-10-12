falhas = [
    [2,3,1],
    [0,4,2],
    [1,1,0],
    [3,2,4]
]

dia = 1

for falha in falhas:
    total = 0

    for f in falha:
        total += f
        
    print(f'Total de {dia} = {total}')
    dia += 1


 