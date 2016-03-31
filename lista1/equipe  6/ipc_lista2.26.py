#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
#

litros = float(input("Quantidade de litros:\n"))
tipo_combustivel = raw_input("Tipo de combustivel (A)-alcool ou (G)-gasolina:")

if(tipo_combustivel == "A" or tipo_combustivel == "a"):
    if(litros <= 20):
        preco_alcool = (litros*1.90)
        preco_total_desconto = (preco_alcool-(preco_alcool*3/100))
        print("Valor total: R$",preco_total_desconto)
    if(litros > 20):
        preco_alcool = (litros*1.90)
        preco_total_desconto = (preco_alcool-(preco_alcool*5/100))
        print("Valor total: R$",preco_total_desconto)
if(tipo_combustivel == "G" or tipo_combustivel == "g"):
    if(litros <=20):
        preco_gasolina = (litros*2.50)
        preco_total_desconto = (preco_gasolina-(preco_gasolina*4/100))
        print("Valor total: R$",preco_total_desconto)
    if(litros > 20):
        preco_gasolina = (litros*2.50)
        preco_total_desconto = (preco_gasolina-(preco_gasolina*6/100))      
        print("Valor total: R$",preco_total_desconto)
        
