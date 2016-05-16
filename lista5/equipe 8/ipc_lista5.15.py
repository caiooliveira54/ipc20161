#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#

from matriz import*

cidades = (1,2,3,4)

ligacoes_cidades = [[1,1,0,0],
                    [0,1,1,1],
                    [0,1,1,0],
                    [0,1,0,1],]

def contar_estradas_saindo(tabela, cidade):
    saidas = -1
    for i in tabela[cidade]:
        if(i == 1):
            saidas += 1
    return saidas

def contar_estradas_chegando(tabela, cidade):
    entradas = -1
    for j in range(len(tabela[0])):
        if(tabela[j][cidade] == 1):
            entradas += 1
    return entradas

def determinar_cidade_com_mais_estradas(tabela):
    mais_estradas = 0
    cidade = 0
    for i in range(len(tabela)):
        estradas = contar_estradas_chegando(tabela, i) + contar_estradas_saindo(tabela, i)
        if(estradas > mais_estradas):
            mais_estradas = estradas
            cidade = i
    return cidade

print(determinar_cidade_com_mais_estradas(ligacoes_cidades))

def determinar_mao_dupla(tabela, cidade):
    for i in range(len(tabela[cidade])):
        if tabela[cidade][i] == 1:
            if tabela[i][cidade] != 1:
                return False
    return True

def determinar_saidas_diretas(tabela, cidade):
    saidas = []
    for i in range(len(tabela[cidade])):
        if(tabela[cidade][i] == 1):
            if(cidade != i):
                saidas.append(i)
    return saidas    

def verificar_cidade_isolada(tabela, cidade):
    if((contar_estradas_chegando(tabela, cidade) + contar_estradas_saindo(tabela, cidade)) == 0):
        return True
    else:
        return False
    
def verificar_trajeto(trajeto, tabela):
    anterior = trajeto[0]
    for i in trajeto:
        if(tabela[anterior][i] == 1):
            anterior = i
        else:
            return False
    return True
        

print(verificar_trajeto([0,1,2,1,3], ligacoes_cidades))

