#bruno de Oliveira Freire - 1615310030
hora=float(input("quantas horas voce trabalha?:\n"))
ganho_hora=float(input("quanto voce ganho por hora?:\n"))
ir=0
bruto=hora*ganho_hora
fgts=bruto*0.11
inss=bruto*0.05
desconto=bruto-inss-ir
salario_liquido=bruto-desconto

if bruto<=900:
    ir=bruto*0
    print("o salario bruto é:R$ %.2f"%bruto)
    print("o imposto de renda é: %.2f"%ir)
    print("o valor do inss e:R$ %.2f"%inss)
    print("o valor do fgts e:R$ %.2f"%fgts)
    print("o desconto total vale: R$ %.2f"%desconto)
    print(" o salario liquido vale:R$ %.2f"%salario_liquido)
    
if 900<bruto<=1500:
    ir=bruto*0.05
    print("o salario bruto é:R$ %.2f"%bruto)
    print("o imposto de renda é: %.2f"%ir)
    print("o valor do inss e:R$ %.2f"%inss)
    print("o valor do fgts e:R$ %.2f"%fgts)
    print("o desconto total vale: R$ %.2f"%desconto)
    print("o salario liquido vale:R$ %.2f"%salario_liquido) 
    
if 1500<bruto<=2500:
    ir=bruto*0.10
    print("o salario bruto é:R$ %.2f"%bruto)
    print("o imposto de renda é: %.2f"%ir)
    print("o valor do inss e:R$ %.2f"%inss)
    print("o valor do fgts e:R$ %.2f"%fgts)
    print("o desconto total vale: R$ %.2f"%desconto)
    print("o salario liquido vale:R$ %.2f"%salario_liquido)  
    
if bruto>=2500: 
    ir=bruto*0.20
    print("o salario bruto é:R$ %.2f"%bruto)
    print("o imposto de renda é: %.2f"%ir)
    print("o valor do inss e:R$ %.2f"%inss)
    print("o valor do fgts e:R$ %.2f"%fgts)
    print("o desconto total vale: R$ %.2f"%desconto)
    print("o salario liquido vale:R$ %.2f"%salario_liquido)
        
        
     
     
    
    


