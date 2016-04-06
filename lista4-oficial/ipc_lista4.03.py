# Calebe Roberto Chaves da Silva Rebello - 1615310043

vetor = []
acm = 0
contador = 0
while contador < 4:
    nota = int(input("Digite sua nota: "))
    vetor.append(nota)
    acm = acm + nota
    contador = contador + 1

media = acm/contador
print(vetor)
print(media)
