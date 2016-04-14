#Nickso Patrick Façanha Calheiros - 1615310059
#Ariel Guilherme Rocha Capistrano - 1615310029

import random

numero = (random.randint(1,5))
escolha = 0

nome = input("digite seu nome:\n")

while escolha == 0: 

    print("1 - pedra\n2 - papel\n3 - tesoura\n4 - largato\n5 - spock\n")

    tentativa = int(input("digite o numero correspondente:\n"))

    if tentativa == 1:

        if numero == 2:
            print("Voce ecolheu pedra, a maquina escolheu papel")
            print("Voce perdeu")

        if numero == 3:
            print("Voce ecolheu pedra, a maquina escolheu tesoura")
            print("Voce ganhou")

        if numero == 4:
            print("Voce ecolheu pedra, a maquina escolheu largato")
            print("Voce ganha")

        if numero == 5:
            print("Voce ecolheu pedra, a maquina escolheu spock")
            print("Voce perdeu")

        if numero == tentativa:
            print("Voce ecolheu pedra, a maquina escolheu pedra")
            print("empate")

    if tentativa == 2:

        if numero == 3:
            print("Voce ecolheu papel, a maquina escolheu tesoura")
            print("Voce perdeu")

        if numero == 1:
            print("Voce ecolheu papel, a maquina escolheu pedra")
            print("Voce ganhou")

        if numero == 4:
            print("Voce ecolheu papel, a maquina escolheu largato")
            print("Voce perdeu")

        if numero == 5:
            print("Voce ecolheu papel, a maquina escolheu spock")
            print("Voce ganhou")

        if numero == tentativa:
            print("Voce ecolheu papel, a maquina escolheu papel")
            print("empate")

    if tentativa == 3:

        if numero == 2:
            print("Voce ecolheu tesoura, a maquina escolheu papel")
            print("Voce ganhou")

        if numero == 1:
            print("Voce ecolheu tesoura, a maquina escolheu pedra")
            print("Voce perdeu")

        if numero == 4:
            print("Voce ecolheu tesoura, a maquina escolheu largato")
            print("Voce ganhou")

        if numero == 5:
            print("Voce ecolheu tesoura, a maquina escolheu spock")
            print("Voce perdeu")

        if numero == tentativa:
            print("Voce ecolheu tesoura, a maquina escolheu tesoura")
            print("empate")

    if tentativa == 4:

        if numero == 2:
            print("Voce ecolheu largato, a maquina escolheu papel")
            print("Voce ganhou")

        if numero == 1:
            print("Voce ecolheu largato, a maquina escolheu pedra")
            print("Voce perdeu")

        if numero == 3:
            print("Voce ecolheu largato, a maquina escolheu tesoura")
            print("Voce perdeu")

        if numero == 5:
            print("Voce ecolheu largato, a maquina escolheu spock")
            print("Voce ganhou")

        if numero == tentativa:
            print("Voce ecolheu largato, a maquina escolheu largato")
            print("empate")

    if tentativa == 5:

        if numero == 2:
            print("Voce ecolheu spock, a maquina escolheu papel")
            print("Voce perdeu")

        if numero == 1:
            print("Voce ecolheu spock, a maquina escolheu pedra")
            print("Voce ganhou")

        if numero == 3:
            print("Voce ecolheu spock, a maquina escolheu tesoura")
            print("Voce ganhou")

        if numero == 4:
            print("Voce ecolheu spock, a maquina escolheu largato")
            print("Voce perdeu")

        if numero == tentativa:
            print("Voce ecolheu spock, a maquina escolheu spock")
            print("empate")


    resposta = input("Voce quer continuar jogando(sim ou nao)?\n")

    if resposta == "sim":
            escolha = 0 

    if resposta == "nao":
            escolha = 1

print ("Cansou de joguinho pro hoje? \nvolte sempre!")
            
