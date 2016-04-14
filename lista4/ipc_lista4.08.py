"""
lista 4 questao 8:
Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""
# EQUIPE 2
#ANA BEATRIZ FROTA - 1615310027
#
#
#Luiz Gustavo Rocha Melo - 1615310015
altura = [] #vetor para altura
alturainv = [] #vetor para a altura na ordem inversa
idade = [] #vetor para idade
idadeinv = [] #vetor para idade na ordem inversa
v = 5 #variável para o indice
c1 = #contador

while (c1 < v): 
    x = int(input("A idade da pessoa: "))
    idade.append(x) 
    y = float(input("A altura da pessoa: "))
    altura.append(y)
    c1 += 1
    
while (v > 0):
    v -= 1
    w = idade[v]
    z = altura [v]
    
    idadeinv.append(w)
    alturainv.append(z)

print("A ordem inversa da idade",idadeinv)
print("A ordem inversa da altura",alturainv)
