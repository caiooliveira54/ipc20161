
#Grupo: 2
# Lucas Ferreira Soares - 1615310014
# Ana Beatriz Frota - 1615310027
# 
#Lista: 4
#Questão: 17

vet = []
nome = input("Atleta: ")

salto1 = float(input("Primeiro salto:"))

vet.append (salto1)

salto2= float(input("Segundo salto:"))

vet.append (salto2)

salto3 = float(input("Terceiro salto:"))

vet.append (salto3)

salto4 = float(input("Quarto salto:"))

vet.append (salto4)

salto5 = float(input("Quinto salto:"))

vet.append (salto5)

print("Resultado final:")
print("Atleta:",nome)
print("Saltos:",vet[0],"-",vet[1],"-",vet[2],"-",vet[3],"-",vet[4])
media = ((vet[0]+vet[1]+vet[2]+vet[3]+vet[4])/5)
print("Média dos saltos:",media)


        
