def pot(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * pot(base, exp-1)

def hiper_fat(limite):
    if limite == 1:
        return pot(limite, limite)
    else:
        return pot(limite, limite) * hiper_fat(limite-1)

print ("Programa que imprime o hiperfatorial de um numero: 1¹ * 2² * 3³ * ... * N")
limite = int(input("Qual o valor de N para o hiperfatorial? "))
print ("\nO hiperfatorial de %d e:"%(limite), hiper_fat(limite))
