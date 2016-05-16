#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#
from matriz import*
print("----------Matriz----------")
tamL = int(input("Quantidades de linhas: "))
tamC = int(input("Quantidades de colunas: "))

matriz = gerar_matriz(tamL,tamC)
print("--------------------------------------------------")
mostrar_matriz(matriz,tamL)
print("--------------------------------------------------")

verifica = verificar_permutacao(matriz,tamL,tamC)
print(verifica)
