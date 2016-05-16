#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

from matriz import*

resultado = int(input("Elementos do vetor resultado: "))
vetor_teste = criar_vetor(resultado)
linha = int(input("digite a quantidade de linhas: "))
coluna = int(input("digite a quantidade de colunas: "))
matriz = criar_matriz(linha,coluna)
vetor = criar_vetor(coluna)
resposta = multiplicar_linhavetor(matriz,vetor)
verificar_produto(resposta,resultado)
