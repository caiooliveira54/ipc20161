#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 1
#
#Any Mendes Carvalho - 1615310044
#Kid Mendes de Oliveira Neto - 1615310011
#Victor Rafael da Silva e Silva - 1615310025
#Eduardo Maia Freire - 1615310003
#Luiz Gustavo de Rocha Melo - 1615310015
#Matheus Palheta Barbosa -1615310019
#
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
#

metros = int(input("Digite a area para ser pintada: "))

cobertura = metros/3
qtd_tinta = cobertura//18
preco_total = qtd_tinta * 80

print ("Voce precisara de %d latas de tinta e custara R$%.2f" %(qtd_tinta, preco_total))
