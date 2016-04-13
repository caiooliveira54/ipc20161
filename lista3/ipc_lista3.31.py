#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição
continua2 = True
while continua2 :
    
    continua = True
    acm = 0
    while continua :
        num = float(raw_input(" digite um número : " ))
        if( num == 0 ):
            continua = False
        acm = acm + num
    pagamento = float(input(" qual o pagamento ? " ))
    troco = pagamento - acm
    print(acm)
    print(troco)
    num2 = int(input(" quer continuar ? 1 para sim 2 para não " ))
    if( num2 != 1 ):
        continua2 = False
        
        
