"""
lista 4 questao 9
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Kylciane Cristiny Lopes Freitas - 1615310052
#Frankilin Yuri Gonçaves dos santos - 1615310033
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
