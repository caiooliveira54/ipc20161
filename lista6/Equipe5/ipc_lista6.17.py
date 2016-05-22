
#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def fatorial (num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fatorial(num-1)

def fatorialquad(num):
        return fatorial(2*num)/ fatorial(num)
    
num =  int(input("Informe um numero inteiro: "))
print (fatorialquad(num))
