#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#
from matriz import*

print("Digite o tamanho da matriz A")
tamLA = int(input("Quantidades de linhas: "))
tamCA = int(input("Quantidades de colunas: "))
print("Matriz A")
matrizA = gerar_matriz(tamLA,tamCA)

print("--------------------------------------------------")
print("Digite o tamanho da matriz B")
tamLB = int(input("Quantidades de linhas: "))
tamCb = int(input("Quantidades de colunas: "))

if tamCA != tamLB:
    print("Nao existe produto da matriz A por B")
else:
    print("Matriz B")
    matrizB = gerar_matriz(tamLB,tamCb)
    matrizC = multiplicar_matrizes(matrizA,matrizB)
    print("Matriz A * Matriz B -> ",matrizC)

