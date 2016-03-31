#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
#


data = raw_input ("Digite uma data com o formato dd/mm/aaaa:\n")
dia  = int(data[0:2])
mes  = int(data[3:5])
ano  = int(data[6:10])
bissexto = (ano%100!=0 and ano%4 ==0 or ano%400==0)

if(dia <= 31):
    if(mes>=1 and mes<=12):
        if (dia > 29 and mes == 2):
            print("Data invalida")            
        if(dia == 29 and mes == 2 and bissexto):
            print("Data valida")
        elif(dia>28 and mes == 2 ):
            print("Data invalida")
        if(dia <=28 and mes == 2 ):
            print("Data valida")        
        if(dia>30 and mes == 4 or dia>30 and mes == 6 or dia>30 and mes == 9 or dia>30 and mes == 11):
            print("Data invalida")
        if(dia > 31 and mes == 1 or dia > 31 and mes == 3 or dia > 31 and mes == 5 or dia > 31 and mes ==7 or dia > 31 and mes == 8 or dia > 31 and mes == 10 or dia > 31 and mes == 12):
            print("Data invalida")
        if(dia <= 30 and mes == 4 or dia <= 30 and mes == 6 or dia<=30 and mes == 9 or dia<=30 and mes == 11):
            print("Data valida")
        if(dia <= 31 and mes == 1 or dia <= 31 and mes == 3 or dia <= 31 and mes == 5 or dia <= 31 and mes == 7 or dia <= 31 and mes == 8 or dia <= 31 and mes == 10 or dia <= 31 and mes == 12):
            print("Data valida")
        
    else:
        print("Data invalida")
else:
    print("Data invalida")
    
