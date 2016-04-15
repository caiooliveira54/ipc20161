#Introduçao a programaçao de computadores
#Professor: Jucimar Junior
#Bruno de Oliveira Freire - 1615310030
#Thiago Santos Borges - 1615310023
#Nickso Patrick Façanha Calheiros - 1615310059
#Matheus Mota de Souza - 1615310016
#Igor Menezes Sales Vieira - 16153100
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
    
