#
#Introdução a Programação de Computadores
#Professor: Jucimar JR.
#EQUIPE 1
#
#Any Mendes Carvalho - 1615310044
#Kid Mendes de Oliveira Neto - 1615310011
#Victor Rafael da Silva e Silva - 1615310025
#Eduardo Maia Freire - 1615310003
#Luiz Gustavo de Rocha Melo - 1615310015
#Matheus Palheta Barbosa -1615310019
#
# Jogo da Velha

from random import *

tabuleiro_velha=["_","_","_","_","_","_","_","_","_"]
posicoes=[1,2,3,4,5,6,7,8,9]
i = 0            
numero_de_jogadas_player = 0
fim_de_jogo = False
cond = False
cond1 = False
cond_verdade = False
cond2 = False
end = False 

def imprimir_tabela():
    print("\n|-----Posicoes------|----Jogo da Velha----|")
    print("|    _%s_|_%s_|_%s_    |     _%s_|_%s_|_%s_     |" %(posicoes[6],posicoes[7],posicoes[8],tabuleiro_velha[6],tabuleiro_velha[7],tabuleiro_velha[8]))
    print("|    _%s_|_%s_|_%s_    |     _%s_|_%s_|_%s_     |" %(posicoes[3],posicoes[4],posicoes[5],tabuleiro_velha[3],tabuleiro_velha[4],tabuleiro_velha[5]))
    print("|     %s | %s | %s     |      %s | %s | %s      |" %(posicoes[0],posicoes[1],posicoes[2],tabuleiro_velha[0],tabuleiro_velha[1],tabuleiro_velha[2]))
    print("|-------------------|---------------------|\n")


            
while numero_de_jogadas_player < 5 :
#Verificar Vitoria/Derrota
    if(tabuleiro_velha[0]=="X" and tabuleiro_velha[1]=="X" and tabuleiro_velha[2]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[3]=="X" and tabuleiro_velha[4]=="X" and tabuleiro_velha[5]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[6]=="X" and tabuleiro_velha[7]=="X" and tabuleiro_velha[8] == "X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[0]=="X" and tabuleiro_velha[3] == "X" and tabuleiro_velha[6] == "X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[1]=="X" and tabuleiro_velha[4]=="X" and tabuleiro_velha[7]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[2]=="X" and tabuleiro_velha[5] == "X" and tabuleiro_velha[8]== "X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[0]=="X" and tabuleiro_velha[4]=="X" and tabuleiro_velha[8]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[6]=="X" and tabuleiro_velha[4]=="X" and tabuleiro_velha[2]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    else:
        if(fim_de_jogo == False):
            fim_de_jogo = False
    if(tabuleiro_velha[0]=="O" and tabuleiro_velha[1]=="O" and tabuleiro_velha[2]=="O"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[3]=="O" and tabuleiro_velha[4]=="O" and tabuleiro_velha[5]=="O"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[6]=="O" and tabuleiro_velha[7]=="O" and tabuleiro_velha[8] == "O"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[0]=="O" and tabuleiro_velha[3] == "O" and tabuleiro_velha[6] == "O"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[1]=="O" and tabuleiro_velha[4]=="O" and tabuleiro_velha[7]=="O"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[2]=="O" and tabuleiro_velha[5] == "O" and tabuleiro_velha[8]== "O"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[0]=="O" and tabuleiro_velha[4]=="O" and tabuleiro_velha[8]=="O"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(tabuleiro_velha[6]=="O" and tabuleiro_velha[4]=="O" and tabuleiro_velha[2]=="O"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    else:
        if(fim_de_jogo == False):
            fim_de_jogo = False            
    imprimir_tabela()
#verificar fim de jogo
    if(cond_verdade == True):
        numero_de_jogadas_player = 5
        cond = True
        fim_de_jogo = True
        end = True
#Vez do jogador
    if(cond == False):
        print("Qual posicao quer joga?")
        jogada = int(input())
        i = jogada-1
        if(jogada > 9 or jogada < 1):
            print("Jogada invalida!Escolha  um numero entre 1 e 9!")
            cond = False
            cond2 = True
        elif(jogada <= 10 and jogada >= 1):
            if(tabuleiro_velha[i]=="_" or tabuleiro_velha[i]==" "):
                tabuleiro_velha[i]="X"
                cond1 = False
                cond2 = False
            else:                                               #Caso uma posicao ja tiver sido escolhida
                print("Posicao ja preenchida!Escolha outra!")
                cond1 = True
                print("Qual posicao quer joga?")
                jogada = int(input())
                i = jogada-1
                if(tabuleiro_velha[i]=="_" or tabuleiro_velha[i]==" "):
                    tabuleiro_velha[i]="X"
                    cond1 = False
                    cond2 = False
                
    numero_de_jogadas_player+=1    
    end = False
#vez do computador
    i = randint(0,8)
    if(numero_de_jogadas_player < 5):                           
        if(end != True):
            if(cond2 != True):
                while cond == False:
                    if(cond1 != True):
                        if(tabuleiro_velha[i]=="_" or tabuleiro_velha[i]==" "):
                            tabuleiro_velha[i]="O"
                            cond=True
                        else:
                            i = randint(0,8)
    cond = False
    if(numero_de_jogadas_player == 5):
        cond = True        
if(fim_de_jogo == False):    
    print("\n O Jogo velhou!Vamos jogar novamente!")

