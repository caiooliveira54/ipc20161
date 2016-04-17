#
#Introdução a programação de computadores
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
#Faça um Programa que peça dois números e imprima o maior deles. 
#



num1 = float(input("Informe um numero: "))
num2 = float(input("Informe outro numero: "))

if (num1 > num2):
    print ("O maoir numero e: ",num1)
elif(num1 == num2):
    print("Os dois numeros sao iguais.")
else:
    print ("O maior numero e: ",num2)
