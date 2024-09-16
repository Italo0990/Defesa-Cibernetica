valores = list(range(4,11))

print(valores)

# valores = list(range(4,11, 2)) 
# colocar o 2 depois do 11, indica o "caminho"
# (No caso, a contagem a cima vai ser de 2 em 2)

valores = [8,2,5,4,9,3,0]

valores.sort() 
# Coloca os núemros me ordem crescente

valores.sort(reverse=True)
# Coloca os núemros me ordem decrescente

len(valores)
# Conta quantos elementos tem na lista

del()
# remove um elemento de uma lista pelo índice ou pela sequência do índice (slice)

string()
# para dividir uma string em uma lista de substrings, ou seja, em pequenos pedaços

# slice:
# b = "Hello, World!"
# print(b[2:5])
# Nesse caso, ele vai imprimir "llo"