#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

from matriz import*

m = (int(input("digite a quantidade de linhas da primeira matriz: ")))
n = (int(input("digite a quantidade de linhas da primeira matriz e de colunas para a segunda: ")))
p = (int(input("digite a quantidade de colunas da segunda matriz: ")))
matriz_a = criar_matriz(m,n)
matriz_b = criar_matriz(n,p)
matriz_c = multiplicar_matriz(matriz_a,matriz_b)
mostrar_matriz(matriz_a,m)
mostrar_matriz(matriz_b,m)
mostrar_matriz(matriz_c,m)
