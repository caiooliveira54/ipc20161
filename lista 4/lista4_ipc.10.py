#Beatriz Pessoa Longato 1615310001

a=[]

b=[]

c=[]

quantidade_elementos=10


for i in range(quantidade_elementos):
    
    n=float(raw_input("Digite um número para a lista A: "))
    
    a.append(n)
    
for i in range (quantidade_elementos):
    
    n2=float(raw_input("Digite um número para a lista B: "))
    
    b.append(n2)
    
for i,y in zip (a,b):
    
    c.append(i)
    c.append(y)
    
    
print (a) 
print (b)
print "Lista resultante intercalada:"
print (c) 

    
    











    
    
    

    
