#
#Igor Menezes Sales Vieira - Matricula: 1615310007
#
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
vetor_par = []
vetor_impar = []
v = len(numeros)
i = 0
for i in range(v):
    if(numeros[i] % 2 == 0):
        vetor_par.append(numeros[i])
    else:
        vetor_impar.append(numeros[i])
    i+=1
print("Primeiro vetor = ",numeros)
print("Vetor par = ",vetor_par)
print("Vetor impar = ",vetor_impar)
