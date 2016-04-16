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

morango = float(input("Quanto Kg de morango?\n"))
maca = float(input("Quanto Kg de maca?\n"))

peso_total = (morango + maca)

if(0 < morango <= 5):
    preco_morango = (2.50*morango)
    if(0 < maca <= 5):
        preco_maca = (1.80*maca)
        preco_total = (preco_maca + preco_morango)
        if(peso_total > 8 or preco_total > 25):
            preco_total_desconto = (preco_total-(preco_total*10/100))
            print("O valor a ser pago e: R$"%preco_total_desconto)
        else:
            print("O valor a ser pago e: R$",preco_total)
    if(maca > 5):
        preco_maca = (1.50*maca)
        preco_total = (preco_maca + preco_morango)
        if(peso_total > 8 or preco_total > 25):
            preco_total_desconto = (preco_total-(preco_total*10/100))
            print("O valor a ser pago e: R$",preco_total_desconto)
        else:
            print("O valor a ser pago e: R$",preco_total)
    if(maca == 0):
        print("O valor a ser pago e: R$",preco_morango)
if(morango > 5):
    preco_morango = (2.20*morango)
    if(maca <= 5):
        preco_maca = (1.80*maca)
        preco_total = (preco_maca + preco_morango)
        if(peso_total > 8 or preco_total > 25):
            preco_total_desconto = (preco_total-(preco_total*10/100))
            print("O valor a ser pago e: R$",preco_total_desconto)
        else:
            print("O valor a ser pago e: R$",preco_total)
    if(maca > 5):
        preco_maca = (1.50*maca)
        preco_total = (preco_maca + preco_morango)
        if(peso_total > 8 or preco_total > 25):
            preco_total_desconto = (preco_total-(preco_total*10/100))
            print("O valor a ser pago e: R$",preco_total_desconto)
        else:
            print("O valor a ser pago e: R$",preco_total)
    if(morango > 8 and maca == 0 ):
        desconto_morango = (preco_morango-(preco_morango*10/100))
        print("O valor a ser pago e: R$",desconto_morango)
    if(maca == 0):
        print("O valor a ser pago e: R$",preco_morango)
elif(maca <= 5 and morango == 0 ):
    preco_maca = (1.80*maca)
    print("O valor a ser pago e: R$",preco_maca)
elif(maca > 5 and morango == 0):
    preco_maca = (maca*1.50)
    if(maca > 8):
        desconto_maca = (preco_maca-(preco_maca*10/100))
        print("O valor a ser pago: R$",desconto_maca)
    else:
        print("O valor a ser pago: R$",preco_maca)
    
