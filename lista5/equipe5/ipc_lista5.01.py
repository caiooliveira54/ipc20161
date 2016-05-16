#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

from matriz import*

linha = int(input("Quantas linhas tem sua matriz? "))
coluna = int(input("Quantas colunas tem sua matriz? "))
matriz = criar_matriz(linha,coluna)
vetor = criar_vetor(coluna)
mostrar_matriz(matriz,linha)
multiplicar_linhavetor(matriz,vetor)
