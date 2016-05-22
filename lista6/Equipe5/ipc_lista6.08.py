#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def mdc (x,y):
    if y == 0:
        return x
    else:
        return mdc(y,x%y)

x = int (input("Informe o valor de X: "))
y = int (input("Informe o valor de Y: "))
m = mdc(x,y)
print (m)