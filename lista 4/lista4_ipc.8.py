#Beatriz Pessoa Longato 1615310001

idade= [] # Vetor que armazenará todas as idades que serão informadas pelo usuário
altura= [] # Vetor que armazenará todas as alturas que serão informadas pelo usuário

quantidade_pessoa= 5 # Variável que recebe a quantidade de pessoas que informarão a idade e altura

for i in range (quantidade_pessoa): # Enquanto o índice i estiver no alcance das 5 pessoas, ou seja, no intervalo 0 <= i < 5
    
    idade.append(int(raw_input("Digite sua idade: "))) # Solicitará ao usuário a sua idade e automaticamente, com seu índice, armazenará a idade no seu respectivo vetor
    
    altura.append(float(raw_input("Digite sua altura: "))) # Solicitará ao usuário a sua altura e automaticamente, com seu índice, armazenará a altura no seu respectivo vetor
    

print (idade) # Imprimirá o vetor idade com todas as idades em seus respectivos índices

print(list(reversed(idade))) # Imprimirá o vetor idade com todas as idades em seus respectivos índices invertidos

print (altura) # Imprimirá o vetor altura com todas as alturas em seus respectivos índices

print(list(reversed(altura))) # Imprimirá o altura idade com todas as alturas em seus respectivos índices invertidos


