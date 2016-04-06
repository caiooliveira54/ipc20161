#Bruno de Oliveira Freire - 1615310030
v=[]
vp=[]
vi=[]
i=0
acm=1
print("voce vai inserir 20 numeros")

for i in range(20):
    n=int(input("insira o numero %d:"%acm))
    v.append(n)
    if v[i]%2==0:
        vp.append(v[i])
    else:
        vi.append(v[i])
    acm+=1    
    i+=1    
print(v)
print("esses sao os numeros pares:%s"%vp)
print("esses sao os numeros impares:%s"%vi)
        

