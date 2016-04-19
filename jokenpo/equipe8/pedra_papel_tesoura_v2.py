# Mateus Mota de Souza - 1615310016
# Nahan Trindade Passos
import random
print ("Pedra, Papel, Tesoura, Spock e Lagarto - v1 \n")

nome = str(input("Qual seu nome? \n"))
print ("\nOlá " + nome + ", vamos jogar Pedra, Papel, Tesoura, Spock e Lagarto?")
quantidade = int(input("Quantas vezes você quer me desafiar? \n"))
vitoria = 0
print ("\nOpções para escolha: \n1- Pedra \n2- Papel \n3- Tesoura \n4- Spock \n5- Lagarto \n")

for i in range(quantidade):
    cpu = random.randint(1,5)
    escolha = int(input("Qual a sua escolha?\n"))
    if escolha == 1:
        if cpu == 1:
            print ("\nAparentemente empatamos " + nome + ", você escolheu pedra e eu também\n")
        if cpu == 2:
            print ("\nQue pena " + nome + ", você perdeu, papel cobre pedra\n")
        if cpu == 3:
            print ("\nParabéns " + nome + ", você venceu, pedra quebra tesoura\n")
            vitoria += 1
        if cpu == 4:
            print ("\Que pena " + nome + ", Spock evaporiza pedra\n")
        if cpu == 5:
            print ("\nCaraca " + nome + ", você decapitou meu lagarto com sua pedra\n")
            vitoria += 1
    if escolha == 2:
        if cpu == 1:
            print ("\nParabéns" + nome + ", papel cobre pedra\n")
            vitoria += 1
        if cpu == 2:
            print ("\nAparentemente empatamos "+ nome + ", você escolheu papel e eu também\n")
        if cpu == 3:
            print ("\nQue pena " + nome + ", tesoura corta papel\n")
        if cpu == 4:
            print ("\nCaraca " + nome + ", você refrutou Spock com seu papel\n")
            vitoria += 1
        if cpu == 5:
            print ("\nQue pena " + nome + ", lagarto acidentalmente comeu seu papel\n")
    if escolha == 3:
        if cpu == 1:
            print ("\nQue pena " + nome + ", pedra destrói tesoura\n")
        if cpu == 2:
            print ("\nParabéns " + nome + ", tesoura corta papel\n")
            vitoria += 1
        if cpu == 3:
            print ("\nAparentemente empatamos "+ nome + ", você escolheu tesoura e eu também\n")
        if cpu == 4:
            print ("\nQue pena " + nome + ", Spock destruiu a sua tesoura\n")
        if cpu == 5:
            print ("\nCaraca " + nome + ", você decapitou meu lagarto com sua tesoura\n")
            vitoria += 1
    if escolha == 4:
        if cpu == 1:
            print ("\nCaramba " + nome + ", Spock vaporizou minha pedra\n")
            vitoria += 1
        if cpu == 2:
            print ("\nCaramba " + nome + ", seu papel refrutou Spock\n")
            vitoria += 1
        if cpu == 3:
            print ("\nQue pena " + nome + ", Spock quebrou sua tesoura\n")
        if cpu == 4:
            print ("\nAparentemente empatamos "+ nome + ", você escolheu Spock e eu também\n")
        if cpu == 5:
            print ("\Que pena " + nome + ", Spock foi envenenado pelo lagarto\n")

    if escolha == 5:
        if cpu == 1:
            print ("\nQue pena " + nome + ", minha pedra quebrou sua\n")
        if cpu == 2:
            print ("\nCaramba " + nome + ", seu lagarto comeu meu papel\n")
            vitoria += 1
        if cpu == 3:
            print ("\nQue pena " + nome + ", eu decaptei seu lagarto com a tesoura\n")
        if cpu == 4:
            print ("\nCaracoles " + nome + ", seu lagarto envenenou Spock\n")
            vitoria += 1
        if cpu == 5:
            print ("\nAparentemente empatamos "+ nome + ", você escolheu lagarto e eu também\n")

print ("\nObrigado por jogar, quem sabe não tentamos uma partida futuramente, você ganhou", vitoria, "vez(es), parabéns")
            
            
