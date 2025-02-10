var_global = 'Variável global'
print(var_global)

def func():
    var_local = 'Variável local'
    global var_global
    var_global = 'Altera global'
    print(var_local,'e', var_global)
    
func()
print(var_global)