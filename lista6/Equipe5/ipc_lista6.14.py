#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def par_crescente(num):
    if num == 0:
        return 0
    if num % 2 == 0: 
        return str(par_crescente(num-2))+ " " +str(num)

num = int (input("Informe um numero: "))
x = par_crescente(num)
print ("Sequencia de numeros pares ate %d :" %(num),x) 
    