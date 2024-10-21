#EXERCICIO 
#Voce recebeu um csv com os dados de ataques de 2023. Faça a leitura  do csv ataques.csv, 
#acrescente as informações do novo ano e salve em um novo ataques_atual.csv 
import csv


with open('ataques.csv') as file, open('ataques_2023.csv') as file2:
    ataques = list(csv.DictReader(file))
    ataques_2023 = list(csv.DictReader(file2, delimiter=';'))
    at = [lin for lin in ataques if lin]

    for lin in ataques_2023:
        for linha in ataques:
            if linha['Mes'] == lin['Mes']:
                linha.update(lin)
                break

with open('C:\\Users\\labsfiap\\Desktop\\CFS 21-10-24\\ataques_atual.csv', 'w',newline='') as file3:
    atual = csv.DictWriter(file3, fieldnames=ataques[0].keys())
    atual.writeheader()
    atual.writerows(ataques)
