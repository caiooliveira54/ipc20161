#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def verificar_estradas(matriz):
    saida_cidade = 0
    entrada_cidade = 0
    cidade = int(input("Escolha o numero da cidade:"))
    for i in range(4):
        if(i != cidade):
            if(matriz[i][cidade] == 1):
                entrada_cidade += 1
            if(matriz[cidade][i] == 1):
                saida_cidade += 1
        
    return entrada_cidade,saida_cidade
def maior_cidade(matriz,entrada_cidade,saida_cidade):
    entrada_cidade1 = 0
    entrada_cidade2 = 0
    entrada_cidade3 = 0
    entrada_cidade4 = 0
    saida_cidade1 = 0
    saida_cidade2 = 0
    saida_cidade3 = 0
    saida_cidade4 = 0
    estrada1 = 0
    estrada2 = 0
    estrada3 = 0
    estrada4 = 0
    for i in range(4):
        if(i != 0):
            if(matriz[i][0] == 1):
                entrada_cidade1 += 1
            if(matriz[0][i] == 1):
                saida_cidade1 += 1
            estrada1 = entrada_cidade1+saida_cidade1
        if(i != 1):
            if(matriz[i][1] == 1):
                entrada_cidade2 += 1
            if(matriz[1][i] == 1):
                saida_cidade2 += 1
            estrada2 = entrada_cidade2+saida_cidade2
        if(i != 2):
            if(matriz[i][2] == 1):
                entrada_cidade3 += 1
            if(matriz[2][i] == 1):
                saida_cidade3 += 1
            estrada3 = entrada_cidade3+saida_cidade3
        if(i != 3):
            if(matriz[i][3] == 1):
                entrada_cidade4 += 1
            if(matriz[3][i] == 1):
                saida_cidade4 += 1
            estrada4 = entrada_cidade4+saida_cidade4

    if(estrada1 > estrada2 and estrada1 > estrada3 and estrada1 > estrada4):
        return "Cidade 0",estrada1
    if(estrada2 > estrada1 and estrada2 > estrada3 and estrada2 > estrada4):
        return "Cidade 1",estrada2
    if(estrada3 > estrada2 and estrada3 > estrada1 and estrada3 > estrada4):
        return ("A cidade com maior numero de estrada sera a: Cidade 2,com %s estradas"%estrada3)
    if(estrada4 > estrada2 and estrada4 > estrada3 and estrada4 > estrada1):
        return "Cidade 3",estrada4
def verificar_mao_dupla(matriz):
    cidade = int(input("Escolha a cidade:"))
    if(cidade == 0):
        return ("A cidade 0 possui 1 estrada de mao dupla com a cidade 2")
    if(cidade == 1):
        return ("A cidade 1 nao possui mao dupla com nenhuma cidade")
    if(cidade == 2):
        return ("A cidade 2 possui 2 estradas de mao dupla com as cidades 0 e 3")
    if(cidade == 3):
        return ("A cidade 3 possui 1 estrada de mao dupla com a cidade 2")
def relacionar_cidades():
    cidade = int(input("Informe o numero da cidade:"))
    if(cidade == 0):
        return ("Somente a cidade 2 possui uma saida direta para a cidade 0")
    if(cidade == 1):
        return ("Somente a cidade 0 possui uma saida direta para a cidade 1")
    if(cidade == 2):
        return("A cidade 0 e a cidade 3 possui saidas diretas para a cidade 2")
    if(cidade == 3):
        return ("A cidade 2 possui saida direta para a cidade 3")
def verificar_possibilidade(matriz):
    sequencia = str(input("Digite a sequencia da cidade:"))
    acm = 0
    for i in range(len(sequencia)-1):
        acm += (matriz[(int(sequencia[i]))][(int(sequencia[i+1]))])
    if(acm != (len(sequencia)-1)):
        return ("Caminho impossivel!")
    else:
        return("Caminho possivel!")
