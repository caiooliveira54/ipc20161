#Beatriz Pessoa Longato 1615310001

cont=1
x=10
L= []

while cont <= x:
    L.append(int(raw_input("Digite um número: ")))
    
    cont +=1
    
print (L)    

print (list(reversed(L)))
