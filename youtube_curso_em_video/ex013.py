# faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Digite o salário atual do funcionário R$'))
aum = sal * 0.15 + sal
print(f'O novo salario com aumento é de \033[35mR${aum:.2f}\033[m')
