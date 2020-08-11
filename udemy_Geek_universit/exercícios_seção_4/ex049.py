"""
Faça um programa que leia um horario (Hora,Minuto,Segundo) de inicio e a duração em segundos de uma
experiencia biologica. O programa deve retornar com o novo horario (Hora, Minuto, Segundo)
de termino da mesma.
"""
print(f'Digite abaixo o horario de inicio do experimento')
hi = str(input('Horas : Minutos : Segundos '))
h = int(hi[0] + hi[1])
m = int(hi[3] + hi[4])
s = int(hi[6] + hi[7])
sd = int(input('Quantos segundos de duração: '))
st = (h * 3600) + (m * 60) + sd + s
dc = st // 86400
sgr = st % 86400
hc = sgr // 3600
sgr0 = sgr % 3600
mc = sgr0 // 60
sc = sgr0 % 60

if dc == 0:
    print(f'A experiência terminou as \033[34m{hc}:{mc}:{sc}\033[m')
elif dc > 0:
    print(f'A experiência durou \033[33m{dc}\033[m dia(s) \033[34m{hc}\033[m hora(s) \033[34m{mc}\033[m minutos \033[34m{sc}\033[m segundos')