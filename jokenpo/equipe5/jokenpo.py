#Calebe Roberto Chaves da Silva Rebello - 1615310043
import random

tentativas_max = 1
qtd_tentativas = 0
qtd_tentativas1 = 2
numero = random.randint(1,3)

Pedra = 1
Papel = 2
Tesoura = 3

print("Insira seu nome: ")
nome = input()

print("\nOla",nome,"vamos jogar!\n")
print("\nVoce tem apenas uma tentativa\n")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

tentativa = int(input("Insira o numero: \n"))     

while qtd_tentativas < tentativas_max:

    if numero == 1 and tentativa == 3:
        print("Perdeu! :(, eu escolhi",numero)
    if numero == 2 and tentativa == 3:
        print("Ganhou! :), eu escolhi",numero)
    if numero == 3 and tentativa == 3:
        print("Empate! Jogue novamente!")
        tentativa = int(input("Insira o numero: \n"))
    if numero == 1 and tentativa == 2:
        print("Ganhou! :), eu escolhi",numero)
    if numero == 2 and tentativa == 2:
        print("Empate! Jogue novamente!")
        tentativa = int(input("Insira o numero: \n"))
    if numero == 3 and tentativa == 2:
        print("Perdeu! :(, eu escolhi",numero)
    if numero == 1 and tentativa == 1:
        print("Empate! Jogue novamente!")
        tentativa = int(input("Insira o numero: \n"))
    if numero == 2 and tentativa == 1:
        print("Perdeu! :(, eu escolhi",numero)
    if numero == 3 and tentativa == 1:
        print("Ganhou! :), eu escolhi",numero)
    qtd_tentativas += 1
    while qtd_tentativas < qtd_tentativas1:
        if tentativa != 1 and tentativa != 2 and tentativa != 3:
            print("Numero Invalido!")
            tentativa = int(input("Insira o numero: \n"))
            if numero == 1 and tentativa == 3:
                print("Perdeu! :(, eu escolhi",numero)
            if numero == 2 and tentativa == 3:
                print("Ganhou! :), eu escolhi",numero)
            if numero == 3 and tentativa == 3:
                print("Empate! Jogue novamente!")
                tentativa = int(input("Insira o numero: \n"))
            if numero == 1 and tentativa == 2:
                print("Ganhou! :), eu escolhi",numero)
            if numero == 2 and tentativa == 2:
                print("Empate! Jogue novamente!")
                tentativa = int(input("Insira o numero: \n"))
            if numero == 3 and tentativa == 2:
                print("Perdeu! :(, eu escolhi",numero)
            if numero == 1 and tentativa == 1:
                print("Empate! Jogue novamente!")
                tentativa = int(input("Insira o numero: \n"))
            if numero == 2 and tentativa == 1:
                print("Perdeu! :(, eu escolhi",numero)
            if numero == 3 and tentativa == 1:
                print("Ganhou! :), eu escolhi",numero)
        qtd_tentativas1 += 1
        





