#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def somar (num):
    if num ==0:
        return 0
    if num == 1:
        return 1
    else:
        return num + somar(num-1)

num = int(input("Digite o numero que deseja somar: "))
print ("Resultado da soma do numero %d: " %(num),somar(num))