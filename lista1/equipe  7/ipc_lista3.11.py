"""
#lista de repetição

#Antonio Rodrigues de Souza Neto --- matrícula ----1615310028
#Gabriel Machado Moreira --- matrícula ----1615310034
#Luiz Gustavo de Rocha Melo --- matrícula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matrícula---1615310043

"""

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

c1 = x
c2 = y
soma = 0

if (c1 < c2):
    while (c1 < c2):
        print("Número %d"% c1)
        soma += c1
        c1 += 1

if (c2 < c1):
    while (c2 < c1):
        print("Número %d"% c2)
        soma += c2
        c2 += 1

print("A soma dos valores é",soma)
