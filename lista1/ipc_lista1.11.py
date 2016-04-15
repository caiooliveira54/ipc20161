#Introdução a programação de computadores
#Professor: Jucimar Junior
#Any Mendes Carvalho - 1615310044
#Kid Mendes de Oliveira Neto - 1615310011
#Victor Rafael da Silva e Silva - 1615310025
#Eduardo Maia Freire - 1615310003
#Luiz Alexandre Olivera de Souza-1615310057
#Matheus Palheta Barbosa -1615310019
#
#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:  
# a-o produto do dobro do primeiro com metade do segundo .  
# b-a soma do triplo do primeiro com o terceiro.  
# c-o terceiro elevado ao cubo.  
  
import math

number1 = input("Digite o primeiro numero inteiro:  ")
number2 = input("Digite o segundo numero inteiro:  ")
nReal = input("Digite o numero real:  ")
resultado1 = number1 * 2 * (number2 / 2)          
print ("o produto do dobro do primeiro com metade do segundo = "), resultado1   
resultado2 = number1 *  3 + nReal
print ("a soma do triplo do primeiro com o terceiro = "), resultado2
resultado3 = nReal ** 3
print ("o terceiro elevado ao cubo"), resultado3
