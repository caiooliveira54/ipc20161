

def somatorio(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + somatorio(n-1)

print("Digite o numero voce deseja somar: ")
n = int(input("(Vamos soma-lo de 1, ate o numero que voce digitou):"))
print(somatorio(n))
