"""
As tarifas de certo parque de estacionamento são as seguintes:

1ª e 2ª hora - R$ 1,00 cada
3ª e 4ª hora - R$ 1,40 cada
5ª e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minnutos. Crie um programa que, lidos pelo teclado os momentos de chegada e partida, escreva na tela o preço cobrado pelo estacionamento.
"""

print('-----------------------------------------')
print('             PARQUIMETRO                 ')
print('-----------------------------------------')
print('Formato de data dd/mm')
print('Formato de hora 24h 00:00')

# dt_chegada = input('Data de entrada -> ')
hr_chegada = input('Hora de entrada -> ')
# dt_saida = input('Data de saída -> ')
hr_saida = input('Hora de saída -> ')

# if dt_saida == dt_chegada:


if tot_horas <= 2:
    tot_pg = tot_horas * 1
elif tot_horas == 3 or tot_horas == 4:
    tot_pg = tot_horas * 1.4
else:
    tot_pg = tot_horas * 2

print(tot_horas)
print(f'O total a pagar é R${tot_pg:.2f}')