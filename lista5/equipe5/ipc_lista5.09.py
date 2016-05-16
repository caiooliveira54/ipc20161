from matriz import*

linha = int(input("Quantidade de linhas na matriz: "))
coluna = int(input("Quantidade de colunas na matriz: "))
matriz = criar_matriz(linha,coluna)
mostrar_matriz((ver_matriz(matriz,linha,coluna)),linha)
