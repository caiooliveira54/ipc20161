#Introdução a programação de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Ana Beatriz Frota - 1615310027

import random
opcoes = ["pedra","papel","tesoura"]
cond = 0
nome = raw_input("Qual o seu nome?\n")
while cond != -1:
    print("Ola humano "+ nome + ", o destino da humanidade sera decidido neste jogo de jokenpo\nComecemos!")
    print("Digite o numero de uma das opcoes a seguir:")
    print("1 - pedra\n2 - papel\n3 - tesoura")
    jogada = int(input("Faça sua escolha: "))
    num = random.randint(1,3)
    if jogada == 1 and num == 3:
        print("Voce ganhou pois coloquei %s e voce %s.\nParece que a humanidade vivera mais um dia..."%(opcoes[2],opcoes[0]))
    if jogada == 2 and num == 1:
        print("Voce ganhou pois coloquei %s e voce %s.\nParece que a humanidade vivera mais um dia..."%(opcoes[0],opcoes[1]))
    if jogada == 3 and num == 2:
        print("Voce ganhou pois coloquei %s e voce %s.\nParece que a humanidade vivera mais um dia..."%(opcoes[1],opcoes[2]))
    if jogada == 1 and num == 1:
        print("Empatamos pois coloquei %s e voce tambem.\nHumano, tens muita sorte..."%opcoes[0])
    if jogada == 2 and num == 2:
        print("Empatamos pois coloquei %s e voce tambem.\nHumano, tens muita sorte..."%opcoes[1])
    if jogada == 3 and num == 3:
        print("Empatamos pois coloquei %s e voce tambem.\nHumano, tens muita sorte..."%opcoes[2])
    if jogada == 1 and num == 2:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nDiga adeus ao mundo que conhece humano!"%(opcoes[1],opcoes[0]))
    if jogada == 2 and num == 3:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nDiga adeus ao mundo que conhece humano!"%(opcoes[2],opcoes[1]))
    if jogada == 3 and num == 1:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nDiga adeus ao mundo que conhece humano!"%(opcoes[0],opcoes[2]))
    cond = int(input("Se deseja parar o programa, digite -1: "))
    print("    ")
