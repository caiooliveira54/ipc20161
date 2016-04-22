#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 4
#
#Bruno de Oliveira Freire - 1615310030
#Igor Menezes Sales Vieira - 1615310007
#Matheus Mota de Souza - 1615310016
#Nadine da Cunha Brito - 1615310040
#Nickso Patrick Façanha Calheiros - 1615310059
#Thiago Santos Borges - 1615310023
#

N  = int(input("N:"))
cont = 1
H = 0
while cont < (N+1):
    print("1/",cont)
    H = H + (1/cont)
    cont = cont + 1
print("O resultado da serie ",H)
