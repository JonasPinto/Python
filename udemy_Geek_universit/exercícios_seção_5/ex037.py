"""
As tarifas de certo parque de estacionamento são as seguintes:

1ª e 2ª hora - R$ 1,00 cada
3ª e 4ª hora - R$ 1,40 cada
5ª e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minnutos. Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior á da partida, isso não é uma cituação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.   
"""

"""
print('-----------------------------------------')
print('             PARQUIMETRO                 ')
print('-----------------------------------------')
print('Formato de hora 24h 00:00')

chegada = input('Digite o horaio de entrada -> ')
saida = input('Digite o horario de saída    -> ')

s = '2015/08/05 08:12:23'
t = '2015/08/09 08:13:23'




print(chegada)
print(type(chegada))
"""



"""
if tot_horas <= 2:
    tot_pg = tot_horas * 1
elif tot_horas == 3 or tot_horas == 4:
    tot_pg = tot_horas * 1.4
else:
    tot_pg = tot_horas * 2

print(f'O total a pagar é R${tot_pg:.2f}')
"""