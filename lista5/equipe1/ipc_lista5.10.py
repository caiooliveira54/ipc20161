#Introducao a programacao de computadores
#Professor: Jucimar Junior
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Nahan Trindade Passos - 1615310021

def criar_tabuleiro(m,n):
    for i in range(m):
        tabuleiro.append([])
        for j in range(n):
            tabuleiro[i].insert(j,0)
        
    return tabuleiro
tabuleiro = []

def organizar_tabuleiro(m,n):
    for i in range(m):
        for j in range(n):
            if i == 0 and j%2 == 0 :
                tabuleiro[i][j] = -1
            if i == 1 and j%2 != 0 :
                tabuleiro[i][j] = -1
            if i == 2 and j%2 == 0 :
                tabuleiro[i][j] = -1
            if i == 7 and j%2 != 0 :
                tabuleiro[i][j] = 1
            if i == 6 and j%2 == 0 :
                tabuleiro[i][j] = 1
            if i == 5 and j%2 != 0 :
                tabuleiro[i][j] = 1
             
    return tabuleiro

def mover_preta (linha_atual,coluna_atual,linha,coluna):
    for i in range(8):
            for j in range(8):
                if tabuleiro[linha_atual][coluna_atual] == -1 :
                    if linha == linha_atual+1 and coluna == coluna_atual-1 or coluna == coluna_atual+1:
                        if tabuleiro[linha][coluna] == 0:
                            tabuleiro[linha][coluna] = tabuleiro[linha_atual][coluna_atual]
                            tabuleiro[linha_atual][coluna_atual] = 0
                      
    return condicao_preta

def mover_branca (linha_atual,coluna_atual,linha,coluna):
    for i in range(8):
            for j in range(8):
                if tabuleiro[linha_atual][coluna_atual] == 1 :
                    if linha == linha_atual-1 and coluna == coluna_atual-1 or coluna == coluna_atual+1:
                        if tabuleiro[linha][coluna] == 0:
                            tabuleiro[linha][coluna] = tabuleiro[linha_atual][coluna_atual]
                            tabuleiro[linha_atual][coluna_atual] = 0
                           
    return condicao_branca

def mostrar_tabuleiro(m,n):
    for i in range(8):
        print(tabuleiro[i])
    return tabuleiro

    
criar_tabuleiro(8,8)

organizar_tabuleiro(8,8)

print("Bem vindo ao DAMAS... Versão Pré-Alfa 0.2\n Apenas 10 rodadas")


condicao_branca = ""
condicao_preta = ""
contador = 0

mostrar_tabuleiro(8,8)
print("---Jogador das peças brancas---")
linha_atual = int(input("Informe a linha da peça que deseja mover:\n"))
coluna_atual = int(input("Informe a coluna da peça que deseja mover:\n"))
linha = int(input("Informe a linha da posição que deseja mover:\n"))
coluna = int(input("Informe a linha da posição que deseja mover:\n"))
mover_branca(linha_atual,coluna_atual,linha,coluna)
       
mostrar_tabuleiro(8,8)

    
print("---Jogador das peças pretas---")
linha_atual = int(input("Informe a linha da peça que deseja mover:\n"))
coluna_atual = int(input("Informe a coluna da peça que deseja mover:\n"))
linha = int(input("Informe a linha da posição que deseja mover:\n"))
coluna = int(input("Informe a linha da posição que deseja mover:\n"))
mover_preta(linha_atual,coluna_atual,linha,coluna)
mostrar_tabuleiro(8,8)

    
    
