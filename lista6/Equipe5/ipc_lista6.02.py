#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def fibonacci (num):
    if num ==1:
        return 0
    if num ==2:
        return 1
    else:
        x = fibonacci(num-1) + fibonacci (num-2)
        print (x)
    return x

num = int (input("Informe um numero: "))
x = fibonacci(num)
print ("O fibonacci do numero %d e:"%(num), x)
