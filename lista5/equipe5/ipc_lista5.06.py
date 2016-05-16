#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

from matriz import*

m=int(input("Numero de linhas: "))
n=int(input("Numero de colunas: "))
matriz = criar_matriz(m,n)
mostrar_matriz(matriz,m)
verificar_nulas(matriz,m,n)
