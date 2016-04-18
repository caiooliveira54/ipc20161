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
  
number1 = int(input("Digite o primeiro numero inteiro:  ")) # Solicita um número inteiro ao usuário
number2 = int(input("Digite o segundo numero inteiro:  ")) # A mesma coisa que a anterior
nReal = float(input("Digite o numero real:  ")) # Aqui é solicitado um número real

resultado1 = (number1 * 2) * (number2 / 2) # Calcula o produto do dobro do primeiro número com a metade do segundo
resultado2 = (number1 * 3) + nReal # Calcula a soma do triplo do primeiro com o número real
resultado3 = nReal ** 3 # Aqui calcula o cubo do número real

print ("o produto do dobro do primeiro com metade do segundo = ",resultado1) # Impressão do produto do dobro do primeiro número com a metade do segundo
print ("a soma do triplo do primeiro com o terceiro = ",resultado2) # Impressão da soma do triplo do primeiro com o número real
print ("o terceiro elevado ao cubo",resultado3) # Impressão o cubo do número real
