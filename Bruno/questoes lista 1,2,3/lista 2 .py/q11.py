#bruno de Oliveira Freire - 1615310030
salario=float(input("informe seu salario atual:\n"))

percentual1= salario*0.2
percentual2= salario*0.15
percentual3= salario*0.1
percentual4= salario*0.05

reajuste1=salario + percentual1
reajuste2=salario + percentual2
reajuste3=salario + percentual3
reajuste4=salario + percentual4

if(salario<=280):
    print("seu salario antigo era:%.2f"%salario)
    print("seu salario vai aumentar:20%")
    print("o valor do aumento é:%.2f"%percentual1)
    print("seu novo salario é:R$ %.2f"%reajuste1) 

if(280< salario <=700):
    print("seu salario antigo era:%.2f"%salario)
    print("seu salario vai aumentar:15%")
    print("o valor do aumento é:%.2f"%percentual2)
    print("seu novo salario é:R$ %.2f"%reajuste2)
        
if(700<salario<1500):
    print("seu salario antigo era:%.2f"%salario)
    print("seu salario vai aumentar:10%")
    print("o valor do aumento é:%.2f"%percentual3)
    print("seu novo salario é:R$ %.2f"%reajuste3) 
    
if(salario>=1500):
    print("seu salario antigo era:%.2f"%salario)
    print("seu salario vai aumentar:5%")
    print("o valor do aumento é:%.2f"%percentual4)
    print("seu novo salario é:R$ %.2f"%reajuste4)     
