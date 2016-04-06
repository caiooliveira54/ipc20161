num = int(input("Informe até onde deseja analisar o codigo:\n"))
i = 1
x = 1

while x <= num :
    if x!=2 and x!=3 and x!=5 and x!=7:
        if  x%2!=0 and x%3!=0 and x%4!=0 and x%5!=0 and x%6!=0 and x%7!=0 and x%8!=0 and x%9!=0 and x!=1:
            print(x)
    else:
        print(x)
    x+=1
        
