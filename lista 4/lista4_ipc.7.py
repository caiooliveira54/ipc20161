#Beatriz Pessoa Longato 1615310001

numeros=[]

quant_numero= 5

soma=0

mult=1

for i in range (quant_numero):
 
    n=int(raw_input("Digite um número: "))
    
    numeros.append(n)
    
    soma= soma + numeros[i]
    
    mult = mult * numeros[i]
    
print (numeros)

print (soma)

print (mult)


    
    
    
    
    
    