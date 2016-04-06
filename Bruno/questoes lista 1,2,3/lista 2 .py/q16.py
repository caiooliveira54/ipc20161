
print("Digite os valores para equacao ax2+bx+c")
a = float(input("digite a: "))
if(a!=0):
    b = float(input("digite b: "))
    c = float(input("digite c: "))
    delta = (b**2)-(4*a*c)
    
    raiz1 = ((-1)*b + delta**0.5)/2*a
    raiz2 = ((-1)*b - delta**0.5)/2*a
    if(delta<0): 
         print("Nao possui raizes reais")
    if(delta==0):
         print("Possui apenas uma raiz",raiz1)
    if(delta>0):
         print(raiz1)
         print(raiz2)
else:
    print("Nao e do segundo grau")






