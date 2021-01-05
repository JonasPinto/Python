'''
Faça um algoritmo que caucule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

          I M C            /      C l a s s i f i c a ç ã o
          <18,5                      Abaixo do peso
          18,6 - 24,9                Peso normal
          25,0 - 29,9                Sobrepeso
          30,0 - 34,9                Obesidade Grau I
          35,0 - 39,9                Obesidade Grau II(severa)
          >= 40,0                    Obesidade Grau III(mórbida)
'''
import math

altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))

imc = peso / math.sqrt(altura)

print(imc)