import random

tentativas_max = 1
qtd_tentativas = 0
qtd_tentativas1 = 2
numero = random.randint(1,5)

Pedra = 1
Papel = 2
Tesoura = 3
Lagarto = 4
Spock = 5

print("Insira seu nome: ")
nome = input()

print("\nOla",nome,"\nVamos jogar!\n")
print("Voce tem apenas uma tentativa")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
print("4 - Lagarto")
print("5 - Spock")

tentativa = int(input("Insira um numero: \n"))

while qtd_tentativas < tentativas_max:
    if numero == 1 and tentativa == 1:
        print("Empate! Jogue novamente!")
        tentativa = int(input("Insira um numero: "))
    if numero == 1 and tentativa == 2:
        print("Ganhou! Eu tirei",numero)
    if numero == 1 and tentativa == 3:
        print("Perdeu! Eu tirei",numero)
    if numero == 1 and tentativa == 4:
        print("Perdeu! Eu tirei",numero)
    if numero == 1 and tentativa == 5:
        print("Ganhou! Eu tirei",numero)
    if numero == 2 and tentativa == 1:
        print("Perdeu! Eu tirei",numero)
    if numero == 2 and tentativa == 2:
        print("Empate! Jogue novamente!")
        tentativa = int(input("Insira um numero: "))
    if numero == 2 and tentativa == 3:
        print("Ganhou! Eu tirei",numero)
    if numero == 2 and tentativa == 4:
        print("Ganhou! Eu tirei",numero)
    if numero == 2 and tentativa == 5:
        print("Perdeu! Eu tirei",numero)
    if numero == 3 and tentativa == 1:
        print("Ganhou! Eu tirei",numero)
    if numero == 3 and tentativa == 2:
        print("Perdeu! Eu tirei",numero)
    if numero == 3 and tentativa == 3:
        print("Empate! Jogue novamente!")
        tentativa = int(input("Insira um numero: "))
    if numero == 3 and tentativa == 4:
        print("Ganhou! Eu tirei",numero)
    if numero == 3 and tentativa == 5:
        print("Ganhou! Eu tirei",numero)
    if numero == 4 and tentativa == 1:
        print("Ganhou! Eu tirei",numero)
    if numero == 4 and tentativa == 2:
        print("Perdeu! Eu tirei",numero)
    if numero == 4 and tentativa == 3:
        print("Ganhou! Eu tirei",numero)
    if numero == 4 and tentativa == 4:
        print("Empate! Jogue novamente!")
        tentativa = int(input("Insira um numero: "))
    if numero == 4 and tentativa == 5:
        print("Perdeu! Eu tirei",numero)
    if numero == 5 and tentativa == 1:
        print("Perdeu! Eu tirei",numero)
    if numero == 5 and tentativa == 2:
        print("Ganhou! Eu tirei",numero)
    if numero == 5 and tentativa == 3:
        print("Perdeu! Eu tirei",numero)
    if numero == 5 and tentativa == 4:
        print("Ganhou! Eu tirei",numero)
    if numero == 5 and tentativa == 5:
        print("Empate! Jogue novamente!")
        tentativa = int(input("Insira um numero: "))
    qtd_tentativas += 1
while qtd_tentativas < qtd_tentativas1:
    if tentativa != 1 and tentativa != 2 and tentativa != 3 and tentativa != 4 and tentativa != 5:
        print("Numero Invalido!")
        tentativa = int(input("Insira um numero: "))
        if numero == 1 and tentativa == 1:
            print("Empate! Jogue novamente!")
            tentativa = int(input("Insira um numero: "))
        if numero == 1 and tentativa == 2:
            print("Ganhou! Eu tirei",numero)
        if numero == 1 and tentativa == 3:
            print("Perdeu! Eu tirei",numero)
        if numero == 1 and tentativa == 4:
            print("Perdeu! Eu tirei",numero)
        if numero == 1 and tentativa == 5:
            print("Ganhou! Eu tirei",numero)
        if numero == 2 and tentativa == 1:
            print("Perdeu! Eu tirei",numero)
        if numero == 2 and tentativa == 2:
            print("Empate! Jogue novamente!")
            tentativa = int(input("Insira um numero: "))
        if numero == 2 and tentativa == 3:
            print("Ganhou! Eu tirei",numero)
        if numero == 2 and tentativa == 4:
            print("Ganhou! Eu tirei",numero)
        if numero == 2 and tentativa == 5:
            print("Perdeu! Eu tirei",numero)
        if numero == 3 and tentativa == 1:
            print("Ganhou! Eu tirei",numero)
        if numero == 3 and tentativa == 2:
            print("Perdeu! Eu tirei",numero)
        if numero == 3 and tentativa == 3:
            print("Empate! Jogue novamente!")
            tentativa = int(input("Insira um numero: "))
        if numero == 3 and tentativa == 4:
            print("Ganhou! Eu tirei",numero)
        if numero == 3 and tentativa == 5:
            print("Ganhou! Eu tirei",numero)
        if numero == 4 and tentativa == 1:
            print("Ganhou! Eu tirei",numero)
        if numero == 4 and tentativa == 2:
            print("Perdeu! Eu tirei",numero)
        if numero == 4 and tentativa == 3:
            print("Ganhou! Eu tirei",numero)
        if numero == 4 and tentativa == 4:
            print("Empate! Jogue novamente!")
            tentativa = int(input("Insira um numero: "))
        if numero == 4 and tentativa == 5:
            print("Perdeu! Eu tirei",numero)
        if numero == 5 and tentativa == 1:
            print("Perdeu! Eu tirei",numero)
        if numero == 5 and tentativa == 2:
            print("Ganhou! Eu tirei",numero)
        if numero == 5 and tentativa == 3:
            print("Perdeu! Eu tirei",numero)
        if numero == 5 and tentativa == 4:
            print("Ganhou! Eu tirei",numero)
        if numero == 5 and tentativa == 5:
            print("Empate! Jogue novamente!")
            tentativa = int(input("Insira um numero: "))
        
