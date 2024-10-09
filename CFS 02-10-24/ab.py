variavel_global = 10
print(variavel_global)


def funcao(arg1, arg2, arg3='!!!'):
    global variavel_global
    variavel_global = 'GLOBAL FUNÇÂO'
    print(variavel_global)
    print('Hello', arg1, arg2, arg3)


funcao('World', 2024)
print(variavel_global)