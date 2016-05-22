#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def potenciacao (base, expoente):
    if base == 0:
        return 0
    if expoente == 0:
        return 1
    if expoente == 1:
        return base
    else:
        x = base * potenciacao(base, (expoente - 1))
    return x

base = int (input("Informe a base: "))
expoente = int (input("Informe o expoente: "))
x = potenciacao(base,expoente)
print ("%d elevado ao expoente %d é %d" %(base,expoente,x))
