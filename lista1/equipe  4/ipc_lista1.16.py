#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

metros = int(input("Digite a área para ser pintada: "))

cobertura = metros/3
qtd_tinta = cobertura//18
preço_total = qtd_tinta * 80

print ("Você precisará de %d latas de tinta e custará R$%.2f" %(qtd_tinta, preço_total))
