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

print(lista_notas)

