#professor Jucimar junior
#Ana Jessye 1615310046, 
#Franklin Yuri 1615310033,
#Kylciane Freitas 1615310032 
#Madson Lemos 1615310037
#IPC_Lista3.4

pop_A = 80000 
pop_B = 200000
anos = 0
cresc_A = 0.03
cresc_B = 0.015

while (pop_A < pop_B):
    anos = anos+1
    pop_A = (pop_A + (pop_A * cresc_A))
    pop_B = (pop_B + (pop_B * cresc_B))

print ("Apos", anos, "anos a populacao A superou a de B")
print ("Populacao de A: ", pop_A)
print ("Populacao de B: ", pop_B)
