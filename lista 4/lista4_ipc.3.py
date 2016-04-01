#Beatriz Pessoa Longato 1615310001

notas = []

quantidade_notas= 4

media = 0

for i in range (quantidade_notas):
    
    notas.append(float(raw_input("Digite a nota: ")))
    
    media = media + notas[i]
    
media = media / quantidade_notas

print (notas)

print "A média é" , (media)
