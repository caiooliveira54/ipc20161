
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
        
        