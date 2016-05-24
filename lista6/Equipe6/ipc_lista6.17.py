#
# Questao 17 da lista 6 de "Recurs�o";
# Professor: Jucimar Junior;
#
# Alunos;
# Caio de Oliveira Martins - 1615310031;
# Lorene da Silva Marques - 1615310013;
# Nadine da Cunha Brito - 1615310040;
#

#coding: utf-8

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def fatorial_quadruplo(n):
    if n == 0 or n == 1:
        return fatorial(2)
    else:
        return (fatorial(2*n)) / (fatorial(n))
cond = True
n = int(input("Digite um numero para ser calculado o seu fatorial qu�druplo (2n!/n!):\n"))
if n < 0:
    while cond:
        print("Por favor, digite um n�mero positivo para que possa ser calculado o seu fatorial qu�druplo.")
        n = int(input("Digite um numero para ser calculado o seu fatorial qu�druplo (2n!/n!):\n"))
        if n >= 0:
            cond = False

fat_quadra = fatorial_quadruplo(n) 

print("O fatorial qu�druplo de %d (%d!/%d!) � igual a:\n%d" % (n, 2*n, n, fat_quadra))
print("\nObrigado por usar este programa! :D")