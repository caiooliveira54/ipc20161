#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição

eleit = int(input("Quantos eleitores vão votar?\n"))
x = 1
x1 = 0
cand1 = 1
cand2 = 2
cand3 = 3
soma1 = 0
soma2 = 0
soma3 = 0

while(  x <= eleit ):
    n = int(input("Vote aqui:\n"))
    if( n == cand1 ):
        x = x + 1
        x1 = x1 + 1        
        soma1 = soma1 + 1
        print("O %dº eleitor votou no candidato 1"%x1)
    elif( n == cand2 ):
        soma2 = soma2 + 1
        print("O %dº eleitor votou no candidato 2"%x1)
    elif( n == cand3 ):
        soma3 = soma3 + 1
        print("O %dº eleitor votou no candidato 3"%x1)
    else:
        print("O %dº eleitor votou num candidato invalido"%x1)
        x1 = x1 - 1
print("O candidato 1 recebeu %d votos\nO candidato 2 recebeu %d votos\nE o candidato 3 recebeu %d votos"%(soma1,soma2,soma3))
