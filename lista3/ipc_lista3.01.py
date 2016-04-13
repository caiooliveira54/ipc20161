#professor Jucimar junior
#Ana Jessye 1615310046, 
#Franklin Yuri 1615310033,
#Kylciane Freitas 1615310032 
#Madson Lemos 1615310037
#IPC_Lista3.1

nota = float(input("Informe uma nota entre 0 a 10: "))

while nota <0 or nota>10:
    print("Nota Invalida!")
    nota = float(input("Informe uma nota entre 0 a 10: "))

print ("Nota valida: ",nota)
