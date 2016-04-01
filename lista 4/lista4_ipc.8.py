#Beatriz Pessoa Longato 1615310001

idade= []
altura= []

quantidade_pessoa= 5

for i in range (quantidade_pessoa):
    
    idade.append(int(raw_input("Digite sua idade: ")))
    
    altura.append(float(raw_input("Digite sua altura: ")))
    

print (idade)

print(list(reversed(idade)))

print (altura)

print(list(reversed(altura)))

