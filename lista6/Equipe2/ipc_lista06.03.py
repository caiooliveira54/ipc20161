#Introdução à Programaçãol de Computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo Rocha Melo - 1615310015
#Igor Menezes Sales Vieira - 1615310007

def inverter(n):
    if len(str(n)) == 1:
        return 1
    else:
        return str(n%10) + str(inverter(n//10))
n = int(input("Valor: "))
inv = inverter(n)
print(inv)
