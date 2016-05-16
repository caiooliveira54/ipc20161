#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#
from matriz import*

l = int(input("Quantas linhas voce quer apos a primeira? "))
print("--------------------------------------------------")
vetor = []
for l in range(0,l+1):
    vet = []
    for i in range(0,l+1):
        vet.append(int(analisea_triangulo(l,i)))
        vetor.append(int(analisea_triangulo(l,i)))
    print(vet)
print("--------------------------------------------------")
print("RESULTADO EM UM VETOR")
print(vetor)