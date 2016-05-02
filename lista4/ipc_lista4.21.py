#Beatriz Pessoa Longato 1615310001 
#Equipe 3 



carros=[]

kmsporlitro=[]

litrospara1000=[]

precopara1000=[]

menor_consumo=0

pos=0

print (" ")

print ("Comparativo de Consumo de Combustível")

print (" ")

for i in range (5):
    carro=raw_input('Veículo: ' )
    kmporlitro= float(raw_input("Km por litro: "))
    
    carros.append(carro)
    kmsporlitro.append(kmporlitro)
    print (" ")
    
for i in kmsporlitro:
    litrosparamilkm= 1000 / i
    
    litrospara1000.append(round(litrosparamilkm,2))
    
for i in litrospara1000:
    
    precoparamilkm= 2.25 * i
    
    precopara1000.append(round(precoparamilkm,2))

print ("  ")
print ("Relaatório Final:")
print (" ")
print ("Modelo:  KM/L:  Consumo para Mil KM:  Preço em R$ para Mil KM:")
    
for i in range (5):
    
    print " "
    print carros[i] , kmsporlitro[i] , litrospara1000[i] , precopara1000[i]

for i in range (5):
        
    if kmsporlitro[i] > menor_consumo:
            
        menor_consumo = kmsporlitro[i]
            
        pos=i

print "O menor consumo foi do carro" , carros[pos]
            
            
        
    

        
        
        
        
    
    
    

