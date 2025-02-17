class Estudante:
    
    universidade = 'Uninove'
    
    def __init__(self,nome,ano,id,media):

        
        self._nome = nome
        self._ano = ano
        self._id = id
        self._media = media
        
    def __str__(self):
        return f'{self._nome.ljust(15)} | {self._ano.ljust(15)} | {self._id.ljust(15)} |  {int(self._media)}'
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        if not nome or isinstance(nome,str):
            raise Exception('Nome inválido')
        self._nome = nome
    
    @staticmethod
    def tem_alura(self):
        if self._media >= 8:
            return f'Tem Alura!'
        return f'Não tem alura :C'
    
    @classmethod
    def set_universidade(cls,novauni):
        cls.universidade = novauni
        
    
e1 = Estudante('Sarah', '3° ano', 'ID12563', 8)
e2 = Estudante('Italo', '1° ano', 'ID28374', 7)

print('='* 75)
print('REGISTO DOS ESTUDANTES:')
print('='* 75)
e1.tem_alura()
print(e1)
print(e2)

print('='* 75)