#Beatriz Pessoa Longato 1615310001
#Equipe 3
#Algoritmo criado no python 2.7.10
#Sintam-se livres para fazer alterações e atualizações
a=[]

b=[]

c=[]

d=[]

quantidade_elementos=10


for i in range(quantidade_elementos):
    
    n=float(raw_input("Digite um número para a lista A: "))
    
    a.append(n)
    
for i in range (quantidade_elementos):
    
    n2=float(raw_input("Digite um número para a lista B: "))
    
    b.append(n2)
    
for i in range (quantidade_elementos):
    
    n3=float(raw_input("Digite um número para a lista C: "))
    
    c.append(n3)
    
    
for i,y,z in zip (a,b,c):
    
    d.append(i)
    d.append(y)
    d.append(z)
    
    
print (a) 
print (b)
print (c)
print "Lista resultante intercalada:"
print (d) 
