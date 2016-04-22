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

preco=float(input("informe o preco do pao:\n"))
cont=1
soma=0
nume=0
print("preco do pao:R$ %.2f"%preco)
print("panificadora pao  de ontem - tabela de precos")
while(cont<=50):
    soma=soma+preco
    nume+=1
    print("%d R$%.2f"%(nume,soma))
    cont+=1
