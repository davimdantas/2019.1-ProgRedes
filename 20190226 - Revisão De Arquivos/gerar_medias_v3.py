# Abrindo arquivo em modo de Leitura
arquivo = open('notas_alunos.txt', 'r')

lista_notas = []

# Lendo a primeira linha do arquivo
conteudo = arquivo.readline()

# Adicionando a primeira linha do arquivo na lista_notas
# Removendo '\n' com [:-1] e separando as informações
# com split (caractere de separação ';')
linha = conteudo[:-1].split(';')
lista_notas.append(linha)

while conteudo:
   # Lendo uma linha do arquivo a cada iteração do WHILE
   conteudo = arquivo.readline()
   # Adicionando a linha do arquivo na lista_notas
   # Removendo '\n' com [:-1] e separando as informações
   # com split (caractere de separação ';'
   linha = conteudo[:-1].split(';')
   lista_notas.append(linha)

# Fechando o Arquivo
arquivo.close()

# Removendo a última posição da lista
lista_notas.pop()

# Calculando as Médias
for contador in range(0, len(lista_notas)):
    matricula = lista_notas[contador][0]
    nota_1    = float(lista_notas[contador][1])
    nota_2    = float(lista_notas[contador][2])
    nota_3    = float(lista_notas[contador][3])
    nota_4    = float(lista_notas[contador][4])
    media     = (nota_1 + nota_2 + nota_3 + nota_4)/4
    print('{0};{1:.2f};{2:.2f};{2:.2f};{3:.2f};{4:.2f}'.format(matricula,nota_1,nota_2,nota_3,nota_4,media))
