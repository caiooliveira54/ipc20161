#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num-1)
    
def super_fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fatorial(num) * super_fatorial(num-1)

num = int(input("Qual superfatorial deseja saber? "))
print (super_fatorial(num))
