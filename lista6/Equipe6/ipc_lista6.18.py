#
# Questao 18 da lista 6 de "Recursão";
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

def super_fatorial(n):
    super_fat = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(n):
            super_fat *= fatorial(n-i) 
        return super_fat
cond = True
print("Fórmula do super fatorial de um número:\n n! * (n-1)! * (n-2)! * ... * 3! * 2! * 1!")
n = int(input("Digite um numero para ser calculado o seu super fatorial:\n"))
if n < 0:
    while cond:
        print("Por favor, digite um número positivo para que possa ser calculado o seu super fatorial.")
        n = int(input("Digite um numero para ser calculado o seu super fatorial:\n"))
        if n >= 0:
            cond = False

super_fat = super_fatorial(n)

print("O super fatorial de %d é igual a:\n%d" % (n, super_fat))
print("\nObrigado por usar este programa! :D")