def dispo(disposivio,**config):
    print(disposivio,':')
    if config:
        print(config)
    else:
        print('Sem COnfigurações')


dispo(disposivio='Notebook',processador='Snapdragon 888', ram='8GB')