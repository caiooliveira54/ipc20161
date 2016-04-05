#questao 11
vetor1 = [1,3,5,7,9,11,13,15,17,19]
vetor2 = [2,4,6,8,10,12,14,16,18,20]
vetor3 = [100,200,300,400,500,600,700,800,900,1000]
vetor4 = []
i=0
v = len(vetor1)
for i in range(v):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])
    i+=1
print("Vetor1 = ",vetor1)
print("Vetor2 = ",vetor2)
print("Vetor3 = ",vetor3)
print("Vetor4 = ",vetor4)
