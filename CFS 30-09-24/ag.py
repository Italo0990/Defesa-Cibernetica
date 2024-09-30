users = [ 
        {'id':1,'username':'admin'}, 
        {'id':2,'username':'estagiario02'}, 
        {'id':3,'username':'estagiario01'} 
    ] 

def login(username):
    for user in users:
        if user['username'] == username:
            return user['id'], user['username']
        
        
user = login('admin')

if user:
    print(f'Usuário encontrado')
else:
    print('Não encontrado')
            
            