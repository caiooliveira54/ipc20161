a=[]
b=[]
k=[]
c=[]
x=0
p=1
for x in range(10):
    n1=int(input("insira o numero %d do vetor1:"%p))
    n2=int(input("insira o numero %d do vetor2:"%p))
    n3=int(input("insira o numero %d do vetor3:"%p))
    a.append(n1)
    b.append(n2)
    k.append(n3)
    p+=1
z=0
while z<=9:
    c.append(a[z])
    c.append(b[z])
    c.append(k[z])
    z+=1
print("elementos do primeiro vetor:%s"%a)
print("esses sao elementos do segundo vetor:%s"%b)
print("esses sao elementos do terceiro vetor:%s"%k)
print("numeros intercalado do vetor 1,2,3:%s"%c)
    
    

    
    
    