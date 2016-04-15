#Introdução a programação de computadores
#Professor: Jucimar Junior
#Thiago Santos Borges - 1615310023
#Bruno de Oliveira Freire - 1615310030
#Nickso Patrick Façanha Calheiros - 1615310059
#Mateus Mota de Souza - 1615310016
#Igor Menezes Sales Vieira - 1615310007
#
numero = int(input("Digite um numero:"))
aux = numero
reverso = 0

while aux != 0:
    reverso = reverso * 10 + aux % 10
    aux = aux // 10

print("O reverso de numero %d \ne %d"%(numero,reverso))

