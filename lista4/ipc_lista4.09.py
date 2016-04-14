"""
lista 4 questao 9
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
#EQUIPE 2
#ANA BEATRIZ FROTA - 1615310027
#
#
#
#
#Luiz Gustavo Rocha Melo - 1615310015


vetor_A = []
v = 10
c1 = 0
soma = 0

while(c1 < v):
    x = int(input("informe um numero inteiro: "))
    vetor_A.append(x)
    soma = soma + (x**2)
    c1 += 1

print("A soma dos quadrados dos elementos e igual a:", soma)
