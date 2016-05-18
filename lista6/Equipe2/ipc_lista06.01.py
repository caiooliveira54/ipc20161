#Introdução à Programaçãol de Computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo Rocha Melo - 1615310015
#Igor Menezes Sales Vieira - 1615310007

def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        fat = n*fatorial(n-1)
        print(fat)
    return fat

n = int(input("Digite um valor: "))
print("Resposta: ")
fatorial = fatorial(n)
