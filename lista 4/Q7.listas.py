#Eduardo Maia Freire
vetor1 = [1,2,3,4,5]
x = 0
v1 = len(vetor1)
soma = 0
mult = 1
for x in range(v1):
    soma = soma + vetor1[x]
    mult = mult * vetor1[x]
    print(vetor1[x])
print("Soma dos numeros = ",soma)
print("Multiplicaçao dos numeros = ",mult)
print("Vetor 1 = ",vetor1)
