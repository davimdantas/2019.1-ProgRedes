import random

linha = ''

arquivo = open('notas_alunos.txt', 'w')

for contador in range (1,1001):
    matricula = '20182501' + str(contador).zfill(5) + str(random.randint(1,9))

    nota_1 = random.uniform(1,10)
    nota_2 = random.uniform(1,10)
    nota_3 = random.uniform(1,10)
    nota_4 = random.uniform(1,10)

    linha = linha + '{0};{1:.2f};{2:.2f};{3:.2f};{4:.2f}\n'.format(matricula, nota_1, nota_2, nota_3, nota_4)


arquivo.write(linha)

arquivo.close()
