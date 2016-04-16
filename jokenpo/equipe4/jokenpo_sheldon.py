#Kid Mendes de Oliveira Neto 1615310011
#Igor Menezes Sales Vieira 1615310007 
#Eduardo Maia Freire 1615310003
#
import random

pedra = 1
papel = 2
tesoura = 3
lagarto = 4
spock = 5
numero = random.randint(1,5)

print("Digite seu nome:")
nome = raw_input()

print("Vem pro Duelo! %s.Humano"%nome)
print("Vamos jogar um JokenPo!")

jogada = 0
continuar = 0

while continuar != -1:
    jogada =  int(input("Para realizar a jogada voce ira usar: (1)-pedra;(2)-papel;(3)-tesoura;(4)-Lagarto;(5)Spock:\n"))

    if(jogada != -1):
        print("%s escolheu isso: %s"%(nome,jogada))
        print("A minha escolha foi: %s"%numero)
        if(jogada == 1):
            if(numero == 2 or numero == 5):
                print("Voce perdeu!Mizeravi")
            if(numero == 1):
                print("Empatamos!Vamos outra!")
            if(numero == 3 or numero == 4):
                print("Ganhou Mizeravi!")
        if(jogada == 2):
            if(numero == 3 or numero == 4):
                print("Voce perdeu!Mizeravi!")
            if(numero == 2):
                print("Empatamos!Vamos outra!")
            if(numero == 1 or numero == 5):
                print("Ganhou Mizeravi!")
        if(jogada == 3):
            if(numero == 1 or numero == 5):
                print("Voce perdeu!Mizeravi")
                
            if(numero == 3):
                print("Empatamos!Vamos outra!")
            if(numero == 2 or numero == 4):
                print("Ganhou Mizeravi!")
        if(jogada == 4):
            if(numero == 1 or numero == 3):
                print("Voce perdeu!Mizeravi")
            if(numero == 4):
                print("Empatamos!Vamos outra!")
            if(numero == 2 or numero == 5):
                print("Ganhou Mizeravi!")
        if(jogada == 5):
            if(numero == 2 or numero == 4):
                print("Voce perdeu!Mizeravi")
            if(numero == 5):
                print("Empatamos!Vamos outra!")
            if(numero == 3 or numero == 1):
                print("Ganhou Mizeravi!")

    continuar = int(input("Quer continuar?(1)-Sim;(-1)-Nao:"))
    numero = random.randint(1,5)
    if(continuar == -1):
        jogada == -1
