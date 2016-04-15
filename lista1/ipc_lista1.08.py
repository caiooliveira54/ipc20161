#Introdução a Programação de Computadores
#Professor: Jucimar Junior
#Any Mendes Carvalho - 1615310044
#Kid Mendes de Oliveira Neto - 1615310011
#Victor Rafael da Silva e Silva - 1615310025
#Eduardo Maia Freire - 1615310003
#Luiz Alexandre Olivera de Souza-1615310057
#Matheus Palheta Barbosa -1615310019
#
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

QntHora = input("Entre com o valor de seu rendimento por hora: ")  
hT = input("Entre com a quantidade de horas trabalhadas no mês: ")  
  
Salario = round(QntHora*hT,2) 

print (("\n Voce ganhou %.2f reais neste mes") % (Salario))  




