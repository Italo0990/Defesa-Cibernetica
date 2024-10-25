# Crie um script que dado um dicionário 
# com alunos, e uma lista com novos alunos, 
# insira os novos alunos mantendo a sequencia das chaves:

alunos = {
  7:{'nome':'Jose','sobrenome':'Silva'},
   8:{'nome':'Jose','sobrenome':'Souza'},
  9:{'nome':'Maria','sobrenome':'Silva'},
  10:{'nome':'Enio','sobrenome':'Lopes'}
   }
novo = [
  [('nome','Mario'),('sobrenome','Gomes')],
  [('nome','Kang'),('sobrenome','Pereira')]
   ]


ultimo = max(alunos.keys())
for chave, valor in enumerate(novo, ultimo + 1):
    alunos[chave] = dict(valor)

    print(alunos)