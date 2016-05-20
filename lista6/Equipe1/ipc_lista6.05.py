def somar_n (n):
    if n == 1:
        return 1
    else:
        return n + somar_n(n-1)

numero = int(input("Digite um numero: "))
print ("A soma dos numeros de 1 a %d é %d" %(numero,somar_n(numero)))
