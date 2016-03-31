#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição
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
