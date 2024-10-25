# Crie um script que leia o arquivo ip.txt 
# e salve o conteúdo em outro arquivo chamado lista_ip.txt
# acrescentado a informação ‘IP: ‘ 
# Exemplo: IP: numero do IP 



with open('C:\\Users\\labsfiap\\Desktop\\ip.txt') as file:
    # file.readlines()

    with open('C:\\Users\\labsfiap\\Desktop\\lista_ip.txt', 'w') as file2:
        for x in file2:
            file2.write(x)
        