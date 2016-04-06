# Victor Rafael da Silva e Silva 1615310025 

vet = []
vet_1=[]
vet_2=[]
for i in range(5):
    valor = int(input("Vetor 1 - Digite um numero: "))
    vet_1.append(valor)

for i in range(5):
    valor = int(input("Vetor 2 - Digite um numero: "))
    vet_2.append(valor)
    
for i in range(5):
    valor = vet_1[i]
    vet.append(valor)
    valor = vet_2[i]
    vet.append(valor)

print(vet_1)
print(vet_2)    
print(vet)    

    
