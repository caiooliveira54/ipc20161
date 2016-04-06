#Bruno de Oliveira Freire - 1615310030
v=[]
soma=0
i=0
m=1

for i in range(5):
    n=int(input("insira um numero inteiro:"))
    v.append(n)
    soma=soma+v[i]
    m=m*v[i]
    i+=1
    
print("esse e a lista:%s"%v)
print("esse e a soma dos elementos da lista:%d"%soma)
print("essa e a multiplicaçao dos elementos da lista:%d"%m)
