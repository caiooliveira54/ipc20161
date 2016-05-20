def somar_vetor(vetor,ac):
    if len(vetor) + ac == 0:
        return vetor[0]
    else:
        return vetor[ac] + somar_vetor(vetor,ac-1)

def criar_vetor(n):
    vetor = []
    for i in range(n):
        nume = int(input("Vetor na posicao %d: " % (i+1)))
        vetor.append(nume)
    return vetor
        

limite = int(input("Difite o tamanho do vetor: "))
vetor = criar_vetor(limite)
ac = -1
print (vetor)
print (somar_vetor(vetor,ac))
