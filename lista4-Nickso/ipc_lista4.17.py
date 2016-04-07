#Nickso Patrick Façanha Calheiros - 1615310059

cond = True
vetsalto = []
nomes = []
media = []
ac = 0
cont = 0

while cond :
    nome = input("Digite seu nome(s p/ sai): \n")
    if nome == "":
        break
    nomes.append(nome)
    salto1 = float(input("Primeiro Salto: "))
    salto2 = float(input("Segundo Salto: "))
    salto3 = float(input("Terceiro Salto: "))
    salto4 = float(input("Quarto Salto: "))
    salto5 = float(input("Quinto Salto: "))
    vetsalto.append([salto1, salto2, salto3, salto4, salto5])
    soma = salto1 + salto2 + salto3 + salto4 + salto5
    media.append(soma/5)
    
maior = media[0]
while cont < len(media):
    if maior < media[cont]:
        maior = media[cont]
        ac = cont
    cont += 1
v = len(vetsalto)
for i in range(v):
    print ("Atleta: %s" % nomes[i])
    print ("Primeiro Salto: %5.2f" % vetsalto[i][0])
    print ("Segundo Salto: %5.2f" % vetsalto[i][1])
    print ("Terceiro Salto: %5.2f" % vetsalto[i][2])
    print ("Quarto Salto: %5.2f" % vetsalto[i][3])
    print ("Quito Salto: %5.2f \n" % vetsalto[i][4])

print ("Reseltado Final!\n")
print ("Atleta: %s" % nomes[ac])
print ("Saltos: %5.2f - % 5.2f - %5.2f - %5.2f - %5.2f" %(vetsalto[ac][0], vetsalto[ac][1], vetsalto[ac][2], vetsalto[ac][3], vetsalto[ac][4]))
print ("Media dos saltos %5.2f" % maior)       
    
        
        
    
