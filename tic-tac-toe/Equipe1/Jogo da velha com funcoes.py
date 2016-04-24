#
#Introdução a Programação de Computadores
#Professor: Jucimar Jr.
#EQUIPE 1
#
#Any Mendes Carvalho - 1615310044
#Kid Mendes de Oliveira Neto - 1615310011
#Victor Rafael da Silva e Silva - 1615310025
#Eduardo Maia Freire - 1615310003
#Luiz Gustavo de Rocha Melo - 1615310015
#Matheus Palheta Barbosa -1615310019
#Mateus Mota de Souza - 1615310016
#Ariel Guilherme - 1615310029
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Nickso Patrick Façanha Calheiros - 1615310059
#Igor Menezes Sales Vieira - 1615310007
#Lucas Ferreira Soares - 1615310014
#


from random import *

vet1=[" "," "," ","_","_","_","_","_","_"]
vet=[1,2,3,4,5,6,7,8,9]
i = 0            
jogadas = 0
cond = False
cond1 = False
cond2 = False 
bloquear=False
fim_de_jogo = False

def verificar_vitoria():
    if((vet1[0]=="X" and vet1[1]=="X" and vet1[2]=="X") or (vet1[3]=="X" and vet1[4]=="X" and vet1[5]=="X") or (vet1[6]=="X" and vet1[7]=="X" and vet1[8] =="X") or (vet1[0]=="X" and vet1[3] =="X" and vet1[6] =="X") or (vet1[1]=="X" and vet1[4]=="X" and vet1[7]=="X") or(vet1[2]=="X" and vet1[5] =="X" and vet1[8]=="X") or (vet1[0]=="X" and vet1[4]=="X" and vet1[8]=="X") or (vet1[6]=="X" and vet1[4]=="X" and vet1[2]=="X")):
        print("Voce venceu!Parabens!")
        return True    
    else:
        return False  
def verificar_derrota():
    if((vet1[0]=="O" and vet1[1]=="O" and vet1[2]=="O") or (vet1[3]=="O" and vet1[4]=="O" and vet1[5]=="O") or (vet1[6]=="O" and vet1[7]=="O" and vet1[8]=="O") or (vet1[0]=="O" and vet1[3]=="O" and vet1[6]=="O") or (vet1[1]=="O" and vet1[4]=="O" and vet1[7]=="O") or (vet1[2]=="O" and vet1[5]=="O" and vet1[8]=="O") or (vet1[0]=="O" and vet1[4]=="O" and vet1[8]=="O") or (vet1[6]=="O" and vet1[4]=="O" and vet1[2]=="O")):
        print("Voce perdeu!Tente novamente.")
        return True    
    else:
        return False  
    
def imprimir_tabela():
    print("\n|-----Posicoes------|----Jogo da Velha----|")
    print("|    _%s_|_%s_|_%s_    |     _%s_|_%s_|_%s_     |" %(vet[6],vet[7],vet[8],vet1[6],vet1[7],vet1[8]))
    print("|    _%s_|_%s_|_%s_    |     _%s_|_%s_|_%s_     |" %(vet[3],vet[4],vet[5],vet1[3],vet1[4],vet1[5]))
    print("|     %s | %s | %s     |      %s | %s | %s      |" %(vet[0],vet[1],vet[2],vet1[0],vet1[1],vet1[2]))
    print("|-------------------|---------------------|\n")  

def verifica_posicao_valida(jogada):
    if(jogada <= 9 and jogada >= 1):
        return True
    else:
        print("Posicao invalida")
        return False

def verificar_posicao_ocupada(jogada):
    i = jogada-1
    if(vet1[i] == "O" or vet1[i] == "X"):
        print("Posicao ocupada")        
        return False
    else:
        return True
    
def vez_jogador():
    cond1 = False
    cond2 = False
    cond = False
    while(cond ==  False):
        print("Qual posicao quer joga?")
        jogada = int(input())        
        cond1 = verifica_posicao_valida(jogada)
        if(cond1 == True):
            cond2 = verificar_posicao_ocupada(jogada)
            if(cond2 == False):
                cond = False
            else:
                i = jogada-1
                vet1[i] = "X"
                cond = True
        if(cond1 == False):
            cond = False
            
def jogar_linha(symbol):
    for i in range(0,9,3):
        if((vet1[i]==symbol and vet1[i+1]==symbol)):
            if(vet1[i+2]=="_" or vet1[i+2]==" "):
                vet1[i+2]="O"
                return True
        elif((vet1[i]==symbol and vet1[i+2]==symbol)):
            if(vet1[i+1]=="_" or vet1[i+1]==" "):
                vet1[i+1]="O"
                return True
        elif((vet1[i+1]==symbol and vet1[i+2]==symbol)):
            if(vet1[i]=="_" or vet1[i]==" "):
                vet1[i]="O"  
                return True
    return False

