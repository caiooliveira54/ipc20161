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

altura = float(input("Entre com a sua altura: ")) # Solicita a altura do usuário
sexo = input("Sexo M ou F: ") # Logo após isso solicita o sexo do usuário
peso = float(input("Qual seu peso: "))  # E por último solicita
    
if ("F" == sexo): # Verificará se o sexo é feminino, se sim, calculará o peso ideal
     resultado = (62.1*altura) - 44.7  
else:  # Caso seja masculino, calculará o peso ideal
     resultado = (72.7*altura) - 58     
  
if (peso > resultado): # Se o peso for maior que o peso ideal, imprimirá que está acima do peso
    print("Voce esta acima do peso, seu peso ideal e %.1f kg" % (resultado)) 
else: # Caso contrário, abaixo do peso ideal
    print("Voce esta abaixo do peso, seu peso ideal e %.1f kg" % (resultado))
