#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#

from matriz import*

tabela_custo = [[1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5],
                [1,2,3,4,5]]

def calcular_custo(rota, tabela):
    anterior = rota[0]
    custo = 0
    for i in rota:
        custo += tabela[anterior][i]
        anterior = i
    return custo

print(calcular_custo([1,1,2,3,4], tabela_custo))
           