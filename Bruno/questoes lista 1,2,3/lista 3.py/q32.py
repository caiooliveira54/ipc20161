num = int(input("Informe o numero que deseja fatorar:\n"))
cont = 1
fat = 1
x = ""  #string vazia
mult = "" #string vazia

while(cont <= num):
    fat *= cont
    x = str(cont) + mult + x
    mult = "." # a partir daqui o mult é uma string que recebe "."(ponto) nas 
               # demais repetições até o programa finalizar
    cont += 1
    
print("%d! = %s = %d"%(num,x,fat))