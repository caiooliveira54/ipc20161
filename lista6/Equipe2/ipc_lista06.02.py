#Introdução à Programaçãol de Computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo Rocha Melo - 1615310015
#Igor Menezes Sales Vieira - 1615310007

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        f1b = fibonacci(n-1) + fibonacci(n-2)
    return f1b

n = int(input("Digite um valor: "))
fib = fibonacci(n)
print(fib)
