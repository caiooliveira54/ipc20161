def criar_vetor(elementos):
    vetor = []
    for i in range(elementos):
        num = int(input("Qual o %dº elemento? "%(i+1)))
        vetor.append(num)
    return vetor

def somar(vetor, ultimo):
    if ultimo == 0:
        return vetor[0]
    else:
        return vetor[ultimo] + somar(vetor, ultimo-1)

print ("Somador de elementos de um vetor")
elementos = int(input("Quantos elementos tem o vetor? "))
vetor = criar_vetor(elementos)
ultimo = len(vetor) - 1
print ("\nVetor =", vetor, "\n")
print ("A soma dos elementos do vetor é:", somar(vetor, ultimo))
