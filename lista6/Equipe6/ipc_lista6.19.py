#
# Questao 19 da lista 6 de "Recursão";
# Professor: Jucimar Junior;
#
# Alunos;
# Caio de Oliveira Martins - 1615310031;
# Lorene da Silva Marques - 1615310013;
# Nadine da Cunha Brito - 1615310040;
#

#coding: utf-8
def potencia(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n**n

def hiper_fatorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return potencia(n) * potencia(n-1)

cond = True
print("Fórmula do hiper fatorial de um número:\n 1^1 * 2^2 * 3^3 * 4^4 * ... * (n-1)^(n-1) * n^n")
n = int(input("Digite um numero para ser calculado o seu hiper fatorial:\n"))
if n < 0:
    while cond:
        print("Por favor, digite um número positivo para que possa ser calculado o seu hiper fatorial.")
        n = int(input("Digite um numero para ser calculado o seu hiper fatorial:\n"))
        if n >= 0:
            cond = False

hiper_fat = hiper_fatorial(n)

print("O hiper fatorial de %d é igual a:\n%d" % (n, hiper_fat))
print("\nObrigado por usar este programa! :D")