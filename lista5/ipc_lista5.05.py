#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

from matriz import*

m = int(input("quantidade de linhas: " ))
n = int(input("quantidade de colunas: "))
matriz = []
matriz = gerar_matriz(m,n)
mostrar_matriz(matriz, m)
x = verificar_permutacao(matriz,m,n)
print(x)
