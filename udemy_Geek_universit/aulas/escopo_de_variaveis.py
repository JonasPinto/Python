"""
Escopo de variaveis

Dois casos de escopo:
-Variaveis globais
  São reconhecidas por todo o programa
-variaveis locais
  São reconhecidas apenas naquele bloco onde foi declarada

para declarar uma variavel em python fazemos:

nome = 'Jonas'
x = 14
n = 3.14

python possui tipagem dinamica, isso significa que ao declararmos uma variavel
não precisamos declarar o tipo de dado dela
o tipo é inferido ao atribuirmos um valor a ela

exemplo em c:
int numero = 32;

exemplo em java:
int numero = 32;
"""
numero = 32
print(numero)
print(type(numero))
                             #     <-  exemplos de variavel global
numero = 'jonas'
print(numero)
print(type(numero))


