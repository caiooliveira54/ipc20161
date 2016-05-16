#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 5
#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029
#

def criar_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            numero = int(input("linha %d,coluna %d:"%(i+1,j+1)))
            linha.append(numero)
        matriz.append(linha)
    return matriz

def criar_vetor(coluna):
    vetor = []
    for i in range(coluna):
        numero = int(input("Vetor coluna %d:"%(i+1)))
        vetor.append(numero)
    print("vetor")
    print(vetor)
    return vetor

def mostrar_matriz(matriz,linha):
    print("matriz")
    for i in range(linha):
        print(matriz[i])

def multiplicar_linhavetor(matriz,vetor):
    linha = len(matriz)
    coluna = len(matriz[0])
    resultado = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j] * vetor[j]
        resultado.append(acm)
    print("multiplicando")
    print(resultado)

def verificar_produto(vetor,produto):
    if vetor == produto:
        print("e o resultado")
    else:
        print("nao é a resposta")

def multiplicar_matriz(matriz_a,matriz_b):
    linha_a = len(matriz_a)
    coluna_a = len(matriz_a[0])
    linha_b = len(matriz_b)
    coluna_b = len(matriz_b[0])
    resultado = []
    for i in range(linha_a):
        linha = []
        for j in range(coluna_b):
            acm = 0
            for k in range(linha_b):
                acm += matriz_a[i][k]*matriz_b[k][j]
            linha.append(acm)
        resultado.append(linha)
    return resultado

def verificar_repeticao(matriz):
    vetor = []
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            vetor.append(matriz[i][j])
    if len(vetor) == len(set(vetor)):
        print ("Não existem elementos repetidos")
    else:
        print ("Existem elementos repetidos")

def verificar_permutacao (matriz,linha,coluna):
    for i in range (linha):
        ac = 0
        ac2 = 0
        for j in range(coluna):
            if matriz[i][j] == 0 or matriz[i][j]== 1: 
                if matriz[i][j] == 1:
                    ac += 1
                if matriz[j][i] == 1:
                    ac2 += 1
            else:
                return("Nao e de permutacao")
        if (ac == 1 and ac2 == 1):
            return("E de permutacao")
        else:
            return("Nao e permutacao")
        
def verificar_nulas (matriz,linha,coluna):
    ac_linha = 0
    ac_coluna = 0
    for i in range(linha):
        ac1 = 0
        ac2 = 0
        for j in range(coluna):
            if j < linha and i < coluna:
                if matriz[i][j] == 0:
                    ac1 += 1
                    if ac1 == linha or ac1 == coluna:
                        ac_linha += 1
            if j < linha and i < coluna:
                if matriz[j][i] == 0:
                    ac2 += 1
                    if ac2 == coluna or ac2 == linha:
                        ac_coluna += 1
    print("Numero de Linhas nulas %d, e numero de colunas nulas %d" %(ac_linha, ac_coluna))

def chamar_numero():
    numero = int(input("digite um numero: "))
    return numero

def fatorar_numero(numero):
    if (numero == 1) or (numero == 0):
        return 1
    else:
        n = numero - 1
        return numero * fatorar_numero(n)
    
def analisar_combinacao(numero,acm):
    resultado = fatorar_numero(numero) / (fatorar_numero(acm) * fatorar_numero(numero - acm))
    return resultado

def fazer_triangulo(numero):
    for numero in range(0,numero + 1):
        triangulo = []
        for acm in range(0,numero + 1):
            triangulo.append(int(analisar_combinacao(numero, acm)))
        print (triangulo)

def botar_vetor(numero):
    vetor = []
    for numero in range(0,numero + 1):
        triangulo = []
        for acm in range(0,numero + 1):
            resultado = int(fatorar_numero(numero) / (fatorar_numero(acm) * fatorar_numero(numero - acm)))
            vetor.append(resultado)
    print(vetor)

def gerar_tabuleiro():
    number = 0
    tabuleiro = []
    for i in range(0,8):
        linha = []
        for j in range(0,8):
            linha.append(number)
        tabuleiro.append(linha)
    return tabuleiro

