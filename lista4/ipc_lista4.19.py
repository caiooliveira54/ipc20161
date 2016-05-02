#
#introdução a programação de computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Kylciane Cristiny Lopes Freitas - 1615310052
#Frankilin Yuri Gonçaves dos santos - 1615310033
#Lucas Ferreira Soares - 1615310014
#Luiz Gustavo Rocha Melo - 1615310015
#
#
#Questao 19

votos = [0 ,0, 0, 0, 0, 0]
sistemas =["1- Windows Server", "2- Unix", "3- Linux","4- Netware","5- Mac OS","6- Outro","0- Sair da enquete"]
continua = True
total = 0
porc_votos = []

while(continua):
    
    print("Qual o melhor sistema operacional para uso em servidores ?")
    for i in range(len(sistemas)-1):
        print(sistemas[i])
        
    escolha = int(input())
    
    if(escolha == 1):
        votos[escolha - 1] += 1
    elif(escolha == 2):
        votos[escolha - 1] += 1
    elif(escolha == 3):
        votos[escolha - 1] += 1
    elif(escolha == 4):
        votos[escolha - 1] += 1
    elif(escolha == 5):
        votos[escolha - 1] += 1
    elif(escolha == 6):
        votos[escolha - 1] += 1
    elif(escolha == 0):
        continua = False
    else:
        print("digite um valor válido !")
        
for i in range(len(votos)):
    total += votos[i]

for i in range(len(votos)):
    x = votos[i]*100/total
    porc_votos.append(x)
    
print("Sistema Operacional\t Votos\t %")
print("------------------\t -----\t -\n")
mensagem =''
espaco1 = 19
espaco2 = 5
espaco = ' '
for i in range(len(votos)):
    
    campo1 = espaco  * (espaco1 - len(sistemas[i]))
    campo2 = espaco * (espaco2 - len(str(votos[i])))
    mensagem = sistemas[i] + campo1 +"\t" + str(votos[i])+ campo2 + "\t" + str(porc_votos[i])
    print(mensagem)
    
print("\n------------------\t -----\t -")
print("Total:" + "\t"+ str(total))






