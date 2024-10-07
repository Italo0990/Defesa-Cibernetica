
##############################################
#                                            #   
#  exercicio ae.py, mas com o uso do lambda  #
#                                            # 
##############################################


#map(função, lista)
#lambda já tem a função return 

numero = [1,2,3,4,5]
resultado = list(map(lambda x: x**2, numero))
print(resultado)
print(set(filter(lambda x: 5 < x <20, resultado)))