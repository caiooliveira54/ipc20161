#bruno de Oliveira Freire - 1615310030
nota1 = float(input(" qual a sua primeira nota ? "))
nota2 = float(input(" qual a sua segunda nota ?"))
media = (nota1 + nota2)/2
if(media>=7 and media<10):
    print("aprovado")
elif(media==10):
    print("aprovado com distinção")
else:
    print("reprovado")
