import csv


# with open('ataques.csv') as file:
#     # print(file.read())
#     for linha in file:
#         l = linha.rstrip().split(',')
#         print(l)

# with open('dados_pessoais.csv', encoding='utf -8') as file:
#      for pessoas in file:
#          p = pessoas.rstrip().split(',')
#          print(p[4])

# with open('dados_pessoais.csv', encoding='utf -8') as file:
#       pessoas = csv.reader(file)
#       for pessoas in file:
#          print(pessoas)

# with open('ataques.csv') as file:
#     ataques = csv.reader(file)
#     for linha in file:
#         print(linha)

# with open('ataques.csv') as file:
#     ataques = csv.reader(file, delimiter=':')
#     at = [lin for lin in ataques if lin]
    
#     for mes, _2020,_2021,_2022 in at:
#         print(f'''
#               Mês: {mes}
#               2020: {_2020}
#               2021: {_2021}
#               2022: {_2022}
#               ''')

# with open('dados_pessoais.csv', encoding='utf -8') as file:
#       pessoas = csv.DictReader(file)
#      #print(list(pessoas))
#       for pessoas in pessoas:
#         print(f'{pessoas['Nome']} mora em {pessoas['Cidade']}')

# nova_pessoa = ['Mario Jose',50,'marioj@email.com','São Paulo', 'Rua da Fiap 500']
# nova_pessoa2 = ['Maria Josefa',40,'mariaj@email.com','São Paulo', 'Rua da Fiap 400']

# with open('dados_pessoais.csv','a', encoding='utf-8', newline='') as file:
#   pessoas = csv.writer(file)
#   pessoas.writerow(nova_pessoa2)


# nova_pessoa = {'Nome':'Paul Math',
#                'Idade': 20,
#                'Email':'paul@email.com',
#                'Cidade':'Belo Horizonte', 
#                'Endereço':'Rua das Freiras, 701'
#                }

# nova_pessoa2 = {'Nome':'Tomaz Onofre',
#                'Idade': 20,
#                'Email':'tomaz@email.com',
#                'Cidade':'São Paulo', 
#                'Endereço':'Rua das Faculdades, 701'
#                }
  
# with open('dados_pessoais.csv','a', encoding='utf-8', newline='') as file:
#   cabeçalhos = ['Nome','Idade','Email','Cidade', 'Endereço']
#   pessoas = csv.DictWriter(file, fieldnames=cabeçalhos)
#   # pessoas.writeheader()
#   pessoas.writerow(nova_pessoa)
#   pessoas.writerow(nova_pessoa2)
  