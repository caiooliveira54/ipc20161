#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

area = float(input("Qual a área para ser pintada? "))

litros = area/6
latas = litros//18
litros = litros - (latas*18)
galoes = litros//3.6
p_lata = latas * 80
p_gal = galoes * 25

print ("Quantidade de litros necessária: %.0f \nNúmero total de latas %.0f e galões %.0f\nPreço total em latas é R$%.2f e galões R$%.2f"%(litros, latas, galoes, p_lata, p_gal))
