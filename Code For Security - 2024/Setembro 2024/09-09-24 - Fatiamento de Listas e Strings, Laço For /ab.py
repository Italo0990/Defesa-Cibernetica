file_path = '/home/user/projects/python_script.py'
arquivo = file_path.split('/')[-1]

#print(arquivo[1])

print(f'Arquivo com extensão: {arquivo.split('.')[-1]}')