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
