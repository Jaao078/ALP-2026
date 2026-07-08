def ola(nome, genero):
    if genero == 'm':
        return f'olá {nome}, bem vindo'
    elif genero == 'f':
        return f'olá {nome}, bem vinda'
    elif genero == 'n':
        return f'olá {nome}, boas vindas'
Nome = input ('qual seu nome?')
Genero = input ('qual seu genero?')
print (ola(Nome, Genero))