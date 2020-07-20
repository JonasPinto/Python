# Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Eescolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.

from random import randint

list_in = []
list_out_a = []
list_out_b = []
list_r = []
i = 1
qok = 0
qno = 0
for i in range (0, 5):

    a = randint(1, 10)
    b = randint(1, 10)       
    print(f'Pergunta: Qual é a soma de {a} + {b} ?')
    list_in.append(input('   Resposta: '))
    list_out_a.append(a)
    list_out_b.append(b)
    list_r.append(a + b)

for i in range(0,5):
    print(f'A soma de {list_out_a[i]} + {list_out_b[i]} = {list_r[i]}')
    if list_in[i] == str(list_r[i]):
        print(f'Sua resposta = {list_in[i]}')
        print(f'\033[94mResposta correta\033[m\n')
        qok += 1
    else:
        print(f'Sua resposta = {list_in[i]}')
        print(f'\033[31mResposta incorreta\033[m\n')
        qno += 1
print(f'\033[94mAcertos\033[m = {qok} questões\n\033[31mErros\033[m = {qno} questões')