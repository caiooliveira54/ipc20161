#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 3
#
#Antonio Rodrigues de Souza Neto - 1615310028
#Caio de Oliveira Martins - 1615310031
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Felipe Henrique Bastos Costa - 1615310032
#Lorene da Silva Marques - 1615310013
#

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
