#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição
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
