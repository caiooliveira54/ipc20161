#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 1
#
#Any Mendes Carvalho - 1615310044
#Eduardo Maia Freire - 1615310003
#Kid Mendes de Oliveira Neto - 1615310011
#Luiz Gustavo de Rocha Melo - 1615310015
#Matheus Palheta Barbosa -1615310019
#Victor Rafael da Silva e Silva - 1615310025
#

metros = int(input("Digite a area para ser pintada: "))

cobertura = metros/3
qtd_tinta = cobertura//18
preco_total = qtd_tinta * 80

print ("Voce precisara de %d latas de tinta e custara R$%.2f" %(qtd_tinta, preco_total))
