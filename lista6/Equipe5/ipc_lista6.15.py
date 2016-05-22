#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def par_decrescente(num):
    if num == 0:
        return 0
    if num % 2  == 0:
        return str(num) + " " +str(par_decrescente(num-2))

num = int(input("Informe um numero: "))
x = par_decrescente(num)
print ("Sequencia par decrescente de %d: " %(num),x)