def botar_pecas(matriz):
    for i in range(3):
        if i == 3 or i == 1:
            for j in range(8):
                if  j == 1 or j == 3 or j == 5 or j == 7:
                    matriz[i][j] = matriz[i][j] + 1
        else:
            for j in range(8):
                if  j == 0 or j == 2 or j == 4 or j == 6 or j == 8:
                    matriz[i][j] = matriz[i][j] + 1
    acm = 8 - 3
    acm_n = 8

    for k in range(acm,acm_n):
        if k == 6:
            for j in range(8):
                if  j == 1 or j == 3 or j == 5 or j == 7:
                    matriz[k][j] = matriz[k][j] - 1
        elif k == 5 or k == 7:
            for j in range(8):
                if  j == 0 or j == 2 or j == 4 or j == 6 or j == 8:
                    matriz[k][j] = matriz[k][j] - 1


    return matriz

def arrumar_tabuleiro(matriz):
    print ("   0  1  2  3  4  5  6  7")
    al = 0
    for i in range(0,8):
        print (al,matriz[i])
        al += 1


def mostrar_peca(matriz):
    origem = []
    opicao1 = []
    opicao2 = []
    resultado = []
    d = 0
    
    x = int(input("digite a ordenada da peça que queira mover: "))
    y = int(input("digite a abscissa da peça: "))
    origem.append(x)
    origem.append(y)
    resultado.append(origem)
    if matriz[x][y] == 1:
        x += 1  
        d = y
        d -= 1
        y += 1
        if d == -1:
            if matriz[x][y] == 0:
                opicao1.append(x)
                opicao1.append(y)
                resultado.append(opicao1)
                    
                print("opções de jogada %d,%d" %(x,y))
            else:
                print("pecas com movimentos invalidos")
                mostrar_peca(matriz)
        elif y == 8:
            if matriz[x][d] == 0:
                opicao1.append(x)
                opicao1.append(d)
                resultado.append(opicao1)
                    
                print("opções de jogada %d,%d" %(x,d))
            else:
                print("pecas com movimentos invalidos")
                mostrar_peca(matriz)
              
        elif matriz[x][d] == 0 or matriz[x][y] == 0:
            opicao1.append(x)
            opicao1.append(d)
            opicao2.append(x)
            opicao2.append(y)
            resultado.append(opicao1)
            resultado.append(opicao2)
            print("opções de jogada %d,%d ou %d,%d" %(x,d,x,y))
                
        elif matriz[x][y] != 1:
            print("peça invalida")
            mostrar_peca(matriz)

        else:
            print("pecas com movimentos invalidos")
            mostrar_peca(matriz)
        
    if matriz[x][y] == -1:
        x -= 1
        d = y
        d -= 1
        y += 1
        if d == -1:
            if matriz[x][y] == 0:
                opicao1.append(x)
                opicao1.append(y)
                resultado.append(opicao1)
                print("opções de jogada %d,%d" %(x,y))
            else:
                print("pecas com movimentos invalidos")
                mostrar_peca(matriz)
        elif y == 8:
            if matriz[x][d] == 0:
                opicao1.append(x)
                opicao1.append(d)
                resultado.append(opicao1)
                print("opções de jogada %d,%d" %(x,d))
            else:
                print("pecas com movimentos invalidos")
                mostrar_peca(matriz)
        elif matriz[x][d] == 0 or matriz[x][y] == 0:
            opicao1.append(x)
            opicao1.append(d)
            opicao2.append(x)
            opicao2.append(y)
            resultado.append(opicao1)
            resultado.append(opicao2)
            print("opções de jogada %d,%d ou %d,%d" %(x,d,x,y))
        elif matriz[x][y] != -1:
            print("peça invalida")
            mostrar_peca(matriz)
        else:
            print("pecas com movimentos invalidos")
            mostrar_peca(matriz)

    return resultado
        
        
