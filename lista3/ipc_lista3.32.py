
#Introduçao a programaçao de computadores
#Professor: Jucimar Junior
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
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

