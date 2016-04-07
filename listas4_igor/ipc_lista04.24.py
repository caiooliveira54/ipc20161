import random
vetor = [] #Vetor que representa o dado

for i in range(100): #Contara as 100 vezes que o dado for lancado
    vetor.append(random.randint(1,6)) #Adiciona a um contador de inteiros aleatorio nas 6 faces do dado

for i in range(1,7): 
    print("A face %i apareceu %i vezes"%(i, vetor.count(i))) #Mostra quantas vezes cada face aparece, com um contador de indices
