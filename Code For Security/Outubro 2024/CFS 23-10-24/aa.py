import json

aluno = {
    'nome' : 'Sarah',
    'sobrenome' : 'Lima',
    'idade' : 17,
    'bolsa' : False,
    'materias' : [
        'coding',
        'network',
        'mindset',
        'architecture'
    ]
}



with open('aluno_mini.json', 'w') as file:
    json.dump(aluno, file, indent=None, separators=(',',':'))


# with open('ex.json') as file:
#     animal = json.load(file)

# print(animal)
# print(type(animal))
# print(animal['hobbies'])


# jaluno = json.dumps(aluno)
# aluno_json = json.loads(jaluno)
# print(aluno_json)
# print(aluno_json['nome'])

# with open('aluno.json','w') as file:
#     jaluno = json.dump(aluno,file)
#     print(jaluno)

# jaluno = json.dumps(aluno,indent=2)
# print(jaluno)

# jaluno = json.dumps(aluno,sort_keys=True)
# print(jaluno)

# jaluno = json.dumps(aluno)
# print(jaluno)
# print(type(jaluno))

'''
dict --> obeject {}
list --> array []
tuple --> array []
none --> null
'''