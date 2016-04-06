#Bruno de Oliveira Freire - 1615310030
altura=[]
idade=[]
media=0
a=0
qtd_aluno=30
v=1
acm=0
r=0
acm2=0    

for x in range(qtd_aluno):
    print("-----------idade e altura do aluno %d----------------"%v)
    
    alt=float(input("insira a altura do aluno %d:"%v))
    ida=int(input("insira a idade do aluno %d:"%v))
    altura.append(alt)
    idade.append(ida)
    a=a+altura[x]
    media=a/30
    v+=1    
for i in range(30):
    if idade[i] > 13 and altura[i] < media:
        r+=1    


print(---------------------------------------------------------)
print("essa e a quantidade de alunos com idade maior que 13 e altura abaixa da media:%d"%r)
print("essa é a media das alturas:%.2f"%media)