#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo Rocha Melo - 1615310015
#Lucas Ferreira Soares - 1615310014

from matriz import*
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
