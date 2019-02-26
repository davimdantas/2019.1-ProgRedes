nomes = []

nome = ''

while True:
   nome = input('Informe um nome: ').upper()
   sobrenome = input('Informe um sobrenome: ').upper()
   if nome == 'EXIT' or sobrenome == 'EXIT': break
   lista_aux = []
   lista_aux.append(nome)
   lista_aux.append(sobrenome)
   nomes.append(lista_aux) 


print(nomes)
