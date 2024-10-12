# Crie um script que contenha uma função que 
# receba uma lista de números e retorne a média aritmética deles.
# Trate exceções caso a lista esteja vazia ou contenha
# valores não numéricos:

def calcula_media(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        print('Lista Vazia')
    except TypeError:
        print('Lista deve conter números')

print(calcula_media([1,5,8]))
print(calcula_media([]))
print(calcula_media([1,'5,',8]))