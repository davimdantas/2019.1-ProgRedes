nome_1 = 'Charles Cesar Magno de Freitas'
nome_2 = 'Charles Freitas'
texto  = 'RN;PB;CE;BA;SP;RJ'

#------------------------------------
print('Exemplo 1: ')
x = nome_1.split()
print(x)
print('')

#------------------------------------
print('Exemplo 2: ')
nome, sobrenome = nome_2.split()
print(nome)
print(sobrenome)
print('')

#------------------------------------
print('Exemplo 3: ')
uf1 = texto.split(';')
print(uf1)
print('')

uf2 = texto.split(';',1)
print(uf2)
print('')

uf3 = texto.rsplit(';',1)
print(uf3)
print('')
