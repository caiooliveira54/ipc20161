def fat(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return num * fat(num-1)
    
def super_fat(num):
    if num == 1:
        return fat(1)
    else:
        return fat(num) * super_fat(num-1)

print ("Programa que calcula o superfatorial de um número: 1! * 2! * 3! * ... * (n-1)! * n! = ?")
numero = int(input("Qual o valor de N para calcular seu superfatorial? "))
print ("\nSF(%d) ="%(numero), super_fat(numero))
