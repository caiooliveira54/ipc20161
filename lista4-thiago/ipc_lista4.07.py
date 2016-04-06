#ipc_lista4.07
#Thiago Santos Borges - Matrícula - 1615310023
#
vetor = []
multi = 1
soma = 0

for i in range(1,6):
    dado = int(input("Informe o dado:"))
    vetor.append(dado)
    multi = multi * dado
    soma = soma + dado

print("O numeros informados foram:",vetor)
print("A soma:%d"%soma)
print("A multiplicacao:%d"%multi)
