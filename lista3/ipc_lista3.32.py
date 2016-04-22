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

numero = int(input("Insira um numero para fatoriar: "))
cont = 1
fatorial = 1
operacao = ""
ponto = ""

while (cont<=numero):
    fatorial = fatorial * cont
    operacao = str(cont) + ponto + operacao
    ponto = " . "
    cont += 1

print ("%d! = %s = %d" %(numero, operacao, fatorial))
