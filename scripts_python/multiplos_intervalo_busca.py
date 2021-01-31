mult = []
nums = []
num = ''

ini = int(input('Digite o intervalo inicial de busca númerica: '))
fim = int(input('Digite o fim do intervalo: '))
divi = int(input('Entre com o Coeficiente: '))
bus = input('Digite o número que deseja buscar na sequência: ')

for i in range(ini, fim):
    num = str(i)
    if i % divi == 0:
        mult.append(num)
    if bus in num:
            nums.append(num)
    
print(nums, len(nums))
print('\n',mult, len(mult))
