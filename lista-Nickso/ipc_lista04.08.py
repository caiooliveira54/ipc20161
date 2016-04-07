vetoridade = []
vetoraltura =[]
cont = 0
i = 1
while cont < 5:
     idade = float(input("Digite sua Idade: "))
     altura = float(input("Digite sua Alura: "))
     vetoridade.append(idade)
     vetoraltura.append(altura)
     cont = cont + 1
while i <= len(vetoridade) or i <= (vetoraltura):
         print (vetoridade[len(vetoridade) - i])
         print (vetoraltura[len(vetoraltura) - i])
         i = i + 1
         

     

