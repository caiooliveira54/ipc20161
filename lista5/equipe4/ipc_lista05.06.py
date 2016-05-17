#Introdução a programação de computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo de Rocha Melo - 1615310015

from matriz import*

m=int(input("Numero de linhas: "))
n=int(input("Numero de colunas: "))

matriz = []
matriz = gerar_matriz(m,n)

mostrar_matriz(matriz,m)

x = verificar_nulas(matriz,m,n)
print (x)
