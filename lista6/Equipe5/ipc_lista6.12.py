#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def sequencia_crescente(num):
    if num  == 0:
        return 0
    else:
        return str(sequencia_crescente(num-1))+ " " +str(num) 
                   
num = int(input("Valor: "))
x = sequencia_crescente(num)
print ("Sequencia crescente ate %d: "%(num),x)