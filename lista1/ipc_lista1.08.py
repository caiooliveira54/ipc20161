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

QntHora = float(input("Entre com o valor de seu rendimento por hora: "))  
hT = float(input("Entre com a quantidade de horas trabalhadas no mês: "))
  
Salario = round(QntHora*hT,2) 

print ("/nVoce ganhou %.2f reais neste mes" %Salario)
