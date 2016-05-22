#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def fatorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        x = num * fatorial(num-1)
        print (x)
    return x

num = int(input("Que número que deseja fatorar? "))
x = fatorial(num)
print ("Resultado de %d!:"%(num),x)
