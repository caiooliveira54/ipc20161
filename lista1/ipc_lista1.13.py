#Alexander Emerson Batalha Carlos - 1615310051
#Any Mendes Carvalho - 1615310044
#Ariel Guilherme Rocha Capistrano - 1615310029
#Beatriz Pessoa Longato - 1615310001
#Nickso Patrick Façanha Calheiros - 1615310059

#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 (h = altura)
#Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
 
altura = input("Entre com a sua altura: ")  
sexo = str(raw_input("Sexo M ou F:"))  
peso = input("Qual seu peso: ")  
    
if ("F" == sexo):          
     resultado = (62.1*altura) - 44.7  
else:  
     resultado = (72.7*altura) - 58     
  
if (peso > resultado):            
    print "Voce esta acima do peso, seu peso ideal e %.1f kg" % (resultado)  
else:  
    print "Voce esta abaixo do peso, seu peso ideal e %.1f kg" % (resultado) 