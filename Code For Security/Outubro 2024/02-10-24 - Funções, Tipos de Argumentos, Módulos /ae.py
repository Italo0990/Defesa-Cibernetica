def soma(*num):
    # soma = 0
    # for n in num:
    #     soma += n
    return sum(num)




def media(*num):
    # media = 0
    # for n in num:
    #     medi += n
    return sum(num) / len(num)


print(soma(2,2))
print(media(3,1))