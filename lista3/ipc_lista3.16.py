#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 3
#
#Antonio Rodrigues de Souza Neto - 1615310028
#Caio de Oliveira Martins - 1615310031
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#

A, B, cont = 1, 1, 2
print(A)
while cont < 500:
    print(B)
    C = A + B
    A = B
    B = C
    cont += 1
print(C)
