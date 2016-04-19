# Ana Beatriz Faria Frota
# Ariel Guilherme
# Kylciane Cristiny Lopes Freitas
# Mateus Mota de Souza
# Nahan Trindade Passos

import random
tab = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
cont = 0

while (cont < 9):
    if cont % 2 == 0:
        tabela = ("\n %s | %s | %s \n---+---+--- \n %s | %s | %s  \n---+---+---\n %s | %s | %s "%(tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7], tab[8]))
        print (tabela)        
        pos = int (input("\nQual posiçao? "))
        if tab[pos] == str(pos):
            tab[pos] = "X"
            cont += 1
        if (tab[0] == tab[1] == tab[2] == "X") or (tab[3] == tab[4] == tab[5] == "X") or (tab[6] == tab[7] == tab[8] == "X") or (tab[0] == tab[3] == tab[6] == "X") or (tab[1] == tab[4] == tab[7] == "X") or (tab[2] == tab[5] == tab[8] == "X") or (tab[0] == tab[4] == tab[8] == "X") or (tab[2] == tab[4] == tab[6] == "X"):
            print ("\nGanho!")
            break
        else:
            cont = cont
    else:
        comp = random.randint(0,8)
        if tab[comp] == str(comp):
            tab[comp] = "O"
            cont += 1
        if (tab[0] == tab[1] == tab[2] == "O") or (tab[3] == tab[4] == tab[5] == "O") or (tab[6] == tab[7] == tab[8] == "O") or (tab[0] == tab[3] == tab[6] == "O") or (tab[1] == tab[4] == tab[7] == "O") or (tab[2] == tab[5] == tab[8] == "O") or (tab[0] == tab[4] == tab[8] == "O") or (tab[2] == tab[4] == tab[6] == "O"):
            print ("\nPerdeu!")
            break
        else:
            cont = cont
if cont == 9:
    print ("velhou")
