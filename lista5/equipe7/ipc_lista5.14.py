#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Gonçalves dos Santos - 1615310033


#Questão14. Os elementos aij de uma matriz inteira Anxn representam os custos de transporte da cidade i para a cidade j. Dados n itinerários, cada um com k cidades, calcular o custo total para cada itinerário.


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
        
def montaritinerario(matriz, linha, coluna):
    soma = 0
    vetor =[]
    for j in range(linha * 2):
        x = int(input("Digite o itinerario que voce deseja saber o custo, numero por numero: "))
        if x >= linha:
            print("Este numero nao pertence ao itinerario")
            while x >= linha:
                x = int(input("Digite o itinerario que voce deseja saber o custo, numero por numero: "))
            vetor.append(x)
        else:
            vetor.append(x)
    w = len(vetor)
    j = 1
    for i in range(w):
        a = vetor[i]
        b = vetor[j]
        soma += matriz[a][b]
        j += 1
        if j >= w:
            break
    print("Itinerario: ", vetor)
    print ("O custo do itinerario e : ", soma)
    
                
m = int(input("Digite o numero de linhas da matriz do jogo: "))
n = int(input("Digite o numero de colunas da matrizdo jogo: "))
A = []  
A = fazermatriz(m,n)
mostrarmatriz(A, m, n)
montaritinerario(A,m, n)