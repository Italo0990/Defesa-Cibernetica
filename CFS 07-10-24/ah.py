# Crie uma função lambda que filtre as 
# linguagens que têm mais de 10 milhões de desenvolvedores ativos. 

linguagens = [ ("Python", 18.0), 
              ("JavaScript", 14.5),     
              ("Java", 9.8),    
              ("C#", 6.5),
              ("C++", 5.6), 
              ("Ruby", 2.2), 
              ("Go", 1.5) 
] 


palavra = filter(lambda x: x[1] > 10, linguagens)



print(list(palavra))