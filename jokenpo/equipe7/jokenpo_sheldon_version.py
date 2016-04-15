#Introdução a programação de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Ana Beatriz Frota - 1615310027

import random
opcoes = ["pedra","papel","tesoura","lagarto","Spock"]
num = random.randint(1,5)
cond = 0
nome = raw_input("Qual o seu nome?\n")
while cond != -1:
    print("Ola "+ nome + ", que tal uma partida de pedra, papel, tesoura, lagarto, spock?")
    print("Digite o numero de uma das opcoes a seguir:")
    print("1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Lagarto\n5 - Spock")
    jogada = int(input("Faça sua escolha: "))
    if jogada == 1 and num == 3:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[2],opcoes[0]))
    if jogada == 1 and num == 4:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[3],opcoes[0]))
    if jogada == 2 and num == 1:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[0],opcoes[1]))
    if jogada == 2 and num == 5:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[4],opcoes[1]))
    if jogada == 3 and num == 2:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[1],opcoes[2]))
    if jogada == 3 and num == 4:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[1],opcoes[2]))    
    if jogada == 4 and num == 2:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[1],opcoes[3]))
    if jogada == 4 and num == 5:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[4],opcoes[3]))
    if jogada == 5 and num == 3:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[2],opcoes[4]))
    if jogada == 5 and num == 1:
        print("Voce ganhou pois coloquei %s e voce %s.\nParabens!"%(opcoes[0],opcoes[4]))    
    if jogada == 1 and num == 1:
        print("Empatamos pois coloquei %s e voce tambem."%opcoes[0])
    if jogada == 2 and num == 2:
        print("Empatamos pois coloquei %s e voce tambem."%opcoes[1])
    if jogada == 3 and num == 3:
        print("Empatamos pois coloquei %s e voce tambem."%opcoes[2])
    if jogada == 4 and num == 4:
        print("Empatamos pois coloquei %s e voce tambem."%opcoes[3])
    if jogada == 5 and num == 5:
        print("Empatamos pois coloquei %s e voce tambem."%opcoes[4])    
    if jogada == 1 and num == 2:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[1],opcoes[0]))
    if jogada == 1 and num == 5:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[4],opcoes[0]))    
    if jogada == 2 and num == 3:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[2],opcoes[1]))
    if jogada == 2 and num == 4:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[3],opcoes[1]))    
    if jogada == 3 and num == 1:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[0],opcoes[2]))
    if jogada == 3 and num == 5:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[4],opcoes[2]))
    if jogada == 4 and num == 3:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[2],opcoes[3]))
    if jogada == 4 and num == 1:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[0],opcoes[3]))
    if jogada == 5 and num == 2:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[1],opcoes[4]))
    if jogada == 5 and num == 4:
        print("Parece que você perdeu, pois coloquei %s e voce %s!\nMais sorte da proxima vez!"%(opcoes[3],opcoes[4]))
    cond = int(input("Se deseja parar o programa, digite -1: "))
