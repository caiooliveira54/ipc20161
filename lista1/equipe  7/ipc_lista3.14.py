"""
#lista de repetição

#Antonio Rodrigues de Souza Neto --- matrícula ----1615310028
#Gabriel Machado Moreira --- matrícula ----1615310034
#Luiz Gustavo de Rocha Melo --- matrícula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matrícula---1615310043

"""
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
