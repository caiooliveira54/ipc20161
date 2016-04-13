#Gabriel Machado Moreira - 1615310034

"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi
conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""

vetor = [1, 2, 3, 4, 5, 6]

resultado = 0

c = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
i = 0

while c < 100:
        
    resultado = vetor[i]

    if resultado == 1:
        c1 += 1
    if resultado == 2:
        c2 += 1
    if resultado == 3:
        c3 += 1
    if resultado == 4:
        c4 += 1
    if resultado == 5:
        c5 += 1
    if resultado == 6:
        c6 += 1
    if i < 6:
        i += 1
    if i == 6:
        i = 0
    c += 1

print("NUMERO 1:",c1)
print("NUMERO 2:",c2)
print("NUMERO 3:",c3)
print("NUMERO 4:",c4)
print("NUMERO 5:",c5)
print("NUMERO 6:",c6)
