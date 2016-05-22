def fatorial (num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fatorial(num-1)

def fatorialquad(num):
        return fatorial(2*num)/ fatorial(num)
    
num =  int(input("Informe um numero inteiro: "))
print (fatorialquad(num))