#professor Jucimar junior
#Ana Jessye 1615310046, 
#Franklin Yuri 1615310033,
#Kylciane Freitas 1615310032 
#Madson Lemos 1615310037
#IPC_Lista3.5

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
