#Beatriz Pessoa Longato 1615310001

numeros= []

par= []

impar=[]

cont= 1

while cont <= 20:
    
    n=int(raw_input("Digite um número: "))
    
    numeros.append(n)
    
    cont +=1
    
    if n % 2 == 0:
        
        par.append(n)
        
    else:
        
        impar.append(n)
        
        
print (numeros)

print(par)

print(impar)
    
    
    

