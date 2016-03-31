"""
#lista de repetição

#Antonio Rodrigues de Souza Neto --- matrícula ----1615310028
#Gabriel Machado Moreira --- matrícula ----1615310034
#Luiz Gustavo de Rocha Melo --- matrícula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matrícula---1615310043

"""
while (1 == 1):
    cont = 1
    prod = 1   
    n = int(input("Digite um valor entre entre 0 e 15: "))
    if (n < 16) and (n >= 0):
        while (cont < n):
            prod = prod * (cont + 1)
            cont = cont + 1
        print("O valor de", n,"! é igual a: %3.f" %prod)
    else:
        print("VALOR INVÁLIDO!")
        n = int(input("Digite um valor entre entre 0 e 15: "))
