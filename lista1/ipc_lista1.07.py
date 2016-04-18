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
   
altura = float(input("Digite a altura do quadrado em metros: ")) # Aqui solicita ao usuário a altura do quadrado
largura = float(input("Digite a largura do quadrado em metros: ")) # Aqui solicita ao usuário a largura do quadrado 
                                                                  # Obs.: Por ser um quadrado, bastava apenas um lado

a = altura * largura # Processo que calcula a área do quadrado

print ("A area e: %.2f m²" %a) # Impressão ao usuário da área do quadrado
print ("O DOBRO da area e:",(a * 2), "m²") # Impressão do dobro da área
