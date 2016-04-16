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
        
