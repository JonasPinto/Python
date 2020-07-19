# crie um algoritmo leia um numero e mostre o seu dobro, triplo e sua raiz quadrada

from math import sqrt   # metodo de importação da função sqrt(raiz quadrada) da biblioteca math(matemática)

n = float(input('\033[35mDigite um número\033[m\n'))
print(f'O dobro de {n} é {n * 2}')
print(f'O triplo de {n} é {n * 3}')
print(f'A raiz quadrada de {n} é {sqrt(n):.2f}')
# print(f'A raiz quadrada de {n} é {n ** (1/2)}')   <--- metodo utilizando exponenciação n elevado a 1/2 (0.5)
#                                  {pow(n, (1/2))}  <--- metodo utilizando power