def mover_pecab(matriz):
    arm = mostrar_peca(matriz)
    tam = len(arm)
    origem = arm[0]
    destino1 = arm[1]
    m = destino1[0]
    m = m - 1
    if origem[0] == m:
        if tam == 2:
            resposta = input("voce quer fazer essa jogada((n) para nao e (s) para sim)? ")
            if resposta == "s":
                matriz[origem[0]][origem[1]] = 0
                matriz[destino1[0]][destino1[1]] = 1
                print(arrumar_tabuleiro(matriz))

            else:
                mover_pecab(matriz)
        if tam == 3:
            resposta = input("voce quer fazer uma das duas jogadas posiveis((n) para nao e (s) para sim)? ")
            if resposta == "s":
                destino2 = arm[2]
                matriz[origem[0]][origem[1]] = 0
                escolha = input("qual das jogadas voce quer fazer((p)para o primeiro e (s) para o segundo))? ")
                if escolha == "p":
                    matriz[destino1[0]][destino1[1]] = 1
                    print(arrumar_tabuleiro(matriz))
                else:
                    matriz[destino2[0]][destino2[1]] = 1
                    print(arrumar_tabuleiro(matriz))
            else:
                mover_pecab(matriz)
    else:
        print("digite uma coordenada de peca branca")
        mover_pecab(matriz)
        
def mover_pecap(matriz):
    arm = mostrar_peca(matriz)
    tam = len(arm)
    origem = arm[0]
    destino1 = arm[1]
    m = destino1[0]
    m = m + 1
    if origem[0] == m:
        if tam == 2:
            resposta = input("voce quer fazer essa jogada((n) para nao e (s) para sim)? ")
            if resposta == "s":
                matriz[origem[0]][origem[1]] = 0
                matriz[destino1[0]][destino1[1]] = 1
                print(arrumar_tabuleiro(matriz))

            else:
                mover_pecap(matriz)
        if tam == 3:
            resposta = input("voce quer fazer uma das duas jogadas posiveis((n) para nao e (s) para sim)? ")
            if resposta == "s":
                destino2 = arm[2]
                matriz[origem[0]][origem[1]] = 0
                escolha = input("qual das jogadas voce quer fazer((p)para o primeiro e (s) para o segundo))? ")
                if escolha == "p":
                    matriz[destino1[0]][destino1[1]] = 1
                    print(arrumar_tabuleiro(matriz))
                else:
                    matriz[destino2[0]][destino2[1]] = 1
                    print(arrumar_tabuleiro(matriz))
            else:
                mover_pecap(matriz)
    else:
        print("digite uma coordenada de peca branca")
        mover_pecap(matriz)

def ordem_jogada(matriz):
    acm = 0
    while acm < 2:
        if acm == 0:
            mover_pecab(matriz)
        if acm == 1:
            mover_pecap(matriz)
            acm = 0

def somar_linha(matriz,linha,coluna,acms):
    acms = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[i][j]
        acms.append(acm)
    return (acms)

def somar_coluna(matriz,linha,coluna,acms):
    acms = []
    for i in range(linha):
        acm = 0
        for j in range(coluna):
            acm += matriz[j][i]
        acms.append(acm)
    return acms

def somar_diagonal(matriz,linha,coluna,acm,acm1):
    for i in range(linha):
        for j in range(coluna):
            if (i == j):
                acm += matriz[i][j]
            if ((i+j) == (linha-1)):
                acm1 += matriz[i][j]
    return acm, acm1

def verificar_cubo(lista):
    cont = 0
    for i in lista:
        if i == lista[0]:
            cont += 1
    if cont == len(lista):
        print ("e um cubo magico")
    else:
        print ("nao e um cubo magico")

def ver_matriz(matriz,linha,coluna):
    cont = 1
    if(matriz[0][0] == 0 and  matriz[0][1] == 0 or  matriz[1][0] == 0):
        matriz[0][0] = cont
        cont += 1
    for i in range(linha):
        for j in range(coluna):            
            if(matriz[i][j] != -1 and matriz[i-1][j-1] != 0):
                matriz[i][j] = cont
                cont += 1
    return matriz
