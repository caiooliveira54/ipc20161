"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e 
armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
simulando os lançamentos dos dados.
"""
from random import randint
lan = []
vetcont = [0,0,0,0,0,0]

for i in range(100):
    dado = randint(1,6)
    if dado == 1:
        vetcont[0] += 1
    elif dado == 2:
        vetcont[1] += 1
    elif dado == 3:
        vetcont[2] += 1
    elif dado == 4:
        vetcont[3] += 1
    elif dado == 5:
        vetcont[4] += 1
    elif dado == 6:
        vetcont[5] += 1
    lan.append(dado)
    
print(lan)
print(vetcont)