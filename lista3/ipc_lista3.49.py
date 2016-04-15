#Introdução a programação de computadores
#Professor: Jucimar Junior
#Thiago Santos Borges - 1615310023
#Bruno de Oliveira Freire - 1615310030
#Nickso Patrick Façanha Calheiros - 1615310059
#Mateus Mota de Souza - 1615310016
#Igor Menezes Sales Vieira - 1615310007
#
cont = 0
n = 1
m = 1
soma = 0
limite = int(input("Digite limite:"))
while cont < limite:
    print(n,"/",m)
    soma = soma + (n/m)
    n = n + 1
    m = m +2
    cont = cont + 1
    
print("A soma da serie ",soma)
