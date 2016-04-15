#Introdução a programação de computadores
#Professor: Jucimar Junior
#Thiago Santos Borges - 1615310023
#Bruno de Oliveira Freire - 1615310030
#Nickso Patrick Façanha Calheiros - 1615310059
#Mateus Mota de Souza - 1615310016
#Igor Menezes Sales Vieira - 1615310007
#
N  = int(input("N:"))
cont = 1
H = 0
while cont < (N+1):
    print("1/",cont)
    H = H + (1/cont)
    cont = cont + 1
print("O resultado da serie ",H)
