#Nickso Patrick Façanha calheiros - 1615310059


import random
vetor = ["0","1","2","3","4","5","6","7","8"]
cont = 0

while cont < 9:
    print ("Jogo da venha\n")
    print ("%s | %s | %s" % (vetor[0], vetor[1], vetor[2]))
    print ("---------")
    print ("%s | %s | %s" % (vetor[3], vetor[4], vetor[5]))
    print ("---------")
    print ("%s | %s | %s" % (vetor[6], vetor[7], vetor[8]))
    
    if cont%2 == 0:
        num = int(input("Digite a posiçao para jogar: "))
        if vetor[num] == "X" or vetor[num] == "O":
            print ("Erro - Posiçao ja de finida, escolha novamente")
            num = (input("Digite a posiçao para jogar: "))
        else:
            vetor[num] = "X"
        if vetor[0] == vetor[1] and vetor[1] == vetor[2] or vetor[3] == vetor[4] and vetor[4] == vetor[5] or vetor[6] == vetor[7] and vetor[7] == vetor[8] or vetor[0] == vetor[3] and vetor[3] == vetor[6] or vetor[1] == vetor[4] and vetor[4] == vetor[7] or vetor[2] == vetor[5] and vetor[5] == vetor[8] or vetor[0] == vetor[4] and vetor[4] == vetor[8] or vetor[2] == vetor[4] and vetor[4] == vetor[6]:
            print ("Voce ganhou, voce e o bixao mesrmo em doido !!!")
            cont = 20
    if cont%2 != 0:
        num1 = random.randint(0,8)
        while vetor[num1] == "X" or vetor[num1] == "O":
            num1 = random.randint(0,8)
        else:
            vetor[num1] = "O"
        if vetor[0] == vetor[1] and vetor[1] == vetor[2] or vetor[3] == vetor[4] and vetor[4] == vetor[5] or vetor[6] == vetor[7] and vetor[7] == vetor[8] or vetor[0] == vetor[3] and vetor[3] == vetor[6] or vetor[1] == vetor[4] and vetor[4] == vetor[7] or vetor[2] == vetor[5] and vetor[5] == vetor[8] or vetor[0] == vetor[4] and vetor[4] == vetor[8] or vetor[2] == vetor[4] and vetor[4] == vetor[6]:
            print ("Voce perdeu para a maquina mais burra do mundo, voce e o bixao mesrmo em doido !!!")
            cont = 20
    cont += 1
if cont == 9:
    print ("O jogo velhou!!! \nEmpate tecnico")
    
        
        
            
        
        
    
