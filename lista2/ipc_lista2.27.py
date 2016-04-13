#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
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
    
