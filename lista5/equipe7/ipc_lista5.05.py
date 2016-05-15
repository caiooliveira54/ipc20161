#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033


#Questao5.  Dizemos que uma matriz inteira Anxn  � uma matriz de permuta��o se em cada linha e em cada coluna houver n-1 elementos nulos e um unico elemento igual a 1. 

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
        
def verificarpermutacao(matriz, linha, coluna):
    num = 0
    col = 0     
    for j in range(coluna):    
        vetor = []
        for i in range(linha):
            x = matriz[i][j]
            vetor.append(x)
            w = len (vetor)  
            for a in range (w):
                for b in range (w):
                    if vetor[b] != 0:
                        num += 1
                        if num > 0 and vetor[b] != 1:
                            col += 1
    if col > w:
        print ("A matriz nao e de permutacao")
    else:
        print ("Matriz de permutacao")


m = int(input("Digite o numero de linhas da matriz: "))
n = int(input("Digite o numero de colunas da matriz: "))
A = []  
A = fazermatriz(m,n)
verificarpermutacao(A, m, n)
mostrarmatriz(A, m, n)
        
        
