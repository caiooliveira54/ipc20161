#Kylciane Cristiny Lopes Freitas - 1615310052
#Questão 14
pergunta = ["Telefonou para a vítima: ? ","Esteve no local do crime: ? ","Mora perto da vítima: ? ","Devia para a vítima: ? "
,"Já trabalhou com a vítima: ? "]
resp = []
cont = 0

for i in range(5):
  print (pergunta[i])
  rpt = raw_input("Responda Sim ou Nao :  ")
  resp.append(rpt)
  if rpt == "sim" :
    cont+=1
  
if cont == 2:
    print ("Suspeita")
elif cont > 2 and cont < 5:
    print ("Cumplice")
elif cont == 5:
    print("Assassina")
else:
    print("Inocente")

