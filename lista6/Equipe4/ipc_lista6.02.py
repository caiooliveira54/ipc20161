def fib(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print ("Serie de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 41, 55, 89...")
num = int(input("Qual o termo que deseja-se obter da serie de Fibonacci? "))
fib = fib(num)
print ("\nO termo de ordem %d é:"%(num), fib)
