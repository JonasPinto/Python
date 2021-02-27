'''
Faça um programa que leia um número inteiro positivo par N, e imprima todos os números pares de 0 até N em ordem decrescente
'''
import time
resp = ''
while True:
    n = int(input('Digite um número inteiro, positivo e par: '))
    if n > 0 and n % 2 == 0:
        for i in range(n, 0, -2):
            time.sleep(0.2)
            print(i, end= ' ')
    else:
        print('Número inválido!')
    resp = input('\nENTER -> Continuar: \nS -> Sair: ')
    if resp == 's':
        break
    