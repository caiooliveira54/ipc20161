#Introduçao a Programação de Computadores
#Professor: Jucimar Junior
#Bruno de Oliveira Freire - 1615310030
#Igor Menezes Sales Vieira - 1615310007
#Matheus Mota de Souza - 1615310016
#Nadine da Cunha Brito - 1615310040
#Nickso Patrick Façanha Calheiros - 1615310059
#Thiago Santos Borges - 1615310023
#

a = int(input("Montar a tabuada de: "))
b1 = int(input("Começar por: "))
b2 = int(input("Terminar em: "))

print("Vou montar a tabuada de %d começando em %d e terminando em %d:"%(a,b1,b2))
while b2<= b1 :
    print("Erro!\nO numero final e menor que o inicial!\nPor favor, insira os numeros corretamente")
    a = int(input("Montar a tabuada de: "))
    b1 = int(input("Começar por: "))
    b2 = int(input("Terminar em: "))
    
while b1 <= b2 :
    formula = a*b1
    print("%d x %d = %d"%(a,b1,formula))
    b1 += 1
