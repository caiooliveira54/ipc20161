#Bruno de Oliveira Freire -1615310030
A=[]
x=0
acm=0
u=1
print ("voce vai digitar 10 numeros e elevarei eles ao quadrado")

for x in range(10):
    n=int(input("digite o numero %d:"%u))
    q=n**2
    A.append(q)
    u+=1
w=len(A)-1
while w>=0:
    acm=acm+A[w]
    w-=1
    
print("esse e o quadrado dos numeros informados:%s"%A)    
print("essa e a soma dos quadrados:%s"%acm)    
    