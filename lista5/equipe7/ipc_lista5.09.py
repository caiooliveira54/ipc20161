#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Gonçalves dos Santos - 1615310033

#Questão9. Um jogo de palavras cruzadas pode ser representado por uma matriz  Amxn  onde cada posição da matriz corresponde a um quadrado do jogo, sendo que 0 indica um quadrado branco e -1 indica um quadrado preto. Indicar na matriz as posições que são início de palavras horizontais e/ou verticais nos quadrados correspondentes (substituindo os zeros), considerando que uma palavra deve ter pelo menos duas letras. Para isso, numere consecutivamente tais posições 


def fazermatriz (linha, coluna):
    matriz =[]
    for i in range (1, linha+1):
        linha = []
        for j in range (1, coluna+1):
            num = int(input("Digite a posicao %i%i da matriz do seu jogo com 0 para os quadrados em branco e -1 para os pretos: " %(i,j)))
            linha.append(num)
        matriz.append(linha)
    return matriz

def alterarmatriz(matriz, linha, coluna):
    Ex = [[00, 01, 02, 03, 04], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24]]
    h = 3
    c = 5
    for k in range (linha):
        for f in range (coluna):
            print ("Indique na matriz as posicoes que nao sao inicio de palavras horizontais e/ou verticais com excecao das que ja possuem -1\n")
            print ("Exemplo de posicoes da matriz, leve em consideracao as dimensoes da sua matriz:")
            mostrarmatriz(Ex, 3, 5)
            print ("Numeros do lado esquerdo representam a linha e do lado direito a coluna, onde nao aparecer numeros do lado direito significa 0")
            i = int(input("Digite a linha :"))
            j = int(input("Digite a coluna :"))
            if matriz[i][j] != -1:
                matriz[i][j] = h + c
                h += 2
                c += 1
            else:
                print("Esta posicao possui -1")
        s = int(input("Digite 0 para parar de alterar ou 1 para continuar"))
        if s == 0:
            break
    print("Matriz alterada:")
    mostrarmatriz(matriz,linha,coluna)

def mostrarmatriz(matriz, linha, coluna):
    for i in range(linha):
        print (matriz[i])
            
        
m = int(input("Digite o numero de linhas da matriz: "))
n = int(input("Digite o numero de colunas da matriz: "))
A = []  
A = fazermatriz(m,n)
mostrarmatriz(A, m, n)
alterarmatriz(A, m, n)
