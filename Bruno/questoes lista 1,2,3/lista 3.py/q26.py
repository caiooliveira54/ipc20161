eleit = int(input(" quantos eleitores ha : "))
acm = 1
cand1 = 1
cand2 = 2
cand3 = 3

soma1 = 0
soma2 = 0
soma3 = 0
while (acm <= eleit):
    print(" 1 - Candidato 1\n 2 - Canditado 2\n 3 - Candidato 3\n" )
    voto = int(input("  vote aqui : "))
    
    if( voto == cand1 ):
        soma1 = soma1 + 1
        print(" O voto foi no candidato 1 " )
        acm = acm + 1
    elif( voto == cand2 ):
        soma2 = soma2 + 1
        print(" O voto foi no candidato 2 " )
        acm = acm + 1
    elif( voto == cand3 ):
        soma3 = soma3 + 1
        print(" O voto foi no candidato 3 " )
        acm = acm + 1
    else:
        print("Candidato Inexistente")
        
print(" o candidato 1 recebeu : \n %d votos " %soma1 )
print(" o candidato 2 recebeu : \n %d votos " %soma2 )
print(" o candidato 3 recebeu : \n %d votos " %soma3 )
