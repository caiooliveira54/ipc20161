#Introduçao a Programação de Computadores
#Professor: Jucimar Junior
#Bruno de Oliveira Freire - 1615310030
#Igor Menezes Sales Vieira - 1615310007
#Matheus Mota de Souza - 1615310016
#Nadine da Cunha Brito - 1615310040
#Nickso Patrick Façanha Calheiros - 1615310059
#Thiago Santos Borges - 1615310023
#

sal_inicial = float(1000)

cont1 = 1995
cont2 = 0.015

while (cont1 < 2016):
    sal_final = sal_inicial + (sal_inicial*cont2)
    cont2 = cont2 * 2
    cont1 = cont1 +1
print("Salario atual é: %.2f" %sal_final)
