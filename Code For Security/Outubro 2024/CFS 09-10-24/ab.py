# lista = [5,3,1,11,2,12,17]

# listaordenada =  sorted(lista, key=lambda x: abs(10 - x))
# print(listaordenada)




# Crie um script que dado um dicionário de alunos e 
# idade gere outro dicionário com os alunos 
# ordenados por idade:


alunos = {
   'jose': 21, 
   'maria': 20, 
  'sebastiao': 24, 
  'antonio': 19, 
  'everaldo': 23, 
   'alva': 27
   }

print(sorted(alunos))
print(sorted(alunos.values()))
print(dict(sorted(alunos.items(), key=lambda x: x[1])))