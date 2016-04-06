#Bruno de Oliveira Freire - 1615310030
s=1
v=[]
v2=[]
i=0
c=0


for i in range(10):
    n=str(raw_input("digite um %d caracter:"%s))
    v.append(n)
    
    
    
    if v[i] != "a"  and v[i] != "e" and v[i] != "i" and v[i] != "o" and v[i] !="u":
        v2.append(v[i])
        c+=1
        
    s+=1    
        
    i+=1  
print(v)
print("essa e a quantidade de consoantes:%d"%c)
print(v2)
    