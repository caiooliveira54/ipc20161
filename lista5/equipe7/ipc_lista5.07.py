#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Gonçalves dos Santos - 1615310033

#Questão7.  Dizemos que uma matriz quadrada inteira é um quadrado mágico (1) se a soma dos elementos de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.  Dada uma matriz quadrada Anxn , verificar se A é um quadrado mágico.  


def fazermatriz (linha, coluna):
    matriz =[]
    for i in range (1, linha+1):
        linha = []
        for j in range (1, coluna+1):
            num = int(input("Digite a posicao %i%i da matriz: " %(i,j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def mostrarmatriz(matriz, linha, coluna):
    for i in range(linha):
        print (matriz[i]) 
        
def verificardiagonalP(matriz, linha, coluna):
    diagp = 0
    diags = 0
    j = 0
    for i in range (linha):
        diagp += matriz[i][j]
        j +=1
    
    for i in range(coluna):
        for j in range (linha):
            if i + j == linha - 1:
                diags += matriz[i][j]
    
    col = []  
    lin = []
    y = 0
    d = 0
    for a in range (linha):
        x = 0
        i = 0
        for j in range (coluna):
            x += matriz[i][j]
        col.append(x)
        y = 0
        i = 0
        for j in range (coluna):
            y += matriz[j][i]
        lin.append(y)
    w = len (lin)
   
    iguald = 0
    igualV = 0
    if diags == diagp:
        iguald = diags
        for c in range (w):
            if lin [c] == col [c]:
                igualV = lin[c]
        if iguald == igualV:
            print ("Quadrado perfeito")
        else:
            print("Nao e um quadrado perfeito")    
            
    
            
       
m = int(input("Digite o numero de linhas da matriz: "))
n = int(input("Digite o numero de colunas da matriz: "))
A = []  
A = fazermatriz(m,n)
mostrarmatriz(A, m, n)
verificardiagonalP(A, m, n)