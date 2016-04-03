#Beatriz Pessoa Longato 1615310001
#Equipe 3
#Algoritmo criado no python 2.7.10
#Sintam-se livres para fazer alterações e atualizações

vetor = list(range(30))
vetor_a = list(range(10))
vetor_b = list(range(10))
vetor_c = list(range(10))
a = 0
b = 0
c = 0
aux = 1
preencher = False

for i in range(10):
    vetor_a[i] = int(input("Insira um numero: "))

for i in range(10):
    vetor_b[i] = int(input("Insira um numero: "))

for i in range(10):
    vetor_c[i] = int(input("Insira um numero: "))
    
for i in range(10):
    preencher = False
    if aux == 1 and preencher == False:
        vetor[i] = vetor_a[a]
        a += 1
        aux = 2
        preencher = True
    if aux == 2 and preencher == False:
        vetor[i] = vetor_b[b]
        b += 1
        aux = 3
        preencher = True
    if aux == 3 and preencher == False:
        vetor[i] = vetor_c[c]
        c += 1
        aux = 1
        preencher = True

print ("Vetor A=", vetor_a)
print ("Vetor B", vetor_b)
print ("Vetor C", vetor_c)
print ("Intercalando A+B+C=", vetor)
