
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
    