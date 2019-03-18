import threading
import os
from _datetime import datetime
from time import ctime

os.system('clear')

#------------------------------------------------------------------------------
# Função para o cálculo da soma dos elementos da Sequência de Fibonacci
#------------------------------------------------------------------------------
def fibonacci(x):
   if x < 2: return 1
   return (fibonacci(x-2) + fibonacci(x-1))


#------------------------------------------------------------------------------
# Função para o cálculo do Fatorial
#------------------------------------------------------------------------------
def fatorial(x):
   if x < 2: return 1
   return (x * fatorial(x-1))

	
#------------------------------------------------------------------------------
# Função para o cálculo da soma dos N elementos
#------------------------------------------------------------------------------
def soma(x):
   if x < 2: return 1
   return (x + soma(x-1))



lFuncoes = [fibonacci, fatorial, soma]
iValor = 35


#------------------------------------------------------------------------------
# Função Principal do Programa
#------------------------------------------------------------------------------
def main():
   print('--------------------------------------------')
   print('THREAD ÚNICA')

   hora_inicial = datetime.now()
   print('Iniciando às {0}'.format(ctime()))

   for i in range(len(lFuncoes)):
      print('Função {0} resultou {1}'.format(lFuncoes[i].__name__.upper(), lFuncoes[i](iValor)))

   hora_final = datetime.now()
   print('Finalizdo às {0}'.format(ctime()))
   print('Tempo Decorrido: {0}'.format(hora_final-hora_inicial))
   print('--------------------------------------------')

   print('\n\n\n')

   print('--------------------------------------------')
   print('THREADS MÚLTIPLAS')
   print('--------------------------------------------')

   threads = []
   for i in range(len(lFuncoes)):
      t = threading.Thread(target=lFuncoes[i], args=(iValor,), name=lFuncoes[i])
      threads.append(t)

   hora_inicial = datetime.now()
   print('Iniciando às {0}'.format(ctime()))

   for i in range(len(lFuncoes)): threads[i].start()

   for i in range(len(lFuncoes)):
      threads[i].join()
      print('Função {0} resultou'.format(threads[i].getName().upper()))

   hora_final = datetime.now()
   print('Finalizdo às {0}'.format(ctime()))
   print('Tempo Decorrido: {0}'.format(hora_final-hora_inicial))
   print('--------------------------------------------')

   print('Fim do Exemplo')

#-----------------------------------------------------
# Chamando a Função Principal do Programa
#-----------------------------------------------------
if __name__ == '__main__': main()
