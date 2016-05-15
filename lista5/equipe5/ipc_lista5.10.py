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
    
    x = int(input("digite a odernada da peça que queira mover: "))
    y = int(input("digite a abicissa da peça: "))
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
                    
                print("opições de jogada %d,%d" %(x,y))
            else:
                print("pecas com movimentos invalidos")
                mostrar_peca(matriz)
        elif y == 8:
            if matriz[x][d] == 0:
                opicao1.append(x)
                opicao1.append(d)
                resultado.append(opicao1)
                    
                print("opições de jogada %d,%d" %(x,d))
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
            print("opições de jogada %d,%d ou %d,%d" %(x,d,x,y))
                
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
                print("opições de jogada %d,%d" %(x,y))
            else:
                print("pecas com movimentos invalidos")
                mostrar_peca(matriz)
        elif y == 8:
            if matriz[x][d] == 0:
                opicao1.append(x)
                opicao1.append(d)
                resultado.append(opicao1)
                print("opições de jogada %d,%d" %(x,d))
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
            print("opições de jogada %d,%d ou %d,%d" %(x,d,x,y))
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
        
t =gerar_tabuleiro()
matriz =botar_pecas(t)
arrumar_tabuleiro(matriz)
ordem_jogada(matriz)
