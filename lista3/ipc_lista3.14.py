#Introdução a programação de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

cont = 1
par = 0
impar = 0
while cont <= 10:
    num = int(input("Digite o numero %i: "%cont))
    if num % 2 ==0:
        par += 1
    else:
        impar += 1

    cont += 1

print("Há um total de %i numeros pares e %i numeros impares."%(par, impar))
