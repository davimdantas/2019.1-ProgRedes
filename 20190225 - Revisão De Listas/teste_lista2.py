nomes = []

nome = ''

while True:
   nome = input('Informe um nome: ').upper()
   if nome == 'EXIT': break
   nomes.append(nome)


print(nomes)
