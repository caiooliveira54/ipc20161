#Bruno de Oliveira Freire - 1615310030
x=[]
x2=[]

cont=0
cont2=0

while cont<=9:
    n=int(input("insira um numero:"))
    x.append(n)
    cont+=1
i=len(x)-1  
while cont2<=i:
    x2.append(x[i])
    i-=1         
    
print(x) 
print(x2)
