#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033


#Questao4. Dada uma matriz real  Amxn, verificar se existem elementos repetidos em A


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


def verificarrepeticao(matriz, coluna, linha):
    vetor = []
    for j in range(coluna):
        for i in range(linha):
            x = matriz[i][j]
            vetor.append(x)
    w = len (vetor)
    num = 0
    c = 0
    d = 0
    for b in range (w):
        num = vetor[b]        
        for a in range(w):
            if num == vetor[a]:
                c += 1
    if c > 4:
        print ("A matriz possui elementos repetidos")
    else: 
        print ("A matriz nao possui elementos repetidos")
            
m = int(input("Digite o numero de linhas da matriz: "))
n = int(input("Digite o numero de colunas da matriz: "))
A = []  
A = fazermatriz(m,n)
mostrarmatriz(A, m, n)

verificarrepeticao(A, m, n)