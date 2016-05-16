#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

from matriz import*

linha = int(input("quantidade de linhas: " ))
coluna = int(input("quantidade de colunas: "))
matriz = criar_matriz(linha,coluna)
mostrar_matriz(matriz, linha)
resultado = verificar_permutacao(matriz,linha,coluna)
print(resultado)
