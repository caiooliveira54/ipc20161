#
# Questao 5 da lista 6 de "Recurs�o";
# Professor: Jucimar Junior;
#
# Alunos;
# Caio de Oliveira Martins - 1615310031;
# Lorene da Silva Marques - 1615310013;
# Nadine da Cunha Brito - 1615310040;
#

#coding: utf-8
def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n-1)

cond = True
n = int(input("Digite um numero para ser calculado o seu somat�rio de 1 a N:\n"))
if n <= 0:
    while cond:
        print("Por favor, digite um numero que seja maior que 0 para que se possa calcular o somat�rio.")
        n = int(input("Digite um numero para ser calculado o seu somat�rio de 1 a N:\n"))
        if n > 0:
            cond = False

soma = somatorio(n)

print("O somat�rio de 1 a %d � igual a:\n%d" % (n, soma))
print("\nObrigado por usar este programa! :D")