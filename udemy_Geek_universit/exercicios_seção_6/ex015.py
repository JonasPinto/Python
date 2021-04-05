'''
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números impares de 1 até N em ordem crescente
'''
from random import random
lista = []

while True:
    var = random()
    lista.append(round(var))
    if len(lista) == 10000:
        break
print(var)
print(lista)
