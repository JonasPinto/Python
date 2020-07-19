# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis

d = input('Digite qualquer coisa : ')
print(f'O tipo primitivo de \033[31m{d}\033[m é', type(d))
print('Só tem espaços?', d.isspace())
print('É número?', d.isnumeric())
print('É alfabetico?', d.isalpha())
print('É alfanumérico', d.isalnum())
print('Está em maiúsculas?', d.isupper())
print('Está em minúsculas?', d.islower())
print('A primeira letra é maiuscula?', d.istitle())
print('Começa com com jo ?', d.startswith('j'))

