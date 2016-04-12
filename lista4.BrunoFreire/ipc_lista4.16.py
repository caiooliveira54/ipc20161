s=[]
classificacao=[0,0,0,0,0,0,0,0,0,0]
x=0

while x!=1:
    
    bruto=float(input("digite a venda bruta da semana :"))
    x=int(input("digite 1 se quiser sair e 0 para continuar:"))
    salario= 200 + (bruto*0.09)
    s.append(salario)
    
    if salario>=200 and salario<=299:
        classificacao[0]+=1
    if salario>=300 and salario<=399: 
        classificacao[1]+=1
    if salario>=400 and salario<=499: 
        classificacao[2]+=1
    if salario>=500 and salario<=599:
        classificacao[3]+=1
    if salario>=600 and salario<=699:
        classificacao[4]+=1
    if salario>=700 and salario<=799: 
        classificacao[5]+=1
    if salario>=800 and salario<=899:
        classificacao[6]+=1
    if salario>=900 and salario<=999:
        classificacao[7]+=1
    if salario>=1000: 
        classificacao[8]+=1
print("%d ganham o salario tipo -a-"%classificacao[0])
print("%d ganham o salario tipo -b-"%classificacao[1])
print("%d ganham o salario tipo -c-"%classificacao[2])
print("%d ganham o salario tipo -d-"%classificacao[3])
print("%d ganham o salario tipo -e-"%classificacao[4])
print("%d ganham o salario tipo -f-"%classificacao[5])
print("%d ganham o salario tipo -g-"%classificacao[6])
print("%d ganham o salario tipo -h-"%classificacao[7])
print("%d ganham o salario tipo -i-"%classificacao[8])
        
        