#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#Luiz Alexandre Oliveira de Souza - 1615310057

from matriz import*

acms1 = []
acms2 = []
acm1 = 0
acm2 = 0
linha = int(input("digite o valor para ser matriz quadrada: "))
coluna = linha
matriz = criar_matriz(linha,coluna)
mostrar_matriz(matriz,linha)
a = somar_linha(matriz,linha,coluna,acms1)
b = somar_coluna(matriz,linha,coluna,acms2)
c = somar_diagonal(matriz,linha,coluna,acm1,acm2)
a.extend(b)
a.extend(c)
verificar_cubo(a)
