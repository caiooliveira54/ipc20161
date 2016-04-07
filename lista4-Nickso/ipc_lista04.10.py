vetor1 = [1,3,5,7,9,11,13,15,17,19]
vetor2 = [2,4,6,8,10,12,14,16,18,20]
vetor3 = []
cont = 0
ind1 = len(vetor1)
ind2 = len(vetor2)

while cont < ind1 or cont < ind2:
    vetor3.append(vetor1[cont])
    vetor3.append(vetor2[cont])
    cont = cont + 1
print (vetor3)
