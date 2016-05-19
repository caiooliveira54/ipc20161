def fat(numero):
    if numero == 0:
        return 1
    if numero == 1:
        return 1
    else:
        return numero * fat(numero-1)
    
def fat_quad(doisene, n):
    if n == 1 or doisene == 1:
        return fat(1)
    else:
        return fat(doisene)/fat(n)

print ("Programa que calcula o fatorial quádruplo de um número (2*n)!/n!")
numero = int(input("Qual o valor para N? "))
dobro_numero = 2 * numero
print ("\n%d!/%d! ="%(dobro_numero, numero), int(fat_quad(dobro_numero, numero)))
