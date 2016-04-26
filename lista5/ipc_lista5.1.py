# Ana Beatriz Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Nahan Trindade Passos - 1615310021 

def gerar_matriz(m, n):
    matriz = []
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            num = int(input("A(%d%d):\t"%(i, j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def gerar_vetor(n):
    vetor = []
    for i in range(n):
        num = int(input("V(%d): \t"%(i)))
        vetor.append(num)
    return vetor

linhas = int(input("Quantidade de linhas: "))
colunas = int(input("Quantidade de colunhas: "))
matriz = gerar_matriz(linhas, colunas)
vetor = gerar_vetor(colunas)
print ("Matriz =", matriz)
print ("Vetor =", vetor)

produto = []
for i in range(linhas):
    acm = 0
    for j in range(colunas):
        acm += matriz[i][j] * vetor[j]
    produto.append(acm)

print ("Matriz * Vetor =", produto)
    
