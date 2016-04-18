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

tamanho = float(input("Tamanho do arquivo em mb:\n")) # Solicita ao usuário o tamanho do arquivo a ser baixado
velocidade = float(input("Velocidade do link:\n")) # Solicita ao usuário a velocidade da internet

tempo = (tamanho)/(velocidade/60) # Calcula o tempo estimado do download

print("Tempo estimado:",tempo) # Imprime ao usuário o tempo do download
