def fat(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return num * fat(num - 1)

def pot(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if base == 0:
        return 0
    else:
        return base * pot(base, exp-1)
    
def fat_exp(base, exp):
    return base * pot(base, exp-1)

print ("Programa que calcula o fatorial exponencial (n^(n-1)^(n-2)...)")
base = int(input("Qual o valor da base 'n'? "))
exp = fat(base-1)
print ("\nResultado =", fat_exp(base, exp))

    
