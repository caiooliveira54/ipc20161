#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#
from matriz import*

tamL = int(input("Quantidade de linhas: "))
tamC = int(input("Quantidade de colunhas: "))

matriz = gerar_matriz(tamL, tamC)
vetor = gerar_vetor(tamC)

vetor_resultado = []
for i in range(tamL):
    acm = 0
    for j in range(tamC):
        acm += matriz[i][j] * vetor[j]
    vetor_resultado.append(acm)

print("--------------------------------------------------")
print ("Matriz =", matriz)
print("--------------------------------------------------")
print ("Vetor =", vetor)
print("--------------------------------------------------")
print ("Matriz * Vetor =", vetor_resultado)
