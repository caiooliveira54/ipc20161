def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n-1)

num = int(input("Qual o número que deseja-se fatorar? \n"))
fatorial = fatorial(num)
print ("\n%d! ="%(num), fatorial)
