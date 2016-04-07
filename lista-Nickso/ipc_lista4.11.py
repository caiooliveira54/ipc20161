# Nickso Patrick Façanha Calheiros - 1615310059

vetor1 = [1,4,7,10,13,16,19,22,25,28]
vetor2 = [2,5,8,11,14,17,20,23,26,29]
vetor3 = [3,6,9,12,15,18,21,24,27,30]
vetor4 = []
cont = 0
ind1 = len(vetor1)
ind2 = len(vetor2)
ind3 = len(vetor3)
while cont < ind1 or cont < ind2 or cont < ind3:
    vetor4.append(vetor1[cont])
    vetor4.append(vetor2[cont])
    vetor4.append(vetor3[cont])
    cont += 1
print (vetor4)