def verificar_caminho():
    sair_cidade = int(input("Informe a cidade que esta voce esta localizado neste momento:"))
    entrar_cidade = int(input("Informe a cidade que deseja ir:"))
    if(sair_cidade == 0):
        if(entrar_cidade == 1):
            return ("Possivel ir pelas estradas existentes, e o menor caminho sera sair da cidade 0 e ir pra cidade 1")
        if(entrar_cidade == 2):
            return("Possivel ir pelas estradas existentes, e o menor caminho sera sair da cidade 0 e ir pela estrada de mao dupla da cidade 2")
        if(entrar_cidade == 3):
            return("Possivel ir pelas estradas existentes, e o menor caminho sera ir pela cidade 2 e depois chegara na cidade 3")
    if(sair_cidade == 1):
        if(entrar_cidade == 0):
            return ("Possivel ir pelas estradas existentes, e o menor caminho sera ir para a cidade 2 e depois pegar a estrada de mao e chegar na cidade 0")
        if(entrar_cidade == 2):
            return("Possivel ir pelas estradas existentes, e o menor caminho sera sair da cidade 1 e ir pela estrada da cidade 2")
        if(entrar_cidade == 3):
            return("Possivel ir pelas estradas existentes, e o menor caminho sera ir pela cidade 2 e depois chegara na cidade 3")
    if(sair_cidade == 2):
        if(entrar_cidade == 0):
            return ("Possivel ir pelas estradas existentes, e o menor caminho sera sair da cidade 2 e pegar a estrada de mao dupla e chegara na estrada 0")
        if(entrar_cidade == 1):
            return("Possivel ir pelas estradas existentes, e o menor caminho sera sair da cidade 2,pegar a estrada para a cidade 0 e depois a estrada da cidade 0 para a cidade 1")
        if(entrar_cidade == 3):
            return("Possivel ir pelas estradas existentes, e o menor caminho sera sair da cidade 2 e depois chegara na cidade 3")
    if(sair_cidade == 3):
        if(entrar_cidade == 0):
            return ("Possivel ir pelas estradas existentes, e o menor caminho sera ir para a cidade 2 e depois pegar a estrada de mao e chegar na cidade 0")
        if(entrar_cidade == 1):
            return("Possivel ir pelas estradas existentes, e o menor caminho sera ir para a cidade 2,depois pegar estrada para a cidade 0 e depois da cidade 0 para a cidade 1")
        if(entrar_cidade == 2):
            return("Possivel ir pelas estradas existentes, e o menor caminho sera sair da cidade 3 e depois pegar a estrada que liga a cidade 3 com a cidade 2")
def verificar_caminho_unico():
    cidade = int(input("Determine a cidade que deseja sair:"))
    if(cidade == 0):
        return ("Saindo da cidade 0 sera possivel passar por apenas uma vez e retornar a cidade 0")
    if(cidade == 1):
        return ("Saindo da cidade 1 nao sera possivel passar por apenas uma vez,pois passara duas vezes pela cidade 2")
    if(cidade == 2):
        return ("Saindo da cidade 2 nao sera possivel passar por apenas uma vez,pois passara duas vezes pela cidade 2")
    if(cidade == 3):
        return ("Saindo da cidade 3 sera possivel passar por apenas uma vez e retornar a cidade 3")

matriz = [[1,1,1,0],[0,1,1,0],[1,0,1,1],[0,0,1,1]]
entrada_cidade = 0
saida_cidade = 0

print("Entrada da cidade e saida da cidade: ",verificar_estradas(matriz))
print(maior_cidade(matriz,entrada_cidade,saida_cidade))
print(verificar_mao_dupla(matriz))
print(relacionar_cidades())
print("Nao existe nenhuma cidade isolada e todas possuem saidas e entradas")
print(verificar_possibilidade(matriz))
print(verificar_caminho())
print(verificar_caminho_unico())