def jogar_coluna(symbol):
    for i in range(0,3):
        if((vet1[i]==symbol and vet1[i+3]==symbol)):
            if(vet1[i+6]=="_" or vet1[i+6]==" "):
                vet1[i+6]="O"
                return True
        elif((vet1[i]==symbol and vet1[i+6]==symbol)):
            if(vet1[i+3]=="_" or vet1[i+3]==" "):
                vet1[i+3]="O"
                return True
        elif((vet1[i+3]==symbol and vet1[i+6]==symbol)):
            if(vet1[i]=="_" or vet1[i]==" "):
                vet1[i]="O"  
                return True
    return False

def jogar_diagonal(symbol):
    if(vet1[0]==symbol and vet1[4]==symbol and vet1[8]=="_"):
        vet1[8]="O"
        return True
    elif(vet1[0]==symbol and vet1[4]=="_" and vet1[8]==symbol):
        vet1[4]="O"
        return True
    elif(vet1[0]==" " and vet1[4]==symbol and vet1[8]==symbol):
        vet1[0]="O"
        return True       
    elif(vet1[6]==symbol and vet1[4]==symbol and vet1[2]==" "):
        vet1[2]="O"
        return True
    elif(vet1[6]==symbol and vet1[4]=="_" and vet1[2]==symbol):
        vet1[4]="O"
        return True
    elif(vet1[6]=="_" and vet1[4]==symbol and vet1[2]==symbol):
        vet1[6]="O"
        return True     
    return False

def vez_computador():
    print("Vez computador")
    bloquear = False
    cond = False
    if(cond == False):
        #Ganhar
        if(bloquear==False):
            #Horizontal
            bloquear = jogar_linha("O")
            cond = True
        if(bloquear==False):    
            #Vertical
            bloquear = jogar_coluna("O")
            cond = True            
        if(bloquear==False):     
            #Diagonal    
            bloquear = jogar_diagonal("O")
            cond = True
        #bloquear
        if(bloquear==False):
            #Horizontal
            bloquear = jogar_linha("X")
            cond = True
        if(bloquear==False):    
            #Vertical
            bloquear = jogar_coluna("X")
            cond = True
        if(bloquear==False):     
            #Diagonal    
            bloquear = jogar_diagonal("X")
            cond = True
      
        if(bloquear==False):    
            #Triangulo
            if(vet1[4] == "_"):
                vet1[4] = "O"
                cond=True 
            elif(vet1[4] =="X"):
                if(vet1[0]==" " or vet1[2]==" " or vet1[6]=="_" or vet1[8]=="_"):
                    i=choice([0,2,6,8])
                    vet1[i]="O"
                    cond=True

            elif(vet1[6] == "X" and vet1[4] == "O" and vet1[2] == "X") or (vet1[8] == "X" and vet1[4] == "O" and vet1[0] == "X"):
                if(vet1[1]==" " or vet1[3]==" " or vet1[5]=="_" or vet1[7]=="_"):
                    i=choice([1,3,5,7])
                    vet1[i]="O"
                    cond=True

            else:
                if(vet1[0]==" "):
                    vet1[0]="O"
                    cond=True
                elif(vet1[2]==" "):
                    vet1[2]="O"
                    cond=True
                elif(vet1[6]=="_"):
                    vet1[6]="O"
                    cond=True
                elif(vet1[8]=="_"):
                    vet1[8]="O"
                    cond=True                       
                elif(vet1[1]==" "):
                    vet1[1]="O"
                    cond=True
                elif(vet1[3]=="_"):
                    vet1[3]="O"
                    cond=True
                elif(vet1[5]=="_"):
                    vet1[5]="O"
                    cond=True
                elif(vet1[7]=="_"):
                    vet1[7]="O"
                    cond=True                
             
def verificar_velha():
    global jogadas
    jogadas = jogadas + 1
    if(jogadas >= 9):
        print("O jogo velhou!Vamos jogar novamente.")
        return True
    else:
        return False

#fluxo principal
imprimir_tabela()
while fim_de_jogo == False:
    vez_jogador()
    fim_de_jogo = verificar_vitoria()
    if(fim_de_jogo == False):
        fim_de_jogo = verificar_velha()
        imprimir_tabela()
        if(fim_de_jogo == False):
            vez_computador()
            fim_de_jogo = verificar_derrota()
            if(fim_de_jogo == False):
                fim_de_jogo = verificar_velha()
            imprimir_tabela()
