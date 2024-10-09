def funcao(*arg):
    print(arg)

funcao(1,2,3,4,5)

# O asterísco permite colocar quantos argumentos você quiser



def funcao2(arg1,arg2,arg3):
    print(arg1,arg2,arg3)


lista = [1,2,3,4,5]
funcao2(*lista)