#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
A = []
soma = 0
quadrado = 1

for i in range(10):
    numerox = int(input("Informe o numero: "))
    A.append(numerox)

for i in A:
    quadrado = i**2
    soma = soma+quadrado

print("A soma dos quadrados e: %d"%soma)
