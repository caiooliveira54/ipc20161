

from matriz import*

linha = int(input("Quantas linhas tem sua matriz? "))
coluna = int(input("Quantas colunas tem sua matriz? "))
matriz = criar_matriz(linha,coluna)
mostrar_matriz(matriz,linha)
verificar_repeticao(matriz)
