def multiplicar(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    if n1 == 1:
        return n2
    if n2 == 1:
        return n1
    else:
        n = n1 * n2        
        if n1 != n:
            return n1 + n1*(n2-1)

n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
n = multiplicar(n1, n2)
print(n)