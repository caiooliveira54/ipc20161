"""
#lista de repetição

#Antonio Rodrigues de Souza Neto --- matrícula ----1615310028
#Gabriel Machado Moreira --- matrícula ----1615310034
#Luiz Gustavo de Rocha Melo --- matrícula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matrícula---1615310043

"""
n = int(input("Digite n: "))
A, B, cont = 1, 1, 2
print(A)
while cont < n:
    print(B)
    C = A + B
    A = B
    B = C
    cont += 1
print(C)
    
