import random

numero = (random.randint(1,3))
escolha = 0

nome = input("digite seu nome:\n")

while escolha == 0: 
    print("1- pedra\n2 - papel\n3 - tesoura\n")
    tentativa = int(input("digite o numero correspondente:\n"))
    if tentativa == 1:
        if numero == 2:
            print("Voce ecolheu pedra, a maquina escolheu papel")
            print("Voce perdeu")
        if numero == 3:
            print("Voce ecolheu pedra, a maquina escolheu tesoura")
            print("Voce ganhou")
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
        if numero == tentativa:
            print("Voce ecolheu papel, a maquina escolheu papel")
            print("empate")
    if tentativa == 3:
        if numero == 2:
            print("Voce ecolheu tesoura, a maquina escolheu papel")
            print("Voce perdeu")
        if numero == 1:
            print("Voce ecolheu tesoura, a maquina escolheu pedra")
            print("Voce ganhou")
        if numero == tentativa:
            print("Voce ecolheu tesoura, a maquina escolheu tesoura")
            print("empate")
    resposta = input("Voce quer continuar jogando(sim ou nao)?\n")
    if resposta == "sim":
            escolha = 0 
    if resposta == "nao":
            escolha = 1

print ("Cansou de joguinho pro hoje? \nvolte sempre!")
            
