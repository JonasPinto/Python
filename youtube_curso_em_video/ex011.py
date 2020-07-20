# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade necessária
# para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Digite a largura :'))
a = float(input('Digite a altura :'))
area = l * a
lt = area / 2
print(f'A area de parede é de \033[31m{area}\033[m m²')
print(f'Será necessario \033[31m{lt}\033[m litros de tinta para pinta-la')
