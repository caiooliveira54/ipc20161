# Victor Rafael da Silva e Silva 1615310025 

vet = []
vet_inpar = []
vet_par = []

for i in range(20):
    valor = int(input("Digite um numero: "))
    vet.append(valor)
    if valor%2==0:
        vet_par.append(valor)
    else:
        vet_inpar.append(valor)

print(vet)
print(vet_inpar)
print(vet_par)