#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#
def itinerario(matriz, itinerariov):
    acum = 0
    for i in range(len(itinerariov)-1):
        acum += (matriz[(int(itinerariov[i]))][int((itinerariov[i+1]))])
    return acum
def produzir_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("A(%s%s): "%(i,j)))
            linha.append(numero)
        matriz.append(linha)
    return matriz
def visualizar_matriz(matriz,linha):
    for i in range(linha):
        print(matriz[i])


linha = int(input("Informe o numero de linhas da matriz quadrada:"))
coluna = linha
itinerariov = str(input("Itinerario:"))
matriz= produzir_matriz(linha,coluna)
visualizar_matriz(matriz,linha)
print("O custo total do itinerario sera: R$ %s"%itinerario(matriz,itinerariov))

        

      
        
