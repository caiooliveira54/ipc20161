#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def inverter(num):
    if len (str(num)) == 1:
        return num
    else:
        return str(num % 10) + str(inverter(num//10))

num = int(input("Que numero quer inverter? "))
x = inverter(num)
print ("Resultado da inverso de %d: "%(num),x)