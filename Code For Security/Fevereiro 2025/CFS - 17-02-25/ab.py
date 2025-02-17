'''DECORATORS'''

def mestre(func):
    def funcionalidade():
        print('Funcionalidade do mestre')
        func()
    return funcionalidade


@mestre
def servo():
    print('Função servo')
    
# mestre()
servo()