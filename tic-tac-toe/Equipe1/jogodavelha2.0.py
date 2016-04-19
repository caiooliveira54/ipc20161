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

vet1=["_","_","_","_","_","_"," "," "," "]
vet=[1,2,3,4,5,6,7,8,9]
i = 0            
cont = 0
cond_aux = False
cond = False
cond1 = False
cond_verdade = False
cond2 = False
end = False 

while cont <= 5 :

    if(vet1[0]=="X" and vet1[1]=="X" and vet1[2]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(vet1[3]=="X" and vet1[4]=="X" and vet1[5]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(vet1[6]=="X" and vet1[7]=="X" and vet1[8] == "X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(vet1[0]=="X" and vet1[3] == "X" and vet1[6] == "X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(vet1[1]=="X" and vet1[4]=="X" and vet1[7]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(vet1[2]=="X" and vet1[5] == "X" and vet1[8]== "X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(vet1[0]=="X" and vet1[4]=="X" and vet1[8]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    elif(vet1[6]=="X" and vet1[4]=="X" and vet1[2]=="X"):
        print("Voce venceu!Parabens!")
        cond_verdade = True
    else:
        if(cond_aux == False):
            cond_aux = False        
    if(vet1[0]=="O" and vet1[1]=="O" and vet1[2]=="O"):
        print("Voce perdeu!Tente novamente.")
        cond_verdade = True
    elif(vet1[3]=="O" and vet1[4]=="O" and vet1[5]=="O"):
        print("Voce perdeu!Tente novamente.")
        cond_verdade = True
    elif(vet1[6]=="O" and vet1[7]=="O" and vet1[8]=="O"):
        print("Voce perdeu!Tente novamente.")
        cond_verdade = True
    elif(vet1[0]=="O" and vet1[3]=="O" and vet1[6]=="O"):
        print("Voce perdeu!Tente novamente.")
        cond_verdade = True
    elif(vet1[1]=="O" and vet1[4]=="O" and vet1[7]=="O"):
        print("Voce perdeu!Tente novamente.")
        cond_verdade = True
    elif(vet1[2]=="O" and vet1[5]=="O" and vet1[8]=="O"):
        print("Voce perdeu!Tente novamente.")
        cond_verdade = True
    elif(vet1[0]=="O" and vet1[4]=="O" and vet1[8]=="O"):
        print("Voce perdeu!Tente novamente.")
        cond_verdade = True
    elif(vet1[6]=="O" and vet1[4]=="O" and vet1[2]=="O"):
        print("Voce perdeu!Tente novamente.")
        cond_verdade = True
    else:
        if(cond_aux == False):
            cond_aux = False  

    print("\n|-----Posicoes------|----Jogo da Velha----|")
    print("|    _%s_|_%s_|_%s_    |     _%s_|_%s_|_%s_     |" %(vet[6],vet[7],vet[8],vet1[6],vet1[7],vet1[8]))
    print("|    _%s_|_%s_|_%s_    |     _%s_|_%s_|_%s_     |" %(vet[3],vet[4],vet[5],vet1[3],vet1[4],vet1[5]))
    print("|     %s | %s | %s     |      %s | %s | %s      |" %(vet[0],vet[1],vet[2],vet1[0],vet1[1],vet1[2]))
    print("|-------------------|---------------------|\n")        

    if(cond_verdade == True):
        cont = 5
        cond = True
        cond_aux = True
        end = True
    if(cond == False):
        print("Qual posicao quer joga?")
        jogada = int(input())
        i = jogada-1
        if(jogada > 9 or jogada < 1):
            print("Jogada invalida!Escolha  um numero entre 1 e 9!")
            cond = False
            cond2 = True
        elif(jogada <= 10 and jogada >= 1):
            if(vet1[i]=="_" or vet1[i]==" "):
                vet1[i]="X"
                cond1 = False
                cond2 = False
            else:                                               #Caso uma posicao ja tiver sido escolhida
                print("Posicao ja preenchida!Escolha outra!")
                cond1 = True
                print("Qual posicao quer joga?")
                jogada = int(input())
                i = jogada-1
                if(vet1[i]=="_" or vet1[i]==" "):
                    vet1[i]="X"
                    cond1 = False
                    cond2 = False
    cont+=1
    end = False
    i = randint(0,8)
    if(cont < 5):                           
        if(end != True):
            if(cond2 != True):
                while cond == False:
                    if(cond1 != True):
                        if(vet1[i]=="_" or vet1[i]==" "):
                            vet1[i]="O"
                            cond=True
                        else:
                            i = randint(0,8)
    cond = False
    if(cont == 5):
        cond = True
if(cond_aux == False):    
    print("\n O Jogo velhou!Vamos jogar novamente!")

