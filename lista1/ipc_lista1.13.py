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
#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 (h = altura)
#Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

altura = float(input("Entre com a sua altura: "))
sexo = input("Sexo M ou F: ")
peso = float(input("Qual seu peso: ")) 
    
if ("F" == sexo):          
     resultado = (62.1*altura) - 44.7  
else:  
     resultado = (72.7*altura) - 58     
  
if (peso > resultado):            
    print("Voce esta acima do peso, seu peso ideal e %.1f kg" % (resultado)) 
else:
    print("Voce esta abaixo do peso, seu peso ideal e %.1f kg" % (resultado))