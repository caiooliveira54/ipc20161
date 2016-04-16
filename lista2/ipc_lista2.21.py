#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Kylciane Cristiny Lopes Freitas - 1615310052
#Franklin Yuri Gonçaves dos Santos - 1615310033
#Lucas Ferreira Soares - 1615310014
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049
#Luiz Alexandre Oliveira de Souza - 1615310057
#Ariel Guilherme Rocha Capistrano - 1615310029
#

saque = int(input("Valor do saque:"))


if(10<=saque and saque<=600):
    nota100 = int(saque/100)
    resto100 = (saque%100)
    if(resto100 == 0):
        print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100")
    elif(resto100>=50):
        nota50 = int(resto100/50)
        resto50 = (resto100%50)
        if(resto50 == 0):
            print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota50,"notas de 50")
        elif(resto50>=10):
            nota10 = int(resto50/10)
            resto10 = (resto50%10)
            if(resto10 == 0):
                print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota50,"notas de 50",nota10,"notas de 10")
            elif(resto10>=5):
                nota5 = int(resto10/5)
                resto5 = (resto10%5)
                if(resto5 == 0):
                    print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota50,"notas de 50",nota10,"notas de 10",nota5,"notas de 5")
                elif(resto5>=1):
                    nota1= int(resto5/1)
                    print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota50,"notas de 50",nota10,"notas de 10",nota5,"notas de 5",nota1,"notas de 1")
        elif(resto50>=5):
            nota5 = int(resto50/5)
            resto5 = (resto50%5)
            if(resto5 == 0):
                print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota50,"notas de 50",nota5,"notas de 5")
            elif(resto5>=1):
                nota1= int(resto5/1)
                print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota50,"notas de 50",nota5,"notas de 5",nota1,"notas de 1")        
    if(resto100<50):
        nota10 = int(resto100/10)
        resto10 = (resto100%10)
        if(resto10 == 0):
            print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota10,"notas de 10")
        elif(resto10>=5):
            nota5 = int(resto10/5)
            resto5 = (resto10%5)
            if(resto5 == 0):
                print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota10,"notas de 10",nota5,"notas de 5")
            elif(resto5>=1):
                nota1= int(resto5/1)
                print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota10,"notas de 10",nota5,"notas de 5",nota1,"notas de 1")
        elif(resto10>=1):
            nota1= int(resto10/1)
            print("Para sacar a quantia de R$",saque,"o programa fornece",nota100,"notas de 100",nota10,"notas de 10",nota1,"notas de 1")        
        
else:
    print("Esse valor nao pode ter o saque")
    
