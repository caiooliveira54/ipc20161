# Ana Beatriz Faria Frota - 1615310027
# Ariel Guilherme - 1615310029
# Kylciane Cristiny Lopes Freitas - 1615310052
# Mateus Mota de Souza - 1615310016
# Nahan Trindade Passos - 1615310021 

import random

tab = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
cont = 0

while cont < 9:
    if cont % 2 == 0:
        print ("\n %s | %s | %s  \n---+---+--- \n %s | %s | %s  \n---+---+--- \n %s | %s | %s "%(tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7], tab[8]))
        num = int(input("\nSua jogada: "))
        if tab[num] == " ":
            tab[num] = "X"
            cont += 1
        if (tab[0] == tab[1] == tab[2] == "X") or (tab[3] == tab[4] == tab[5] == "X") or (tab[6] == tab[7] == tab[8] == "X") or (tab[0] == tab[3] == tab[6] == "X") or (tab[1] == tab[4] == tab[7] == "X") or (tab[2] == tab[5] == tab[8] == "X") or (tab[0] == tab[4] == tab[8] == "X") or (tab[2] == tab[4] == tab[6] == "X"):
            print ("\nGanhou!")
            cont = 10
        else:
            cont = cont       
    else:
        comp = random.randint(0,8)
        if tab[comp] == " ":
            tab[comp] = "O"
            cont += 1
        if (tab[0] == tab[1] == tab[2] == "O") or (tab[3] == tab[4] == tab[5] == "O") or (tab[6] == tab[7] == tab[8] == "O") or (tab[0] == tab[3] == tab[6] == "O") or (tab[1] == tab[4] == tab[7] == "O") or (tab[2] == tab[5] == tab[8] == "O") or (tab[0] == tab[4] == tab[8] == "O") or (tab[2] == tab[4] == tab[6] == "O"):
            print ("\nPerdeu!")
            cont = 10
        else:
            cont = cont

if cont == 9:
    print ("\nEmpatou!")
print ("\n %s | %s | %s  \n---+---+--- \n %s | %s | %s  \n---+---+--- \n %s | %s | %s "%(tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7], tab[8]))

         

