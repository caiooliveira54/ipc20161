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

q_cds = float(input("informe a quantidade de cds:\n"))
cont = 0
valor_total = 0
numero = 0

while (cont<q_cds):
    numero+=1
    valor=float(input("informe quanto custa o cd %d:"%numero))
    valor_total=valor_total+valor
    media=valor_total/q_cds
    cont+=1
    
print("esse e o valor total:%.2f"%valor_total)
print("essa e a media:%.2f"%media)
