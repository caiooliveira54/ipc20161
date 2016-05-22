#Introducao a programacao de computadores
#Professor: Jucimar Junior
#Ana Jessye Almeida Antunes- 1615310046
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Goncalves dos Santos - 1615310033

def criar_vetor(num):
    vetor = []
    for i in range(num):
        x = int(input("Qual o %dº elemento? "%(i+1)))
        vetor.append(x)
    return vetor

def somar_vet(vetor, acm):
    if len(vetor) + acm == 0:
        return vetor[0]
    else:
        return vetor[acm] + somar_vet(vetor, acm-1)

num = int(input("Qual o tamanho do vetor? "))
vetor = criar_vetor(num)
acm =  - 1
print (vetor)
print ("A soma dos elementos deu:", somar_vet(vetor, acm))