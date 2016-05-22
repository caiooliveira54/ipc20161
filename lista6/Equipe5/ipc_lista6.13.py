#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def sequencia_decrescente(num):
    if num == 0:
        return 0
    else:
        return str(num)+ " " +str(sequencia_decrescente(num-1))
                                  
num = int(input("Informe um valor: "))
x = sequencia_decrescente(num)
print ("Sequencia descrente ate %d: " %(num),x)
                                    