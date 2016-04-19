#Introdução a programação de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

import random
lista = ["1","2","3","4","5","6","7","8","9"]
cond = 1

while cond <= 9:
    print("  %s | %s | %s "%(lista[0],lista[1],lista[2])) 
    print("----+---+----")
    print("  %s | %s | %s "%(lista[3],lista[4],lista[5])) 
    print("----+---+----")
    print("  %s | %s | %s \n"%(lista[6],lista[7],lista[8]))
    if cond%2 != 0:
        jogada = int(input("Informe a posição em que deseja jogar: "))
        if lista[jogada - 1] == str(jogada):
            lista[jogada - 1] = "X"
            cond += 1
            if lista[0]==lista[1] and lista[1]==lista[2]:
                print("\nParabens! Voce ganhou a partida")
                cond = 11                
            if lista[3]==lista[4] and lista[4]==lista[5]:
                print("\nParabens! Voce ganhou a partida")
                cond = 11                
            if lista[6]==lista[7] and lista[7]==lista[8]:
                print("\nParabens! Voce ganhou a partida")
                cond = 11                
            if lista[0]==lista[3] and lista[3]==lista[6]:
                print("\nParabens! Voce ganhou a partida")
                cond = 11                
            if lista[1]==lista[4] and lista[4]==lista[7]:
                print("\nParabens! Voce ganhou a partida")
                cond = 11                
            if lista[2]==lista[5] and lista[5]==lista[8]:
                print("\nParabens! Voce ganhou a partida")
                cond = 11                
            if lista[0]==lista[4] and lista[4]==lista[8]:
                print("\nParabens! Voce ganhou a partida")
                cond = 11                
            if lista[2]==lista[4] and lista[4]==lista[6]:
                print("\nParabens! Voce ganhou a partida")
                cond = 11
    else:
        computador = random.randint(0,8)
        if lista[computador] == str(computador + 1):
            lista[computador] = "O"
            cond += 1
            if lista[0]==lista[1] and lista[1]==lista[2]:
                print("\nQue pena, o computador ganhou a partida!")
                cond = 11                
            if lista[3]==lista[4] and lista[4]==lista[5]:
                print("\nQue pena, o computador ganhou a partida!")
                cond = 11                
            if lista[6]==lista[7] and lista[7]==lista[8]:
                print("\nQue pena, o computador ganhou a partida!")
                cond = 11                
            if lista[0]==lista[3] and lista[3]==lista[6]:
                print("\nQue pena, o computador ganhou a partida!")
                cond = 11                
            if lista[1]==lista[4] and lista[4]==lista[7]:
                print("\nQue pena, o computador ganhou a partida!")
                cond = 11                
            if lista[2]==lista[5] and lista[5]==lista[8]:
                print("\nQue pena, o computador ganhou a partida!")
                cond = 11                
            if lista[0]==lista[4] and lista[4]==lista[8]:
                print("\nQue pena, o computador ganhou a partida!")
                cond = 11                
            if lista[2]==lista[4] and lista[4]==lista[6]:
                print("\nQue pena, o computador ganhou a partida!")
                cond = 11        
    if cond == 10:
        print("\nIh, o jogo velhou!")
print("  %s | %s | %s "%(lista[0],lista[1],lista[2])) 
print("----+---+----")
print("  %s | %s | %s "%(lista[3],lista[4],lista[5])) 
print("----+---+----")
print("  %s | %s | %s \n"%(lista[6],lista[7],lista[8]))