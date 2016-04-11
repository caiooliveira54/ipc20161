#bruno de Oliveira Freire - 1615310030
nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))

media = ((nota1 + nota2)/2)

if(media <= 10):
    if(media >= 9) and (media <= 10):
        print(nota1)
        print(nota2)
        print(media)
        print("A")
        print("APROVADO")
    if(media < 9) and (media >= 7.5):
        print(nota1)
        print(nota2)
        print(media)
        print("B")
        print("APROVADO")
    if(media < 7.5) and (media >= 6):
        print(nota1)
        print(nota2)
        print(media)
        print("C")
        print("APROVADO")
    if(media < 6) and (media >= 4):
        print(nota1)
        print(nota2)
        print(media)
        print("D")
        print("REPROVADO")
    if(media < 4) and (media >= 0):
        print(nota1)
        print(nota2)
        print(media)
        print("E")
        print("REPROVADO")
else:
    print("media inalcançável")
