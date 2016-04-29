from matriz import*

m = int(input( ))
n = int(input( ))
matriz = []
matriz = gerar_matriz(m,n)
arrumar_matriz(matriz, m)
x = verificar_permutaçao(matriz,m,n)
print(x)
