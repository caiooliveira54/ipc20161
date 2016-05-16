#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#
from matriz import*
soma1 = []
soma2 = []
acm1 = 0
acm2 = 0

tamL = int(input("Digite a ordem da matriz: "))
tamC = tamL
print("--------------------------------------------------")

matriz = gerar_matriz(tamL, tamC)
print("--------------------------------------------------")
mostrar_matriz3(matriz, tamL)
print("--------------------------------------------------")
#Processamento
verificaL = verificar_linhas(matriz, tamL, tamC, soma1)
verificaC = verificar_colunas(matriz, tamL, tamC, soma2)
verificaD = verificar_diagonais(matriz, tamL, tamC, acm1, acm2)

verificaL.extend(verificaC)
verificaL.extend(verificaD)

#Processamento do Resultado
verificar_cubo(verificaL)
