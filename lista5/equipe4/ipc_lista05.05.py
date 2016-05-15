#Introdução a programação de computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo de Rocha Melo - 1615310015

def gerar_matriz(m, n):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            valor = int(input("Matriz %d%d: "%(i, j)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def verificar_permutaçao(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    permutacao = True
    qtzl = 0
    qtzc = 0
    if(linhas != colunas):
        return False
    else:
        for i in range(linhas):
            for j in range(colunas):
                if(matriz[i][j] == 1):
                    for k in range(colunas):
                        if(matriz[i][k] == 0):
                            qtzc += 1
                        if(matriz[k][j] == 0):
                            qtzl += 1
                
                    if (qtzl != linhas-1) or (qtzc != colunas-1):
                        return False
                    qtzc = 0
                    qtzl = 0
        return permutacao
            
def mostrar_matriz(matriz):
    for i in range(linhas):
        print(matriz[i])

linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))
matriz = gerar_matriz(linhas, colunas)
print(verificar_permutaçao(matriz))
mostrar_matriz(matriz)

