#Introdução a programação de computadores;
#Professor: Jucimar Junior
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#Caio de Oliveira Martins - 1615310031
#Antonio Rodrigues de Souza Neto - 1615310028
#Calebe Roberto Chaves da Silva Rebello - 1615310043

valida = 0

while (valida ==0 ):
    pop_A = float(input("Informe o numero da população A : \n"))
    pop_B = float(input("Informe o numero da população B : \n"))
    
    cresc_A = float(input("Informe a taxa de crescimeto da população A: \n"))
    cresc_B = float(input("Informe a taxa de crescimeto da população B: \n"))
    
    anos = 0
    
    while (pop_A < pop_B):
        anos +=1
        pop_A = (pop_A + (pop_A * cresc_A))
        pop_B = (pop_B + (pop_B * cresc_B))        


print ("Apos", anos, "anos a populacao A superou a de B")
print ("Populacao de A: ", pop_A)
print ("Populacao de B: ", pop_B)
valida = int(input("Quer calcular de novo? 0-Sim - 1-Nao: \n"))
