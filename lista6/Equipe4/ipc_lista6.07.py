def criar_vetor(elementos):
    vetor = []
    for i in range(elementos):
        num = int(input("Qual o %dº elemento? "%(i+1)))
        vetor.append(num)
    return vetor

def inverter(vetor, ultimo):
    if ultimo == 0:
        return vetor[ultimo]
    else:
        return str(vetor[ultimo]) + ", " + str(inverter(vetor, ultimo-1))

print ("Programa que inverte os valores de um vetor")
elementos = int(input("Quantos elementos possuem seu vetor? "))
vetor = criar_vetor(elementos)
ultimo = len(vetor) - 1
print ("\nVetor invertido =", "[",inverter(vetor, ultimo),"]")
