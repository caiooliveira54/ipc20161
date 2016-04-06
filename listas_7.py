vetor = []
multiplicacao = 1
soma = 0

for i in range(1,6):
    dado = int(input("Digite o dado: "))
    vetor.append(dado)
    multi = multiplicacao * dado
    soma = soma + dado

print("O numeros informados foram: ",vetor)
print("A soma:%d"%soma)
print("A multiplicacao:%d"%multiplicacao)
