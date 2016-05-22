def par_decrescente(num):
    if num == 0:
        return 0
    if num % 2  == 0:
        return str(num) + " " +str(par_decrescente(num-2))

num = int(input("Informe um numero: "))
x = par_decrescente(num)
print ("Sequencia par decrescente de %d: " %(num),x)