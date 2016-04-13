#Alexander Emerson Batalha Carlos - 1615310051
#Any Mendes Carvalho - 1615310044
#Ariel Guilherme Rocha Capistrano - 1615310029
#Beatriz Pessoa Longato - 1615310001
#Nickso Patrick Façanha Calheiros - 1615310059

#Controle o redimento diario de João

peso = input("Informe o peso dos peixes: ")

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
    print "Você excedeu" ,excesso, "kg do numero permitido de peixes \n  O valor \
de sua multa e de R$",multa #não coube na linha

else:
    print"Voce nao excedeu o limite de peixes pescados"