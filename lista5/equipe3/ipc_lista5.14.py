#Introducao a programacao de computadores
#Professor: Jucimar Junior
#samuel silva de frança - 1615310049
#bruno de oliveira freire - 1615310030
#Felipe Henrique Bastos Costa - 1615310032

def criar_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        listainterna = []
        for j in range(colunas):
            num = int(input("A(%d%d): "%(i+1,j+1)))
            listainterna.append(num)
        matriz.append(listainterna)
    return matriz
def calcular_itinerario(matriz,linhas,colunas):
    cond = True
    iti = 0
    soma = 0
    listainterna = []
    while cond:
        if iti == -1:
            cond = False
        else:
            print("Informe o itinerario do transporte, sendo estes o numero da coluna ou linha da matriz:")
            iti = int(input("digite -1 se já terminou: "))
            listainterna.append(iti-1)
            cond = True
    itinerario = []
    for i in range(len(listainterna)-2):
        itinerario.append(matriz[listainterna[i]][listainterna[i+1]])
    for i in range(len(itinerario)):
        soma += itinerario[i]
    return soma
def montar_matriz(matriz,linhas):
    for i in range(linhas):
        print matriz[i]

linhas = int(input("Informe quantas linhas têm a matrizA:\n"))
colunas = int(input("Informe quantas colunas têm a matrizA:\n"))
matrizA = criar_matriz(linhas,colunas)
montar_matriz(matrizA,linhas)
soma = calcular_itinerario(matrizA,linhas,colunas)
print soma