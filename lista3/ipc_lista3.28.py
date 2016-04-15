#Introduçao a programaçao de computadores
#Professor: Jucimar Junior
#Bruno de Oliveira Freire - 1615310030
#Thiago Santos Borges - 1615310023
#Nickso Patrick Façanha Calheiros - 1615310059
#Matheus Mota de Souza - 1615310016
#Igor Menezes Sales Vieira - 1615310007
q_cds=float(input("informe a quantidade de cds:\n"))
cont=0
valor_total=0
numero=0


while (cont<q_cds):
    numero+=1
    valor=float(input("informe quanto custa o cd %d:"%numero))
    valor_total=valor_total+valor
    media=valor_total/q_cds
    cont+=1
    
print("esse e o valor total:%.2f"%valor_total)
print("essa e a media:%.2f"%media)
    
    
   
    
