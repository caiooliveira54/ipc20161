#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

from matriz import*

linha = int(input("Quantidade de linhas na matriz: "))
coluna = int(input("Quantidade de colunas na matriz: "))
matriz = criar_matriz(linha,coluna)
mostrar_matriz((ver_matriz(matriz,linha,coluna)),linha)
