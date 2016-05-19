def fat_duplo(num):
    if num % 2 == 0:
        return "Não se tem fatorial duplo de número par"
    if num == 0:
        return 1
    if num == 1:
        return num
    else:
        return num * fat_duplo(num-2)

print ("Programa que calcula o fatorial duplo de um número ímpar")
numero = int(input("Qual o numero que deseja-se calcular? "))
print ("\nResultado =", fat_duplo(numero))


    
