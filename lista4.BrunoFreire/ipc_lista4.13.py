mes=["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
temp=[]
soma=0
cont=1
media=0
cont2=1

for i in range(12):
    t=float(input("digite a temperatura do mes %d:"%cont))
    temp.append(t)
    soma+=t
    cont+=1
media= soma/12
print("essa e a media de temperatura:%d"%media)

for x in range(12):
    if temp[x]>media:
        print("%d - %s"%(cont2,mes[x]))
    cont2+=1
    
            