# Mateus Mota de Souza - 1615310016
# Nahan Trindade Passos
import random
print ("Jogo da velha v1.0 \n")

usuario = str(input("Digite seu nome: \n"))
print ("Olá " + usuario + " você está afim de uma partida desafiadora?")
quantidade = int(input("\nQuantas partidades você deseja jogar comigo? \n"))

print ("Agora vamos ver se consegue me vencer... \n1- Pedra \n2- Papel \n3- Tesoura")
vitoria = 0

for i in range(quantidade):
    cpu = random.randint(1,3)
    escolha = int(input("\nQual a sua jogada? \n"))
    if escolha == 1 and cpu == 1:
        print ("\nParece que empatamos desta vez "+ usuario +", ambos escolhemos pedra")
    if escolha == 1 and cpu == 2:
        print ("\nVocê perdeu " + usuario + ", você escolheu pedra e eu papel")
    if escolha == 1 and cpu == 3:
        print ("\nVocê saiu vitorioso desta vez, " + usuario + " por sorte escolhi tesoura e você pedra")
        vitoria += 1
    if escolha == 2 and cpu == 1:
        print ("\nVocê saiu vitorioso desta vez, " + usuario + " por sorte escolhi pedra e você papel")
        vitoria += 1
    if escolha == 2 and cpu == 2:
        print ("\nParece que empatamos desta vez "+ usuario + ", ambos escolhemos papel")
    if escolha == 2 and cpu == 3:
        print ("\nVocê perdeu " + usuario + ", você escolheu papel e eu tesoura")
    if escolha == 3 and cpu == 1:
        print ("\nVocê perdeu " + usuario + ", você escolheu tesoura e eu pedra")
    if escolha == 3 and cpu == 2:
        print ("\nVocê saiu vitorioso desta vez, " + usuario + " por sorte escolhi papel e você tesoura")
        vitoria += 1
    if escolha == 3 and cpu == 3:
        print ("\nParece que empatamos desta vez "+ usuario +", ambos escolhemos tesoura")
    
print ("\nQuem sabe não jogamos mais um pouco depois " + usuario +", você venceu", vitoria,"vez(es)")
